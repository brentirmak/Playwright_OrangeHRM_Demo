import pytest
import time
import base64
import os
import resend
from playwright.sync_api import sync_playwright
from utils.mysql_logger import log_test_result
from playwright.sync_api import Page
from utils.config import RESEND_API_KEY
from utils.config import EMAIL_ALERT_RECIPIENT

# Initialize Resend with the imported key
resend.api_key = RESEND_API_KEY
email_alert_recipient = EMAIL_ALERT_RECIPIENT

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """Store the flag directly on the Session instance at startup."""
    session.first_failure_alert_sent = False

def detect_run_type() -> str:
    """Automatically determines if the test execution is running on Jenkins or manually."""
    if "JENKINS_URL" in os.environ or "BUILD_NUMBER" in os.environ:
        return "jenkins"
    return "manual"

def pytest_addoption(parser):
    """Safely register browser options for both local and Jenkins environments."""
    for opt, kwargs in [
        ("--browser", {"action": "store", "default": "chromium", "help": "Browser to run tests"}),
        ("--browser-channel", {"action": "store", "default": None, "help": "Browser channel (e.g., msedge, chrome)"})
    ]:
        try:
            parser.addoption(opt, **kwargs)
        except Exception:
            # Already registered by pytest-playwright or another plugin; safe to skip
            pass

@pytest.fixture(scope="module")
def shared_page(request):
    browser_val = request.config.getoption("--browser")
    browser_name = browser_val[0].lower() if isinstance(browser_val, list) else browser_val.lower()
    playwright = sync_playwright().start()
    browser = None
    try:
        if browser_name == "firefox":
            browser = playwright.firefox.launch(headless=True)
        elif browser_name == "webkit":
            browser = playwright.webkit.launch(headless=True)
        elif browser_name in ["edge", "msedge"]:
            browser = playwright.chromium.launch(channel="msedge", headless=True)
        elif browser_name in ["chrome", "google-chrome"]:
            browser = playwright.chromium.launch(channel="chrome", headless=True)
        else:
            # Default to standard Playwright Chromium
            browser = playwright.chromium.launch(headless=True)

        context = browser.new_context()
        page = context.new_page()
        yield page
    finally:
        if browser:
            browser.close()
        playwright.stop()

# attach login duration if needed
@pytest.fixture(scope="function", autouse=True)
def timing(request):
    request.node.start_time = time.time()
    yield
    request.node.duration = time.time() - request.node.start_time

def send_failure_alert(script_name: str, test_name: str, error_message: str, screenshot_bytes: bytes, recipient, browser_type: str):
    try:
        # Ensure browser_type is safely a string
        if isinstance(browser_type, list):
            browser_type = browser_type[0] if browser_type else "chromium"
        browser_str = str(browser_type)

        encoded_screenshot = base64.b64encode(screenshot_bytes).decode("utf-8")

        params = {
            "from": "Playwright - OrangeHRM Test Automation <onboarding@resend.dev>",
            "to": [f"{recipient}"],
            "subject": f"❌ [{browser_str.upper()}] {script_name} - First Test Failure: {test_name}",
            "html": f"""
                <h2>Test Automation Failure Alert</h2>
                <p><strong>Browser:</strong> {browser_str}</p>
                <p><strong>Test Name:</strong> {test_name}</p>
                <p><strong>Error Details:</strong></p>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px;">{error_message}</pre>
                <p>A screenshot of the failure state is attached below.</p>
            """,
            "attachments": [
                {
                    "filename": f"{test_name}_{browser_str}_failure.png",
                    "content": encoded_screenshot,
                }
            ],
        }

        email = resend.Emails.send(params)
        print(f"📧 [Resend] First failure email sent successfully! ID: {email.get('id')}")
    
    except Exception as e:
        print(f"⚠️ [Resend Error] Failed to send error alert email: {e}")

# MySQL logging & First-Failure Alerting hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when != "call":
        return

    status = "passed" if result.passed else "failed"
    error = str(result.longrepr) if result.failed else None
    login_duration = getattr(item, "login_duration", None)
    duration = result.duration
    script_name = os.path.basename(str(item.fspath))
    run_type = detect_run_type()

    # 1. Log to MySQL normally
    log_test_result(
        test_name=item.name,
        script_name=script_name,
        status=status,
        duration=duration,
        error_message=error,
        login_duration=login_duration,
        run_type=run_type,
    )

    # 2. Handle First-Failure Email Alert
    if result.failed:
        session = item.session
        already_sent = getattr(session, "first_failure_alert_sent", False)

        if not already_sent:
            # Extract browser type dynamically from pytest config
            browser_type = item.config.getoption("--browser", default="chromium")

            # Smart lookup: find the Playwright Page object regardless of fixture name ('page', 'shared_page', etc.)
            page = item.funcargs.get("page", None)
            if not page:
                for arg_name, arg_value in item.funcargs.items():
                    # Check if the object is a Playwright Page instance
                    if type(arg_value).__name__ == "Page":
                        page = arg_value
                        break

            if page:
                # Flip lock only AFTER we confirm we found a valid page to screenshot
                session.first_failure_alert_sent = True
                
                try:
                    print(f"📸 Capturing screenshot for first failure in '{item.name}'...")
                    screenshot_bytes = page.screenshot(full_page=True)
                    send_failure_alert(
                        script_name=script_name,
                        test_name=item.name, 
                        error_message=error or "No error traceback available", 
                        screenshot_bytes=screenshot_bytes,
                        recipient=email_alert_recipient,
                        browser_type=browser_type, # Passed successfully here
                    )
                except Exception as e:
                    print(f"⚠️ Could not capture screenshot or send failure alert: {e}")
            else:
                print(f"⚠️ No Playwright Page fixture found in funcargs for '{item.name}'. Skipping alert.")
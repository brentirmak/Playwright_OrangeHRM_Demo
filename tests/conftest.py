import pytest
import time
from playwright.sync_api import Browser, BrowserContext, sync_playwright
from mysql_logger import log_test_result
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app_username = os.getenv("APP_USERNAME")
app_password = os.getenv("APP_PASSWORD")

@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=True)
       yield browser
       browser.close()

#@pytest.fixture
#def page(browser):
#   page = browser.new_page()
#   yield page
#   page.close()

@pytest.fixture(scope="session")
def page(request):
    with sync_playwright() as p:
        #browser = p.chromium.launch(headless=False)
        browser = p.firefox.launch(headless=True)

        context = browser.new_context()

        # SINGLE TAB
        page = context.new_page()

        # Start timing
        login_start = time.time()

        # LOGIN ONCE
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        page.locator("//input[@name='username']").fill(app_username) 
        page.locator("//input[@name='password']").fill(app_password)
        page.locator("//button[@type='submit']").click()

        page.wait_for_url("**/dashboard/index")

        # End timing
        login_duration = time.time() - login_start

        # Attach login duration to pytest session object
        request.session.login_duration = login_duration

        yield page

        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    start_time = time.time()
    outcome = yield
    result = outcome.get_result()

    # Only log after the test "call" phase (not setup/teardown)
    if result.when == "call":
        duration = time.time() - start_time
        status = "passed" if result.passed else "failed"
        error_message = str(result.longrepr) if result.failed else None

        # Retrieve login duration from session (if available)
        login_duration = getattr(item.session, "login_duration", None)

        log_test_result(
            test_name=item.name,
            status=status,
            duration=duration,
            error_message=error_message,
            login_duration=login_duration
        )
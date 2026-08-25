import pytest
import time
import os
from playwright.sync_api import sync_playwright
from utils.mysql_logger import log_test_result

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run tests: chromium, firefox, webkit"
    )

#@pytest.fixture(scope="session")
@pytest.fixture(scope="module")
def shared_page(request):
    browser_name = request.config.getoption("--browser").lower()
    playwright = sync_playwright().start()
    browser = None
    try:
        if browser_name == "firefox":
            browser = playwright.firefox.launch(headless=True)
        elif browser_name == "webkit":
            browser = playwright.webkit.launch(headless=True)
        else:
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


# MySQL logging hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    result = outcome.get_result()

    if result.when != "call":
        return

    status = "passed" if result.passed else "failed"
    error = str(result.longrepr) if result.failed else None

    login_duration = getattr(item, "login_duration", None)
    duration = getattr(item, "duration", result.duration)

    # Extract the filename (e.g., "test_login.py")
    script_name = os.path.basename(item.fspath)

    log_test_result(
        test_name=item.name,
        script_name=script_name,
        status=status,
        duration=duration,
        error_message=error,
        login_duration=login_duration
    )
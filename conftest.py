import pytest
import time
from playwright.sync_api import sync_playwright
from utils.mysql_logger import log_test_result

@pytest.fixture(scope="session")
def shared_page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

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

    log_test_result(
        test_name=item.name,
        status=status,
        duration=duration,
        error_message=error,
        login_duration=login_duration
    )
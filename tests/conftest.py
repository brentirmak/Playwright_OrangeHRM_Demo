import pytest
from playwright.sync_api import Browser, BrowserContext, sync_playwright

@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       yield browser
       browser.close()

#@pytest.fixture
#def page(browser):
#   page = browser.new_page()
#   yield page
#   page.close()

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        #browser = p.chromium.launch(headless=False)
        browser = p.firefox.launch(headless=False)

        context = browser.new_context()

        # SINGLE TAB
        page = context.new_page()

        # LOGIN ONCE
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        #page.get_by_role("textbox", name="Username").fill("Admin")
        #page.get_by_role("textbox", name="Password").fill("admin123")
        #page.get_by_role("button", name="Login").click()

        page.locator("//input[@name='username']").fill("Admin") 
        page.locator("//input[@name='password']").fill("admin123")
        page.locator("//button[@type='submit']").click()

        page.wait_for_url("**/dashboard/index")

        yield page

        browser.close()


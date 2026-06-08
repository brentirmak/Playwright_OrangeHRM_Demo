from pages.login_page import LoginPage
from pages.leave_page import LeavePage
from utils.config import APP_USERNAME, APP_PASSWORD
from playwright.sync_api import expect


def test_leave(page):

    LoginPage(page).login(APP_USERNAME, APP_PASSWORD)

    LeavePage(page).open_leave()

    expect(
        page.get_by_role("heading", name="Leave List")
    ).to_be_visible()

    expect(
        page.get_by_role("button", name="Search")
    ).to_be_visible()
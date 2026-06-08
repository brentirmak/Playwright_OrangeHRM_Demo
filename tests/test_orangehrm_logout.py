from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from utils.config import APP_USERNAME, APP_PASSWORD
from playwright.sync_api import expect


def test_logout(page):

    LoginPage(page).login(APP_USERNAME, APP_PASSWORD)

    LogoutPage(page).logout()

    expect(page.get_by_role("button", name="Login")).to_be_visible()
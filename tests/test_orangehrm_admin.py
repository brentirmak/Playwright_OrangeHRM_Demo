from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.config import APP_USERNAME, APP_PASSWORD
from playwright.sync_api import expect


def test_admin(page):

    LoginPage(page).login(APP_USERNAME, APP_PASSWORD)

    AdminPage(page).open_admin()

    expect(page.get_by_text("System Users")).to_be_visible()
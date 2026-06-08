from pages.login_page import LoginPage
from utils.config import APP_USERNAME, APP_PASSWORD


def test_home(page):

    login = LoginPage(page)
    login.login(APP_USERNAME, APP_PASSWORD)

    assert "dashboard" in page.url
from pages.login_page import LoginPage
from pages.performance_page import PerformancePage
#from utils.config import APP_USERNAME, APP_PASSWORD
from playwright.sync_api import expect


def test_performance(page):

    def __init__(self, page):
        self.page = page

    #LoginPage(page).login(APP_USERNAME, APP_PASSWORD)

    performance = PerformancePage(page)
    performance.open_performance()

    expect(page.get_by_text("Employee Reviews")).to_be_visible()
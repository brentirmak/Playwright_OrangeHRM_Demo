from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page):
        self.page = page
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
        self.dashboard_menu = page.get_by_role("link", name="Dashboard")
        self.performance_menu = page.get_by_role("link", name="Performance")

    def is_upgrade_button_visible(self):
        expect(self.upgrade_button).to_be_visible()
    
    def click_performance_menu(self):
        self.performance_menu.click()

    def click_dashboard_menu(self):
        self.dashboard_menu.click()
    

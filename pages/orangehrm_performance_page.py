from playwright.sync_api import Page, expect

class PerformancePage:
    def __init__(self, page):
        self.page = page
        self.performance_menu = page.get_by_role("link", name="Performance")
        self.my_reviews_menu = page.get_by_role("menuitem", name="My Reviews")
    
    def click_performance_menu(self):
        self.performance_menu.click()
    

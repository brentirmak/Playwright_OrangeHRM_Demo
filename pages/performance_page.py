class PerformancePage:

    def __init__(self, page):
        self.page = page
        self.performance_menu = page.get_by_role("link", name="Performance")

    def open_performance(self):
        self.performance_menu.click()
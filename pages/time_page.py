class TimePage:

    def __init__(self, page):
        self.page = page
        self.time_menu = page.get_by_role("link", name="Time")

    def click_time_menu(self):
        self.time_menu.click()
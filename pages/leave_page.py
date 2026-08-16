class LeavePage:

    def __init__(self, page):
        self.page = page
        self.leave_menu = page.get_by_role("link", name="Leave")

    def click_leave_menu(self):
        self.leave_menu.click()
class LeavePage:

    def __init__(self, page):
        self.page = page
        self.leave_menu = page.get_by_role("link", name="Leave")

    def open_leave(self):
        self.leave_menu.click()
class AdminPage:

    def __init__(self, page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")

    def open_admin(self):
        self.admin_menu.click()
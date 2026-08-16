class AdminPage:

    def __init__(self, page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")

    def click_admin_menu(self):
        self.admin_menu.click()
        self.page.wait_for_load_state("networkidle")
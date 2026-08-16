class MyInfoPage:

    def __init__(self, page):
        self.page = page
        self.myinfo_menu = page.get_by_role("link", name="My Info")

    def click_myinfo_menu(self):
        self.myinfo_menu.click()
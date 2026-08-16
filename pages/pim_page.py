class PIMPage:

    def __init__(self, page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")

    def click_pim_menu(self):
        self.pim_menu.click()
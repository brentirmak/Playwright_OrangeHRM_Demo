class BuzzPage:

    def __init__(self, page):
        self.page = page
        self.buzz_menu = page.get_by_role("link", name="Buzz")

    def click_buzz_menu(self):
        self.buzz_menu.click()
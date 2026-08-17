class DirectoryPage:

    def __init__(self, page):
        self.page = page
        self.directory_menu = page.get_by_role("link", name="Directory")

    def click_directory_menu(self):
        self.directory_menu.click()
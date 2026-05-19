class LogoutPage:
    def __init__(self, page):
        self.page = page
        #self.logout_link = page.get_by_role("menuitem", name="Logout")

    def click_logout(self):
        #self.logout_link.click()
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/logout")
from playwright.sync_api import expect

class LogoutPage:

    def __init__(self, page):
        self.page = page

        self.profile_menu = page.locator(".oxd-userdropdown-tab")
        self.logout_link = page.get_by_role("menuitem", name="Logout")

    def click_logout(self):

        self.profile_menu.click()
        self.page.wait_for_load_state("networkidle")
        expect(self.logout_link).to_be_visible()
        self.logout_link.click()
        self.page.wait_for_load_state("networkidle")
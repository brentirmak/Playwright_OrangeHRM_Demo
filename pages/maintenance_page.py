class MaintenancePage:

    def __init__(self, page):
        self.page = page
        self.maintenance_menu = page.get_by_role("link", name="Maintenance")
        self.cancel_button = page.get_by_role("button", name="Cancel")

    def click_maintenance_menu(self):
        self.maintenance_menu.click()

    def click_cancel_button(self):
        self.cancel_button.click()
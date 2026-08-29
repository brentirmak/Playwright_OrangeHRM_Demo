class LeavePage:

    def __init__(self, page):
        self.page = page
        self.leave_menu = page.get_by_role("link", name="Leave")
        self.apply_submenu = page.get_by_role("link", name="Apply")
        self.my_leave_submenu = page.get_by_role("link", name="My Leave")
        self.entitlements_submenu = page.locator("//li[contains(.,'Entitlements')]")
        self.add_entitlements_submenu = page.locator("//a[contains(.,'Add Entitlements')]")
        self.employee_entitlements_submenu = page.get_by_role("menuitem", name="Employee Entitlements")
        self.my_entitlements_submenu = page.locator("//a[contains(.,'My Entitlements')]")
        self.reports_submenu = page.locator("//li[contains(.,'Reports')]")
        self.leave_entitlements_and_usage_report_submenu = page.get_by_role("menuitem", name="Leave Entitlements and Usage Report", exact=True)
        self.my_leave_entitlements_and_usage_report_submenu = page.get_by_role("menuitem", name="My Leave Entitlements and")
        self.configure_submenu = page.locator("//li[contains(.,'Configure')]")
        self.leave_period_submenu = page.get_by_role("menuitem", name="Leave Period")
        self.leave_types_submenu = page.get_by_role("menuitem", name="Leave Types")
        self.work_week_submenu = page.get_by_role("menuitem", name="Work Week")
        self.holidays_submenu = page.get_by_role("menuitem", name="Holidays")
        self.leave_list_submenu = page.get_by_role("link", name="Leave List")
        self.assign_leave_submenu = page.get_by_role("link", name="Assign Leave")

    def click_leave_menu(self):
        self.leave_menu.click()
        self.page.wait_for_load_state("networkidle")

    def click_apply_submenu(self):
        self.apply_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_my_leave_submenu(self):
        self.my_leave_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_entitlements_submenu(self):
        self.entitlements_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_add_entitlements_submenu(self):
        self.add_entitlements_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_employee_entitlements_submenu(self):
        self.employee_entitlements_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_my_entitlements_submenu(self):
        self.my_entitlements_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_reports_submenu(self):
        self.reports_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_entitlements_and_usage_report_submenu(self):
        self.leave_entitlements_and_usage_report_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_my_leave_entitlements_and_usage_report_submenu(self):
        self.my_leave_entitlements_and_usage_report_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_configure_submenu(self):
        self.configure_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_period_submenu(self):
        self.leave_period_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_types_submenu(self):
        self.leave_types_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_work_week_submenu(self):
        self.work_week_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_holidays_submenu(self):
        self.holidays_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_list_submenu(self):
        self.leave_list_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_assign_leave_submenu(self):
        self.assign_leave_submenu.click()
        self.page.wait_for_load_state("networkidle")

class LeavePage:

    def __init__(self, page):
        self.page = page
        self.leave_menu = page.get_by_role("link", name="Leave")
        
        self.leave_apply_submenu = page.get_by_role("link", name="Apply")
        self.leave_my_leave_submenu = page.get_by_role("link", name="My Leave")
        self.leave_entitlements_submenu = page.locator("//li[contains(.,'Entitlements')]")
        self.leave_entitlements_add_entitlements_submenu = page.locator("//a[contains(.,'Add Entitlements')]")
        self.leave_entitlements_employee_entitlements_submenu = page.get_by_role("menuitem", name="Employee Entitlements")
        self.leave_entitlements_my_entitlements_submenu = page.locator("//a[contains(.,'My Entitlements')]")
        self.leave_reports_submenu = page.locator("//li[contains(.,'Reports')]")
        self.leave_reports_leave_entitlements_and_usage_report_submenu = page.get_by_role("menuitem", name="Leave Entitlements and Usage Report", exact=True)
        self.leave_reports_my_leave_entitlements_and_usage_report_submenu = page.get_by_role("menuitem", name="My Leave Entitlements and")
        self.leave_configure_submenu = page.locator("//li[contains(.,'Configure')]")
        self.leave_configure_leave_period_submenu = page.get_by_role("menuitem", name="Leave Period")
        self.leave_configure_leave_types_submenu = page.get_by_role("menuitem", name="Leave Types")
        self.leave_configure_work_week_submenu = page.get_by_role("menuitem", name="Work Week")
        self.leave_configure_holidays_submenu = page.get_by_role("menuitem", name="Holidays")
        self.leave_leave_list_submenu = page.get_by_role("link", name="Leave List")
        self.leave_assign_leave_submenu = page.get_by_role("link", name="Assign Leave")

    def click_leave_menu(self):
        self.leave_menu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_apply_submenu(self):
        self.leave_apply_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_my_leave_submenu(self):
        self.leave_my_leave_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_entitlements_submenu(self):
        self.leave_entitlements_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_entitlements_add_entitlements_submenu(self):
        self.leave_entitlements_add_entitlements_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_entitlements_employee_entitlements_submenu(self):
        self.leave_entitlements_employee_entitlements_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_entitlements_my_entitlements_submenu(self):
        self.leave_entitlements_my_entitlements_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_reports_submenu(self):
        self.leave_reports_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_reports_leave_entitlements_and_usage_report_submenu(self):
        self.leave_reports_leave_entitlements_and_usage_report_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_reports_my_leave_entitlements_and_usage_report_submenu(self):
        self.leave_reports_my_leave_entitlements_and_usage_report_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_configure_submenu(self):
        self.leave_configure_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_configure_leave_period_submenu(self):
        self.leave_configure_leave_period_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_configure_leave_types_submenu(self):
        self.leave_configure_leave_types_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_configure_work_week_submenu(self):
        self.leave_configure_work_week_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_configure_holidays_submenu(self):
        self.leave_configure_holidays_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_leave_list_submenu(self):
        self.leave_leave_list_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_leave_assign_leave_submenu(self):
        self.leave_assign_leave_submenu.click()
        self.page.wait_for_load_state("networkidle")

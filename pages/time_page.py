class TimePage:

    def __init__(self, page):
        self.page = page
        self.time_menu = page.get_by_role("link", name="Time")
        self.timesheets_submenu = page.get_by_label("Topbar Menu").get_by_text("Timesheets")
        self.my_timesheets_submenu = page.get_by_role("menuitem", name="My Timesheets")
        self.attendance_submenu = page.get_by_role("listitem").filter(has_text="Attendance")
        self.my_records_submenu = page.get_by_role("menuitem", name="My Records")
        self.punchin_punchout_submenu = page.get_by_role("menuitem", name="Punch In/Out")
        self.employee_records_submenu = page.get_by_role("menuitem", name="Employee Records")
        self.configuration_submenu = page.get_by_role("menuitem", name="Configuration")
        self.reports_submenu = page.get_by_role("listitem").filter(has_text="Reports")
        self.project_reports_submenu = page.get_by_role("menuitem", name="Project Reports")
        self.employee_reports_submenu = page.get_by_role("menuitem", name="Employee Reports")
        self.attendance_summary_submenu = page.get_by_role("menuitem", name="Attendance Summary")
        self.project_info_submenu = page.get_by_role("listitem").filter(has_text="Project Info")
        self.customers_submenu = page.get_by_role("menuitem", name="Customers")
        self.projects_submenu = page.get_by_role("menuitem", name="Projects")

    def click_time_menu(self):
        self.time_menu.click()

    def click_timesheets_submenu(self):
        self.timesheets_submenu.click()

    def click_my_timesheets_submenu(self):
        self.my_timesheets_submenu.click()

    def click_attendance_submenu(self):
        self.attendance_submenu.click()

    def click_my_records_submenu(self):
        self.my_records_submenu.click()

    def click_punchin_punchout_submenu(self):
        self.punchin_punchout_submenu.click()

    def click_employee_records_submenu(self):
        self.employee_records_submenu.click()

    def click_configuration_submenu(self):
        self.configuration_submenu.click()

    def click_reports_submenu(self):
        self.reports_submenu.click()

    def click_project_reports_submenu(self):
        self.project_reports_submenu.click()

    def click_employee_reports_submenu(self):
        self.employee_reports_submenu.click()

    def click_attendance_summary_submenu(self):
        self.attendance_summary_submenu.click()

    def click_project_info_submenu(self):
        self.project_info_submenu.click()

    def click_customers_submenu(self):
        self.customers_submenu.click()

    def click_projects_submenu(self):
        self.projects_submenu.click()
    
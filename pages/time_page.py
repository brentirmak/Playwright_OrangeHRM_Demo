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

        #####################################################################################################################
        #
        # Attendance My Records page
        self.time_attendance_my_records_delete_all_checkbox = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span/i")
        self.time_attendance_my_records_trash_icons = page.locator("//div[contains(@class, 'orangehrm-container')]//i[contains(@class,'oxd-icon bi-trash')]")
        self.time_attendance_my_records_delete_selected_button = page.locator("xpath=//button[@type='button'][contains(.,'Delete Selected')]")
        self.time_attendance_my_records_confirm_delete_button = page.locator("xpath=//button[@type='button'][contains(.,'Yes, Delete')]")
        self.time_attendance_my_records_successfully_deleted_message = page.locator("xpath=//p[contains(.,'Successfully Deleted')]")
        #####################################################################################################################
        #
        # Attendance Punch In/Punch Out page
        
        self.time_attendance_punchinpunchout_punchin_label = page.locator("xpath=//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title'][contains(.,'Punch In')]")
        self.time_attendance_punchinpunchout_punchin_date_field = page.locator("xpath=//input[contains(@placeholder,'yyyy-dd-mm')]")
        self.time_attendance_punchinpunchout_punchin_time_field = page.locator("xpath=//input[@placeholder='hh:mm']")
        self.time_attendance_punchinpunchout_in_button = page.locator("xpath=//button[@type='submit'][contains(.,'In')]")
        
        self.time_attendance_punchinpunchout_punchout_label = page.locator("xpath=//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title'][contains(.,'Punch Out')]")
        self.time_attendance_punchinpunchout_punchout_date_field = page.locator("xpath=//input[contains(@placeholder,'yyyy-dd-mm')]")
        self.time_attendance_punchinpunchout_punchout_time_field = page.locator("xpath=//input[@placeholder='hh:mm']")
        self.time_attendance_punchinpunchout_out_button = page.locator("xpath=//button[@type='submit'][contains(.,'Out')]")

        self.time_attendance_punchinpunchedout_punched_in_time_label = page.locator("xpath=//label[contains(.,'Punched in time')]")
        self.time_attendance_punchout_successfully_saved_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")
        self.time_attendance_punchin_successfully_saved_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")

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


    #####################################################################################################################
    #
    # Attendance - My attendance functions

    def click_my_attendance_records_delete_all_checkbox(self):
        self.time_attendance_my_records_delete_all_checkbox.click()

    def click_my_attendance_records_delete_selected_button(self):
        self.time_attendance_my_records_delete_selected_button.click(timeout=5000)

    def click_my_attendance_records_confirm_delete_button(self):
        self.time_attendance_my_records_confirm_delete_button.click(timeout=5000)


    #####################################################################################################################
    #
    # Attendance Punch In/Punch Out functions

    def click_time_attendance_punchinpunchout_punchin_date_field(self):
        self.time_attendance_punchinpunchout_punchin_date_field.click()

    def enter_time_attendance_punchinpunchout_punchin_date_field_value(self, punchin_date):
        self.time_attendance_punchinpunchout_punchin_date_field.fill(punchin_date)

    def click_time_attendance_punchinpunchout_punchin_time_field(self):
        self.time_attendance_punchinpunchout_punchin_time_field.click()

    def enter_time_attendance_punchinpunchout_punchin_time_field_value(self, punchin_time):
        self.time_attendance_punchinpunchout_punchin_time_field.fill(punchin_time)

    def click_time_attendance_punchinpunchout_punchin_button(self):
        self.time_attendance_punchinpunchout_in_button.click()

    def click_time_attendance_punchinpunchout_punchout_date_field(self):
        self.time_attendance_punchinpunchout_punchout_date_field.click()

    def enter_time_attendance_punchinpunchout_punchout_date_field_value(self, punchout_date):
        self.time_attendance_punchinpunchout_punchout_date_field.fill(punchout_date)

    def click_time_attendance_punchinpunchout_punchout_time_field(self):
        self.time_attendance_punchinpunchout_punchout_time_field.click()

    def enter_time_attendance_punchinpunchout_punchout_time_field_value(self, punchout_time):
        self.time_attendance_punchinpunchout_punchout_time_field.fill(punchout_time)

    def click_time_attendance_punchinpunchout_punchout_button(self):
        self.time_attendance_punchinpunchout_out_button.click()

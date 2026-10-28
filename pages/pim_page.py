import re

class PIMPage:

    def __init__(self, page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")

        # Employee List / Add Employee
        self.pim_employee_list_add_button = page.locator("xpath=//button[@type='button'][contains(.,'Add')]")
        self.pim_employee_add_employee_first_name_field = page.locator("xpath=//input[@placeholder='First Name']")
        self.pim_employee_add_employee_last_name_field = page.locator("xpath=//input[@placeholder='Last Name']")
        self.pim_employee_add_employee_id_field = page.get_by_role("textbox").nth(4)
        self.pim_employee_add_employee_save_button = page.locator("xpath=//button[contains(.,'Save')]")
        self.pim_employee_add_employee_successfully_saved_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")
        
        # Employee List / Search Employee
        self.pim_employee_list_employee_name_field = page.get_by_role("textbox", name="Type for hints...").first
        self.pim_employee_list_employee_search_button = page.get_by_role("button", name="Search")
        self.pim_employee_list_reset_button = page.get_by_role("button", name="Reset")
        self.pim_employee_list_employment_status_dropdown = page.get_by_text("-- Select --").first
        self.pim_employee_list_employment_full_time_permanent_option = page.get_by_text("Full-Time Permanent")

        # Employee List / Delete Employee
        self.pim_employee_list_delete_employee_checkbox_field = page.locator(".oxd-table-card-cell-checkbox > .oxd-checkbox-wrapper > label > .oxd-checkbox-input > .oxd-icon")
        self.pim_employee_list_delete_employee_delete_selected_button = page.locator("xpath=//button[contains(.,'Delete Selected')]")
        self.pim_employee_list_delete_employee_confirm_button = page.locator("xpath=//button[@type='button'][contains(.,'Yes, Delete')]")

        # Reports / Add Reports
        self.pim_reports_tab = page.get_by_role("listitem").filter(has_text="Reports")
        self.pim_reports_employee_reports_add_button = page.locator("xpath=//button[@type='button'][contains(.,'Add')]")
        self.pim_reports_add_report_header = page.locator("xpath=//h6[contains(.,'Add Report')]")
        self.pim_reports_add_report_name_field = page.get_by_role("textbox", name="Type here")
        self.pim_reports_add_report_selection_criteria_dropdown = page.get_by_text("-- Select --").first
        self.pim_reports_add_report_selection_employee_name_option = page.get_by_text("Employee Name")
        self.pim_reports_add_report_include_dropdown = page.get_by_text("Current Employees Only")
        self.pim_reports_add_report_current_and_past_employees_only_option = page.get_by_text("Current and Past Employees")
        self.pim_reports_add_report_display_field_group_dropdown = page.get_by_text("-- Select --").first
        self.pim_reports_add_report_display_field_group_dropdown_personal_option = page.get_by_text("Personal")
        self.pim_reports_add_report_select_display_field_dropdown = page.get_by_text("-- Select --")
        self.pim_reports_add_report_select_display_field_dropdown_employee_id_option = page.get_by_text("Employee Id")
        self.pim_reports_add_report_add_display_fields_button = page.get_by_role("button").nth(4)
        self.pim_reports_add_report_save_button = page.locator("xpath=//button[contains(.,'Save')]")

        # Reports / Search Reports
        self.pim_reports_employee_reports_header = page.locator("xpath=//h5[contains(.,'Employee Reports')]")
        self.pim_reports_search_report_report_name_field = page.get_by_role("textbox", name="Type for hints...")
        self.pim_reports_search_report_report_name_field_option = page.get_by_role("option").get_by_text("Temporary Test Report")
        self.pim_reports_search_report_search_button = page.locator("xpath=//button[contains(.,'Search')]")
        self.pim_reports_search_report_test_report_icon = page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(5)
        #self.pim_add_report_button = page.get_by_role("button", name=" Add")
        #self.pim_to_be_deleted_report_checkbox = page.get_by_role("row", name=" Temporary Test Report   ").locator("label")
        #self.pim_to_be_deleted_report_delete_button = page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3)

        # Reports / Delete Reports
        self.delete_button = page.get_by_role("button", name=" Delete Selected")
        self.pim_delete_report_confirm_button = page.get_by_role("button", name=" Yes, Delete")

    def click_pim_menu(self):
        self.pim_menu.click()

    def click_pim_reports_tab(self):
        self.pim_reports_tab.click()

    #################################################################################################################
    # PIM - Add Employee methods
    #################################################################################################################

    def click_pim_employee_list_add_employee_button(self):
        self.pim_employee_list_add_button.click()

    def click_pim_employee_add_employee_first_name_field(self):
        self.pim_employee_add_employee_first_name_field.click()

    def enter_pim_employee_add_employee_first_name_field_value(self,first_name):
        self.pim_employee_add_employee_first_name_field.fill(first_name)

    def click_pim_employee_add_employee_last_name_field(self):
        self.pim_employee_add_employee_last_name_field.click()

    def enter_pim_employee_add_employee_last_name_field_value(self,last_name):
        self.pim_employee_add_employee_last_name_field.fill(last_name)

    def click_pim_employee_add_employee_id_field(self):
        self.pim_employee_add_employee_id_field.click()

    def enter_pim_employee_add_employee_id_field_value(self, employee_id):
        self.pim_employee_add_employee_id_field.fill(employee_id)

    def click_pim_employee_add_employee_save_button(self):
        self.pim_employee_add_employee_save_button.click()

    #################################################################################################################
    # PIM - Search Employee methods
    #################################################################################################################

    def click_pim_employee_list_employee_name_field(self):
        self.pim_employee_list_employee_name_field.click()

    def enter_pim_employee_list_employee_name_field_value(self,name):
        self.pim_employee_list_employee_name_field.fill(name)

    def get_pim_employee_list_employee_option_by_name(self, name: str):
        """Returns the first option matching the given employee name."""
        return self.page.get_by_role("option", name=name).first

    def click_pim_employee_list_employee_search_button(self):
        self.pim_employee_list_employee_search_button.click()

    def click_pim_employee_list_reset_button(self):
        self.pim_employee_list_reset_button.click()

    def click_pim_employee_list_employment_status_dropdown(self):
        self.pim_employee_list_employment_status_dropdown.click()

    def click_pim_employee_list_employment_full_time_permanent_option(self):
        self.pim_employee_list_employment_full_time_permanent_option.click()

    #################################################################################################################
    # PIM - Delete Employee methods
    #################################################################################################################

    def click_pim_employee_list_delete_employee_checkbox_field(self):
        self.pim_employee_list_delete_employee_checkbox_field.click()

    def click_pim_employee_list_delete_employee_delete_selected_button(self):
        self.pim_employee_list_delete_employee_delete_selected_button.click()

    def click_pim_employee_list_delete_employee_confirm_button(self):
        self.pim_employee_list_delete_employee_confirm_button.click()

    #################################################################################################################
    # PIM - Add Reports methods
    #################################################################################################################

    def click_reports_add_report_name_field(self):
        self.pim_reports_add_report_name_field.click()

    def click_reports_add_report_name_field_value(self, report_name):
        self.pim_reports_add_report_name_field.fill(report_name)

    def click_pim_reports_add_report_selection_criteria_dropdown(self):
        self.pim_reports_add_report_selection_criteria_dropdown.click()

    def select_pim_reports_add_report_selection_employee_name_option(self):
        self.pim_reports_add_report_selection_employee_name_option.click()

    def click_reports_add_report_current_and_past_employees_only_option(self):
        self.pim_reports_add_report_current_and_past_employees_only_option.click()

    def click_pim_reports_add_report_include_dropdown(self):
        self.pim_reports_add_report_include_dropdown.click()

    def select_pim_reports_add_report_current_and_past_employees_only_option(self):
        self.pim_reports_add_report_current_and_past_employees_only_option.click()

    def click_pim_reports_add_report_display_field_group_dropdown(self):
        self.pim_reports_add_report_display_field_group_dropdown.click()

    def select_pim_reports_add_report_display_field_group_dropdown_personal_option(self):
        self.pim_reports_add_report_display_field_group_dropdown_personal_option.click()

    def click_pim_reports_add_report_select_display_field_dropdown(self):
        self.pim_reports_add_report_select_display_field_dropdown.click()

    def select_pim_reports_add_report_select_display_field_dropdown_employee_id_option(self):
        self.pim_reports_add_report_select_display_field_dropdown_employee_id_option.click()
    
    def click_pim_reports_add_report_add_display_fields_button(self):
        self.pim_reports_add_report_add_display_fields_button.click()

    def click_pim_reports_add_report_save_button(self):
        self.pim_reports_add_report_save_button.click()

    #################################################################################################################
    # PIM - Search Report methods
    #################################################################################################################

    def click_pim_reports_search_report_report_name_field(self):
        self.pim_reports_search_report_report_name_field.click()

    def enter_pim_reports_search_report_report_name_field(self, report_name):
        self.pim_reports_search_report_report_name_field.fill(report_name)

    def click_pim_reports_search_report_report_name_field_option(self):
        self.pim_reports_search_report_report_name_field_option.click()
    
    def click_pim_reports_search_report_search_button(self):
        self.pim_reports_search_report_search_button.click()

    def click_pim_reports_employee_reports_add_button(self):
        self.pim_reports_employee_reports_add_button.click()

    def click_pim_reports_search_report_test_report_icon(self):
        self.pim_reports_search_report_test_report_icon.click()

    #################################################################################################################
    # PIM - Delete Reports methods
    #################################################################################################################
    
    def click_pim_reports_trashbin_of_tobedeleted_item(self, report_name):
        row = self.page.locator("div.oxd-table-card").filter(has_text=report_name)
        row.get_by_role("button").filter(has=self.page.locator("i.bi-trash")).click()
        self.page.wait_for_load_state("networkidle")

    def click_pim_reports_delete_report_confirm_button(self):
        self.pim_delete_report_confirm_button.click()







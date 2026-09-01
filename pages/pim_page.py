import re

class PIMPage:

    def __init__(self, page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.employee_name_field = page.get_by_role("textbox", name="Type for hints...").first
        self.search_button = page.get_by_role("button", name="Search")
        self.reset_button = page.get_by_role("button", name="Reset")
        self.employment_status_dropdown = page.get_by_text("-- Select --").first
        self.full_time_permanent_option = page.get_by_text("Full-Time Permanent")
        self.add_button = page.get_by_role("button", name=" Add")
        self.first_name_field = page.get_by_role("textbox", name="First Name")
        self.last_name_field = page.get_by_role("textbox", name="Last Name")
        self.employee_id_field = page.get_by_role("textbox").nth(4)
        self.save_button = page.get_by_role("button", name="Save")
        self.checkbox_field = page.locator(".oxd-table-card-cell-checkbox > .oxd-checkbox-wrapper > label > .oxd-checkbox-input > .oxd-icon")
        self.delete_button = page.get_by_role("button", name=" Delete Selected")
        self.confirm_delete_button = page.get_by_role("button", name=" Yes, Delete")
        self.reports_tab = page.get_by_role("listitem").filter(has_text="Reports")
        self.report_name_field = page.get_by_role("textbox", name="Type for hints...")
        self.temporary_test_report_option = page.get_by_role("option").get_by_text("Temporary Test Report")
        self.pim_test_report_icon = page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(5)
        self.pim_add_report_button = page.get_by_role("button", name=" Add")
        self.pim_report_name_field = page.get_by_role("textbox", name="Type here")
        self.pim_selection_criteria_dropdown = page.get_by_text("-- Select --").first
        self.pim_selection_criteria_dropdown_employee_name_option = page.get_by_text("Employee Name")
        self.pim_include_dropdown = page.get_by_text("Current Employees Only")
        self.pim_include_dropdown_current_and_past_employees_only_option = page.get_by_text("Current and Past Employees")
        self.pim_display_field_group_dropdown = page.get_by_text("-- Select --").first
        self.pim_display_field_group_dropdown_personal_option = page.get_by_text("Personal")
        self.pim_select_display_field_dropdown = page.get_by_text("-- Select --")
        self.pim_select_display_field_dropdown_employee_id_option = page.get_by_text("Employee Id")
        self.pim_add_display_fields_button = page.get_by_role("button").nth(4)
        self.pim_to_be_deleted_report_checkbox = page.get_by_role("row", name=" Temporary Test Report   ").locator("label")
        self.pim_to_be_deleted_report_delete_button = page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3)
        self.pim_delete_report_confirm_button = page.get_by_role("button", name=" Yes, Delete")

    def get_employee_option_by_name(self, name: str):
        """Returns the first option matching the given employee name."""
        return self.page.get_by_role("option", name=name).first

    def click_pim_menu(self):
        self.pim_menu.click()

    #################################################################################################################
    # Employee List sub-menu methods
    #################################################################################################################

    def click_employee_name_field(self):
        self.employee_name_field.click()

    def enter_employee_name(self,name):
        self.employee_name_field.fill(name)

    def click_employee_name(self):
        self.first_employee_result.click()

    def click_search_button(self):
        self.search_button.click()

    def click_reset_button(self):
        self.reset_button.click()

    def click_employment_status_dropdown(self):
        self.employment_status_dropdown.click()

    def click_full_time_permanent_option(self):
        self.full_time_permanent_option.click()

    def click_add_button(self):
        self.add_button.click()

    def click_first_name_field(self):
        self.first_name_field.click()

    def enter_first_name(self,first_name):
        self.first_name_field.fill(first_name)

    def click_last_name_field(self):
        self.last_name_field.click()

    def enter_last_name(self,last_name):
        self.last_name_field.fill(last_name)

    def enter_employee_id(self, employee_id):
        self.employee_id_field.fill(employee_id)

    def click_save_button(self):
        self.save_button.click()

    def click_checkbox_field(self):
        self.checkbox_field.click()

    def click_delete_button(self):
        self.delete_button.click()

    def click_confirm_delete_button(self):
        self.confirm_delete_button.click()
    
    def click_reports_tab(self):
        self.reports_tab.click()

    def click_report_name_field(self):
        self.report_name_field.click()

    def fill_report_name_field(self):
        self.report_name_field.fill("Temporary Test Report")

    def click_temporary_test_report_option(self):
        self.temporary_test_report_option.click()

    def click_pim_test_report_icon(self):
        self.pim_test_report_icon.click()

    #################################################################################################################
    # Add Report sub-menu methods
    #################################################################################################################
    def click_pim_add_report_button(self):
        self.pim_add_report_button.click()

    def click_pim_report_name_field(self):
        self.pim_report_name_field.click()

    def enter_pim_report_name(self, report_name):
        self.pim_report_name_field.fill(report_name)

    def click_pim_selection_criteria_dropdown(self):
        self.pim_selection_criteria_dropdown.click()

    def click_pim_selection_criteria_employee_name_option(self):
        self.pim_selection_criteria_dropdown_employee_name_option.click()

    def click_pim_include_dropdown(self):
        self.pim_include_dropdown.click()

    def click_pim_include_current_and_past_employees_only_option(self):
        self.pim_include_dropdown_current_and_past_employees_only_option.click()

    def click_pim_display_field_group_dropdown(self):
        self.pim_display_field_group_dropdown.click()

    def click_pim_display_field_group_dropdown_personal_option(self):
        self.pim_display_field_group_dropdown_personal_option.click()

    def click_pim_select_display_field_dropdown(self):
        self.pim_select_display_field_dropdown.click()

    def click_pim_select_display_field_dropdown_employee_id_option(self):
        self.pim_select_display_field_dropdown_employee_id_option.click()

    def click_pim_add_display_fields_button(self):
        self.pim_add_display_fields_button.click()

    def click_trashbin_of_tobedeleted_item(self):
        row = self.page.locator("div.oxd-table-card").filter(has_text="Temporary Test Report")
        row.get_by_role("button").filter(has=self.page.locator("i.bi-trash")).click()
        self.page.wait_for_load_state("networkidle")


    #def click_pim_to_be_deleted_report_checkbox(self):
    #    self.pim_to_be_deleted_report_checkbox.click()

    #def click_pim_to_be_deleted_report_delete_button(self):
    #    self.pim_to_be_deleted_report_delete_button.click()




    def click_pim_delete_report_confirm_button(self):
        self.pim_delete_report_confirm_button.click()
    
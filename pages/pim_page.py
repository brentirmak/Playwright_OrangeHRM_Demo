import re

class PIMPage:

    def __init__(self, page):
        self.page = page
        #self.pim_menu = page.get_by_role("link", name="PIM")
        self.pim_menu = page.locator("xpath=//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'PIM')]")

        # Employee List / Add Employee
        self.pim_employee_list_add_button = page.locator("xpath=//button[@type='button'][contains(.,'Add')]")
        self.pim_employee_add_employee_first_name_field = page.locator("xpath=//input[@placeholder='First Name']")
        self.pim_employee_add_employee_last_name_field = page.locator("xpath=//input[@placeholder='Last Name']")
        self.pim_employee_add_employee_id_field = page.get_by_role("textbox").nth(4)
        self.pim_employee_add_employee_save_button = page.locator("xpath=//button[contains(.,'Save')]")
        self.pim_employee_add_employee_successfully_saved_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")

        # Employee List / Edit Employee
        self.pim_employee_edit_employee_personal_details_header = page.locator("xpath=//h6[contains(.,'Personal Details')]")
        self.pim_employee_edit_employee_gender_male_selection = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span")
        self.pim_employee_edit_employee_gender_female_selection = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span")
        self.pim_employee_edit_employee_job_tab = page.locator("xpath=//a[contains(.,'Job')]")
        self.pim_employee_edit_employee_job_details_header = page.locator("xpath=//h6[contains(.,'Job Details')]")
        self.pim_employee_edit_employee_job_title_dropdown = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i")
        self.pim_employee_edit_employee_software_engineer_option = page.locator("xpath=//div[@role='option'][contains(.,'Software Engineer')]")
        self.pim_employee_edit_employee_job_category_dropdown = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[1]/div[2]/i")
        self.pim_employee_edit_employee_professionals_option = page.locator("xpath=//div[@role='option'][contains(.,'Professionals')]")
        self.pim_employee_edit_employee_sub_unit_dropdown = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div[1]/div[2]/i")
        self.pim_employee_edit_employee_engineering_option = page.locator("xpath=//span[contains(.,'Engineering')]")
        self.pim_employee_edit_employee_location_dropdown = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[1]/div[2]/i")
        self.pim_employee_edit_employee_hq_ca_option = page.locator("xpath=//span[contains(.,'HQ - CA, USA')]")
        self.pim_employee_edit_employee_employment_status_dropdown = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div[1]/div[2]/i")
        self.pim_employee_edit_employee_full_time_permanent_option = page.locator("xpath=//div[@role='option'][contains(.,'Full-Time Permanent')]")
        self.pim_employee_edit_employee_save1_button = page.locator("xpath=(//button[@type='submit'][contains(.,'Save')])[1]")
        self.pim_employee_edit_employee_save2_button = page.locator("xpath=//button[contains(.,'Save')]")
        self.pim_employee_edit_employee_successfully_updated_message = page.locator("xpath=//p[contains(.,'Successfully Updated')]")
        self.pim_employee_edit_employee_successfully_saved_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")

        # Employee List / Search Employee
        self.pim_employee_list_employee_name_field = page.get_by_role("textbox", name="Type for hints...").first
        self.pim_employee_list_employee_search_button = page.get_by_role("button", name="Search")
        self.pim_employee_list_reset_button = page.get_by_role("button", name="Reset")
        self.pim_employee_list_employment_status_dropdown = page.get_by_text("-- Select --").first
        self.pim_employee_list_employment_full_time_permanent_option = page.locator("xpath=//span[contains(.,'Full-Time Permanent')]")
        self.pim_employee_list_employment_full_time_permanent_result = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[6]/div")
        self.pim_employee_list_user_records = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")

        # Employee List / Delete Employee
        self.pim_employee_list_delete_employee_checkbox_field = page.locator(".oxd-table-card-cell-checkbox > .oxd-checkbox-wrapper > label > .oxd-checkbox-input > .oxd-icon")
        self.pim_employee_list_delete_employee_delete_selected_button = page.locator("xpath=//button[contains(.,'Delete Selected')]")
        self.pim_employee_list_delete_employee_confirm_button = page.locator("xpath=//button[@type='button'][contains(.,'Yes, Delete')]")

        # Bulk Delete
        self.pim_employee_list_bulk_delete_checkbox = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span/i")
        self.pim_employee_list_bulk_delete_delete_selected_button = page.locator("xpath=//button[contains(.,'Delete Selected')]")
        self.pim_employee_list_bulk_delete_delete_confirmation_button = page.locator("xpath=//button[@type='button'][contains(.,'Yes, Delete')]")
        self.pim_employee_list_bulk_delete_successfully_deleted_message = page.locator("xpath=//p[contains(.,'Successfully Deleted')]")
        self.pim_employee_list_one_record_found_header = page.locator("xpath=//span[contains(.,'(1) Record Found')]")

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
    # PIM - Edit Employee methods
    #################################################################################################################

    def click_pim_employee_edit_employee_gender_male_selection(self):
        self.pim_employee_edit_employee_gender_male_selection.click()

    def click_pim_employee_edit_employee_gender_female_selection(self):
        self.pim_employee_edit_employee_gender_female_selection.click()

    def click_pim_employee_edit_employee_job_tab(self):
        self.pim_employee_edit_employee_job_tab.click()

    def click_pim_employee_edit_employee_job_title_dropdown(self):
        self.pim_employee_edit_employee_job_title_dropdown.click()

    def select_pim_employee_edit_employee_job_title_value(self):
        self.pim_employee_edit_employee_software_engineer_option.click()

    def click_pim_employee_edit_employee_job_category_dropdown(self):
        self.pim_employee_edit_employee_job_category_dropdown.click()

    def select_pim_employee_edit_employee_job_category_value(self):
        self.pim_employee_edit_employee_professionals_option.click()

    def click_pim_employee_edit_employee_sub_unit_dropdown(self):
        self.pim_employee_edit_employee_sub_unit_dropdown.click()

    def select_pim_employee_edit_employee_sub_unit_value(self):
        self.pim_employee_edit_employee_engineering_option.click()

    def click_pim_employee_edit_employee_location_dropdown(self):
        self.pim_employee_edit_employee_location_dropdown.click()

    def select_pim_employee_edit_employee_location_value(self):
        self.pim_employee_edit_employee_hq_ca_option.click()

    def click_pim_employee_edit_employee_employment_status_dropdown(self):
        self.pim_employee_edit_employee_employment_status_dropdown.click()

    def select_pim_employee_edit_employee_employment_status_value(self):
        self.pim_employee_edit_employee_full_time_permanent_option.click()

    def click_pim_employee_edit_employee_save1_button(self):
        self.pim_employee_edit_employee_save1_button.click()

    def click_pim_employee_edit_employee_save2_button(self):
        self.pim_employee_edit_employee_save2_button.click()

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

    # Bulk Delete
    def click_pim_employee_list_bulk_delete_checkbox(self):
        self.pim_employee_list_bulk_delete_checkbox.click()

    def click_pim_employee_list_bulk_delete_delete_selected_button(self):
        self.pim_employee_list_bulk_delete_delete_selected_button.click()

    def click_pim_employee_list_bulk_delete_delete_confirmation_button(self):
        self.pim_employee_list_bulk_delete_delete_confirmation_button.click()
    
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







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
    

    
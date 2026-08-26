class PIMPage:

    def __init__(self, page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.employee_name_field = page.get_by_role("textbox", name="Type for hints...").first
        self.search_button = page.get_by_role("button", name="Search")
        self.reset_button = page.get_by_role("button", name="Reset")
        self.employment_status_dropdown = page.get_by_text("-- Select --").first
        self.full_time_permanent_option = page.get_by_text("Full-Time Permanent")

    def get_employee_option_by_name(self, name: str):
        """Returns the first option matching the given employee name."""
        return self.page.get_by_role("option", name=name).first

    def click_pim_menu(self):
        self.pim_menu.click()

    '''
    Employee List sub-menu methods
    '''
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

    
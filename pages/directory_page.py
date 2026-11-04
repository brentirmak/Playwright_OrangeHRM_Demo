import time

class DirectoryPage:

    def __init__(self, page):
        self.page = page
        
        ###################################################################################################################
        # Directory - Identifiers
        #
        
        self.directory_menu = page.get_by_role("link", name="Directory")
        self.directory_directory_header = page.locator("xpath=//h5[contains(.,'Directory')]")

        self.directory_search_button = page.locator("xpath=//button[@type='submit'][contains(.,'Search')]")
        self.directory_reset_button = page.locator("xpath=//button[contains(.,'Reset')]")
        self.directory_employee_name_field = page.locator("xpath=//input[@placeholder='Type for hints...']")
        self.directory_job_title_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]")
        self.directory_job_title_software_engineer_option = page.locator("xpath=//span[contains(.,'Software Engineer')]")
        self.directory_job_title_chief_financial_officer_option = page.locator("xpath=//span[contains(.,'Chief Financial Officer')]")
        self.directory_location_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[2]")
        self.directory_employee_name_chris_collins_value = page.locator("xpath=//div[@role='option'][contains(.,'Chris  Collins')]")
        self.directory_records_found = page.locator("xpath=//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
        self.directory_records_chris_collins_found = page.locator("xpath=//p[contains(.,'Chris  Collins')]")
        self.directory_record_found = page.locator("xpath=//span[contains(.,'(1) Record Found')]")
    ###################################################################################################################
    # Directory - Methods
    #

    def click_directory_menu(self):
        self.directory_menu.click()

    def click_directory_employee_name_field(self):
        self.directory_employee_name_field.click()

    def enter_directory_employee_name_value(self,employee_name):
        if employee_name == "Chris Collins":
            self.directory_employee_name_field.fill("Chris")
            time.sleep(1)
            self.directory_employee_name_chris_collins_value.click()

    def click_directory_job_title_dropdown(self):
        self.directory_job_title_dropdown.click()

    def click_directory_software_engineer_selection(self):
        self.directory_job_title_software_engineer_option.click()

    def click_directory_chief_financial_officer_selection(self):
        self.directory_job_title_chief_financial_officer_option.click()
        
    def click_directory_search_button(self):
        self.directory_search_button.click()
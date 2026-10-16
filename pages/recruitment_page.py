import re
from playwright.sync_api import expect

class RecruitmentPage:

    def __init__(self, page):
        self.page = page
        self.recruitment_menu = page.locator(".oxd-main-menu").get_by_role("link", name="Recruitment")

        ########################################################################################################################################
        # Candidates section/page
        #
        self.candidates_section_header = page.locator("//h5[@class='oxd-text oxd-text--h5 oxd-table-filter-title'][contains(.,'Candidates')]")
        self.candidates_job_title_dropdown =  page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").first
        self.candidates_software_engineer_option = page.get_by_role("listbox").get_by_text("Software Engineer", exact=True)
        self.candidates_search_button = page.get_by_role("button", name="Search")
        self.candidates_vacancy_dropdown = page.get_by_text("-- Select --").nth(1)
        self.candidates_software_engineer_vacancy_option = page.get_by_role("option", name="Software Engineer")
        self.candidates_hiring_manager_dropdown = page.get_by_text("-- Select --").nth(2)
        self.candidates_hiring_manager_dropdown_first_option = page.get_by_role("option").first
        self.candidates_status_dropdown = page.get_by_text("-- Select --").nth(3)
        self.candidates_status_dropdown_application_initiated_option = page.get_by_role("listbox").get_by_text("Application Initiated")
        self.candidates_keywords_textbox = page.get_by_role("textbox", name="Enter comma seperated words...")
        self.candidates_reset_button = page.get_by_role("button", name="Reset")

    
        ########################################################################################################################################
        # Vacancies section/page
        #
        self.vacancies_submenu = page.get_by_role("link", name="Vacancies")
        self.vacancies_job_title_dropdown_account_assistant_option = page.get_by_role("listbox").get_by_text("Account Assistant")
        self.vacancies_add_button = page.locator("//button[@type='button'][contains(.,'Add')]")
        self.vacancies_header = page.locator("//h6[text()='Add Vacancy']")
        self.vacancies_vacancy_name = page.get_by_role("textbox").nth(1)
        self.vacancies_job_title_dropdown = page.locator("//i[contains(@class,'oxd-icon bi-caret-down-fill oxd-select-text--arrow')]")
        self.vacancies_job_title_software_engineer_option = page.get_by_role("option", name="Software Engineer")
        self.vacancies_vacancy_description = page.get_by_role("textbox", name="Type description here")
        self.vacancies_hiring_manager_field = page.get_by_role("textbox", name="Type for hints...")
        self.vacancies_hiring_manager_charles_carter_option = page.get_by_text("Charles Carter")
        self.vacancies_save_button = page.get_by_role("button", name="Save")
        self.vacancies_edit_vacancy_title = page.locator("//h6[contains(.,'Edit Vacancy')]")
        self.vacancies_vacancy_record_found = page.get_by_text("(1) Record Found")
        self.vacancies_job_title_dropdown = page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").first
        self.vacancies_software_engineer_job_title_option = page.get_by_role("option", name="Software Engineer")
        self.vacancies_hiring_manager_dropdown_menu =  page.locator("div:nth-child(3) > .oxd-input-group > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon")
        self.vacancies_hiring_manager_charles_carter_option = page.get_by_role("listbox").get_by_text("Charles Carter")
        self.vacancies_search_button = page.get_by_role("button", name="Search")
        self.vacancies_search_result = page.locator(".oxd-icon.bi-check").first
        self.vacancies_delete_vacancy_button = page.locator("//button[@type='button'][contains(.,'Delete Selected')]")
        self.vacancies_confirm_delete_button = page.locator("//button[@type='button'][contains(.,'Yes, Delete')]")
        self.vacancies_delete_successful_message = page.get_by_text("Successfully Deleted")

    def click_recruitment_menu(self):
        self.recruitment_menu.click()

    ########################################################################################################################################
    # Candidates section/page methods
    #
    def click_candidates_job_title_dropdown(self):
        self.candidates_job_title_dropdown.click()

    def click_candidates_software_engineer_option(self):
        self.candidates_software_engineer_option.click()

    def click_candidates_search_button(self):
        self.candidates_search_button.click()

    def click_candidates_reset_button(self):
        self.candidates_reset_button.click()

    def click_candidates_vacancy_dropdown(self):
        self.candidates_vacancy_dropdown.click()

    def click_candidates_software_engineer_vacancy_option(self):
        self.candidates_software_engineer_vacancy_option.click()

    def click_candidates_hiring_manager_dropdown(self):
        self.candidates_hiring_manager_dropdown.click()

    def click_candidates_hiring_manager_dropdown_first_option(self):
        self.candidates_hiring_manager_dropdown_first_option.click()

    def click_candidates_status_dropdown(self):
        self.candidates_status_dropdown.click()

    def click_candidates_status_dropdown_application_initiated_option(self):
        self.candidates_status_dropdown_application_initiated_option.click()

    def click_candidates_keywords_textbox(self):
        self.candidates_keywords_textbox.click()

    def enter_candidates_keywords(self, keywords): 
        self.candidates_keywords_textbox.fill(keywords)

    ########################################################################################################################################
    # Vacancies section/page methods
    #

    def click_vacancies_submenu(self):
        self.vacancies_submenu.click()

    def click_vacancies_job_title_dropdown_account_assistant_option(self):
        self.vacancies_job_title_dropdown_account_assistant_option.click()

    def click_vacancies_add_button(self):
        self.vacancies_add_button.click()
    
    def click_vacancies_vacancy_name_field(self):
        self.vacancies_vacancy_name.click()

    def enter_vacancies_vacancy_name(self, vacancy_name):
        self.vacancies_vacancy_name.fill(vacancy_name)

    def click_vacancies_job_title_dropdown(self):
        self.vacancies_job_title_dropdown.click()

    def select_vacancies_job_title_software_engineer_option(self):
        self.vacancies_job_title_software_engineer_option.click()

    def click_vacancies_vacancy_description_field(self):
        self.vacancies_vacancy_description.click()

    def enter_vacancies_vacancy_description(self, description):
        self.vacancies_vacancy_description.fill(description)

    def click_vacancies_hiring_manager_field(self):
        self.vacancies_hiring_manager_field.click()

    def enter_vacancies_hiring_manager(self, initial_character):
        self.vacancies_hiring_manager_field.fill(initial_character)
        self.vacancies_hiring_manager_charles_carter_option.click()

    def click_vacancies_save_button(self):
        self.vacancies_save_button.click()

    def click_vacancies_job_title_dropdown(self):
        self.vacancies_job_title_dropdown.click()

    def select_vacancies_software_engineer_job_title_option(self):
        self.vacancies_software_engineer_job_title_option.click()

    def click_vacancies_hiring_manager_dropdown_menu(self):
        self.vacancies_hiring_manager_dropdown_menu.click()

    def select_vacancies_hiring_manager_charles_carter_option(self):
        self.vacancies_hiring_manager_charles_carter_option.click()

    def click_vacancies_search_button(self):
        self.vacancies_search_button.click()

    def click_vacancies_search_result(self):
        self.vacancies_search_result.click()

    def click_vacancies_delete_vacancy_button(self):
        self.vacancies_delete_vacancy_button.click()

    def click_vacancies_confirm_delete_button(self):
        self.vacancies_confirm_delete_button.click()
    
import re
from playwright.sync_api import expect
import time

class RecruitmentPage:

    def __init__(self, page):
        self.page = page
        self.recruitment_menu = page.locator(".oxd-main-menu").get_by_role("link", name="Recruitment")
        self.candidates_tab = page.locator("//a[contains(.,'Candidates')]")
        self.vacancies_tab = page.locator("//a[contains(.,'Vacancies')]")

        ########################################################################################################################################
        # Candidates section/page
        #
        self.candidates_submenu = page.get_by_role("link", name="Candidates")
        self.candidates_candidates_header = page.locator("xpath=//h5[contains(.,'Candidates')]")

        # Add Candidates
        self.candidates_add_button = page.locator("xpath=//button[@type='button'][contains(.,'Add')]")
        self.candidates_add_candidate_header = page.locator("xpath=//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title'][contains(.,'Add Candidate')]")
        self.candidates_add_candidate_first_name_field = page.locator("//input[@name='firstName']")
        self.candidates_add_candidate_last_name_field = page.locator("//input[@name='lastName']")
        self.candidates_add_candidate_vacancy_dropdown = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div[2]/i")
        self.candidates_add_candidate_select_principle_qa_test_option = page.locator("//span[contains(.,'Principle QA Test')]")
        self.candidates_add_candidate_email_address_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input")
        self.candidates_add_candidate_save_button = page.locator("//button[contains(.,'Save')]")
        self.candidates_add_candidate_new_record_saved = page.locator("//p[contains(.,'Successfully Saved')]")

        # Delete Candidates
        self.candidates_delete_candidate_delete_all_checkbox = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span/i")
        self.candidates_delete_candidate_delete_selected_button = page.locator("xpath=//button[@type='button'][contains(.,'Delete Selected')]")
        self.candidates_delete_candidate_confirm_delete_button = page.locator("xpath=//button[@type='button'][contains(.,'Yes, Delete')]")
        self.candidates_delete_candidate_successfully_deleted_message = page.locator("xpath=//p[contains(.,'Successfully Deleted')]")

        # Search Candidates
        self.candidates_search_candidate_job_title_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]")
        self.candidates_search_candidate_job_title_software_engineer_option = page.locator("xpath=//div[@role='option'][contains(.,'Software Engineer')]")
        self.candidates_search_candidate_vacancy_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[2]")
        self.candidates_search_candidate_principle_qa_test_option = page.locator("xpath=//span[contains(.,'Principle QA Test')]")
        self.candidates_search_candidate_hiring_manager_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[3]")
        self.candidates_search_candidate_charles_carter_option = page.locator("xpath=//div[@role='option'][contains(.,'Charles Carter')]")
        self.candidates_search_candidate_status_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[4]")
        self.candidates_search_candidate_status_application_initiated_option = page.locator("xpath=//span[contains(.,'Application Initiated')]")
        self.candidates_search_candidate_candidate_name_field = page.locator("xpath=//input[contains(@placeholder,'Type for hints...')]")
        self.candidates_search_candidate_candidate_name_field_value = page.locator("xpath=//span[contains(.,'Mike  Jones')]")
        self.candidates_search_candidate_keywords_field = page.locator("xpath=//input[contains(@placeholder,'Enter comma seperated words...')]")

        self.candidates_search_candidate_search_button = page.locator("xpath=//button[contains(.,'Search')]")
        self.candidates_search_candidate_record_found_header = page.locator("xpath=//span[contains(.,'(1) Record Found')]")
        self.candidates_search_candidate_no_record_found_header = page.locator("xpath=//span[@class='oxd-text oxd-text--span'][contains(.,'No Records Found')]")

        ########################################################################################################################################
        # Vacancies section/page
        #
        self.vacancies_submenu = page.get_by_role("link", name="Vacancies")
        self.vacancies_vacancies_header = page.locator("xpath=//h5[contains(.,'Vacancies')]")

        # Add Vacancy
        self.vacancies_add_button = page.locator("xpath=//button[@type='button'][contains(.,'Add')]")
        self.vacancies_add_vacancy_header = page.locator("xpath=//h6[text()='Add Vacancy']")
        self.vacancies_add_vacancy_name_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input")
        self.vacancies_add_vacancy_job_title_dropdown = page.locator("xpath=//div[@class='oxd-select-text-input'][contains(.,'-- Select --')]")
        self.vacancies_add_vacancy_job_title_software_engineer_option = page.locator("xpath=//span[contains(.,'Software Engineer')]")
        self.vacancies_add_vacancy_description_field = page.locator("xpath=//textarea[@placeholder='Type description here']")
        self.vacancies_add_vacancy_hiring_manager_field = page.get_by_role("textbox", name="Type for hints...")
        self.vacancies_add_vacancy_hiring_manager_charles_carter_option = page.get_by_text("Charles Carter")
        self.vacancies_add_vacancy_save_button = page.locator("xpath=//button[@type='submit'][contains(.,'Save')]")
        
        # Edit Vacancy
        self.vacancies_edit_vacancy_edit_vacancy_title = page.locator("//h6[contains(.,'Edit Vacancy')]")

        # Delete Vacancy
        self.vacancies_delete_vacancy_delete_all_checkbox = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span/i")
        self.vacancies_delete_vacancy_delete_selected_button = page.locator("xpath=//button[@type='button'][contains(.,'Delete Selected')]")
        self.vacancies_delete_vacancy_confirm_delete_button = page.locator("xpath=//button[@type='button'][contains(.,'Yes, Delete')]")
        self.vacancies_delete_vacancy_successfully_deleted_message = page.locator("xpath=//p[contains(.,'Successfully Deleted')]")

        # Search Vacancy
        self.vacancies_search_vacancy_job_title_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]")
        self.vacancies_search_vacancy_job_title_software_engineer_option = page.locator("xpath=//div[@role='option'][contains(.,'Software Engineer')]")
        self.vacancies_search_vacancy_vacancy_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[2]")
        self.vacancies_search_vacancy_job_title_principle_qa_test_option = page.locator("xpath=//span[contains(.,'Principle QA Test')]")
        self.vacancies_search_vacancy_hiring_manager_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[3]")
        self.vacancies_search_vacancy_charles_carter_option = page.locator("xpath=//span[contains(.,'Charles Carter')]")


        self.vacancies_search_vacancy_search_button = page.locator("xpath=//button[contains(.,'Search')]")
        self.vacancies_search_vacancy_record_found_header = page.locator("xpath=//span[contains(.,'(1) Record Found')]")
    ########################################################################################################################################
    # Recruitment section/page methods
    #

    def click_recruitment_menu(self):
        self.recruitment_menu.click()

    def click_candidates_tab(self):
        self.candidates_tab.click()

    def click_vacancies_tab(self):
        self.vacancies_tab.click()

    ########################################################################################################################################
    # Candidates section/page methods
    #

    def click_candidates_submenu(self):
        self.candidates_submenu.click()

    #
    # Add Candidate methods
    #
    
    def click_candidates_add_button(self):
        self.candidates_add_button.click()

    def click_candidates_add_candidate_first_name_field(self):
        self.candidates_add_candidate_first_name_field.click()
    
    def enter_candidates_add_candidate_first_name_field(self, first_name):
        self.candidates_add_candidate_first_name_field.fill(first_name)
    
    def click_candidates_add_candidate_last_name_field(self):
        self.candidates_add_candidate_last_name_field.click()
        
    def enter_candidates_add_candidate_last_name_field(self, last_name):
        self.candidates_add_candidate_last_name_field.fill(last_name)
    
    def click_candidates_add_candidate_vacancy_dropdown(self):
        self.candidates_add_candidate_vacancy_dropdown.click()
    
    def select_candidates_add_candidate_select_principle_qa_test_option(self):
        self.candidates_add_candidate_select_principle_qa_test_option.click()
    
    def click_candidates_add_candidate_email_address_field(self):
        self.candidates_add_candidate_email_address_field.click()
    
    def enter_candidates_add_candidate_email_address_field(self, email_address):
        self.candidates_add_candidate_email_address_field.fill(email_address)
    
    def click_candidates_add_candidate_save_button(self):
        self.candidates_add_candidate_save_button.click()

    #
    # Search Candidate methods
    #

    def click_candidates_search_candidate_vacancy_dropdown(self):
        self.candidates_search_candidate_vacancy_dropdown.click()

    def select_candidates_search_vacancy_vacancy_dropdown_option(self,vacancy):
        if vacancy == "Principle QA Test":
            self.candidates_search_candidate_principle_qa_test_option.click()

    def click_candidates_search_vacancy_hiring_manager_dropdown(self):
        self.candidates_search_candidate_hiring_manager_dropdown.click()
    
    def select_candidates_search_vacancy_hiring_manager_dropdown_option(self,hiring_manager):
        if hiring_manager == "Charles Carter":
            self.candidates_search_candidate_charles_carter_option.click()

    def click_candidates_search_candidate_status_dropdown(self):
        self.candidates_search_candidate_status_dropdown.click()

    def select_candidates_search_candidate_status_application_initiated_option(self, status):
        if status == "Application Initiated":
            self.candidates_search_candidate_status_application_initiated_option.click()

    def click_candidates_search_candidate_candidate_name_field(self):
        self.candidates_search_candidate_candidate_name_field.click()

    def enter_candidates_search_candidate_candidate_name_field_value(self, candidate_name):
        if candidate_name == "Mike Jones":
            candidate_search_criteria = "Mike"
            self.candidates_search_candidate_candidate_name_field.fill(candidate_search_criteria)
            time.sleep(1)
            self.candidates_search_candidate_candidate_name_field_value.click()

    def click_candidates_search_candidate_keywords_field(self):
        self.candidates_search_candidate_keywords_field.click()

    def enter_candidates_search_candidate_keywords_field_value(self,keywords):
        self.candidates_search_candidate_keywords_field.fill(keywords)

    def click_candidates_search_candidate_search_button(self):
        self.candidates_search_candidate_search_button.click()

    #
    # Delete Candidate methods
    #

    def click_candidates_delete_candidate_delete_all_checkbox(self):
        self.candidates_delete_candidate_delete_all_checkbox.click()

    def click_candidates_delete_candidate_delete_selected_button(self):
        self.candidates_delete_candidate_delete_selected_button.click(timeout=5000)

    def click_candidates_delete_candidate_confirm_delete_button(self):
        self.candidates_delete_candidate_confirm_delete_button.click()

    ########################################################################################################################################
    # Vacancies section/page methods
    #

    def click_vacancies_submenu(self):
        self.vacancies_submenu.click()

    #
    # Add Vacancies methods
    #

    def click_vacancies_add_button(self):
        self.vacancies_add_button.click()

    def click_vacancies_add_vacancy_name_field(self):
        self.vacancies_add_vacancy_name_field.click()

    def enter_vacancies_add_vacancy_name_field_value(self, vacancy_name):
        self.vacancies_add_vacancy_name_field.fill(vacancy_name)

    def click_vacancies_add_vacancy_job_title_dropdown(self):
        self.vacancies_add_vacancy_job_title_dropdown.click()

    def select_vacancies_add_vacancy_job_title_dropdown_option(self, job_title):
        self.vacancies_add_vacancy_job_title_software_engineer_option.click()

    def click_vacancies_add_vacancy_description_field(self):
        self.vacancies_add_vacancy_description_field.click()

    def enter_vacancies_add_vacancy_description_field_value(self, vacancy_description):
        self.vacancies_add_vacancy_description_field.fill(vacancy_description)

    def click_vacancies_add_vacancy_hiring_manager_field(self):
        self.vacancies_add_vacancy_hiring_manager_field.click()

    def enter_vacancies_hiring_manager(self, initial_character):
        self.vacancies_add_vacancy_hiring_manager_field.fill(initial_character)
        self.vacancies_add_vacancy_hiring_manager_charles_carter_option.click()

    def click_vacancies_add_vacancy_save_button(self):
        self.vacancies_add_vacancy_save_button.click()

    #
    # Search Vacancies methods
    #
    def click_vacancies_search_vacancy_job_title_dropdown(self):
        self.vacancies_search_vacancy_job_title_dropdown.click()

    def select_vacancies_search_vacancy_job_title_dropdown_option(self,job_title):
        if job_title == "Software Engineer":
            self.vacancies_search_vacancy_job_title_software_engineer_option.click()

    def click_vacancies_search_vacancy_vacancy_dropdown(self):
        self.vacancies_search_vacancy_vacancy_dropdown.click()

    def select_vacancies_search_vacancy_job_title_principle_qa_test_dropdown_option(self, vacancy_name):
        if vacancy_name == "Principle QA Test":
             self.vacancies_search_vacancy_job_title_principle_qa_test_option.click()

    def click_vacancies_search_vacancy_hiring_manager_dropdown(self):
        self.vacancies_search_vacancy_hiring_manager_dropdown.click()

    def select_vacancies_search_vacancy_charles_carter_dropdown_option(self,hiring_manager):
        if hiring_manager == "Charles Carter":
            self.vacancies_search_vacancy_charles_carter_option.click()

    def click_vacancies_search_vacancy_search_button(self):
        self.vacancies_search_vacancy_search_button.click()


    #
    # Delete Vacancies methods
    #

    def click_vacancies_delete_vacancy_delete_all_checkbox(self):
        self.vacancies_delete_vacancy_delete_all_checkbox.click()

    def click_vacancies_delete_vacancy_delete_selected_button(self):
        self.vacancies_delete_vacancy_delete_selected_button.click(timeout=5000)

    def click_vacancies_delete_vacancy_confirm_delete_button(self):
        self.vacancies_delete_vacancy_confirm_delete_button.click()

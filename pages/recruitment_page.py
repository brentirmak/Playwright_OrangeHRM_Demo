import re


class RecruitmentPage:

    def __init__(self, page):
        self.page = page

        #
        # Candidates
        #
        self.recruitment_menu = page.get_by_role("link", name="Recruitment")
        self.job_title_dropdown = page.get_by_text("-- Select --").first
        self.software_engineer_option = page.get_by_role("listbox").get_by_text("Software Engineer", exact=True)
        self.search_button = page.get_by_role("button", name="Search")
        self.reset_button = page.get_by_role("button", name="Reset")
        self.vacancy_dropdown = page.get_by_text("-- Select --").nth(1)
        self.software_engineer_vacancy_option = page.get_by_role("option", name="Software Engineer")
        self.hiring_manager_dropdown = page.get_by_text("-- Select --").nth(2)
        self.hiring_manager_dropdown_first_option = page.get_by_role("option").first
        self.status_dropdown = page.get_by_text("-- Select --").nth(3)
        self.status_dropdown_application_initiated_option = page.get_by_role("listbox").get_by_text("Application Initiated")
        self.keywords_textbox = page.get_by_role("textbox", name="Enter comma seperated words...")

        #
        # Vacancies
        #
        self.vacancies_submenu = page.get_by_role("link", name="Vacancies")
        self.job_title_dropdown_account_assistant_option = page.get_by_role("listbox").get_by_text("Account Assistant")

    def click_recruitment_menu(self):
        self.recruitment_menu.click()

    def click_job_title_dropdown(self):
        self.job_title_dropdown.click()

    def click_software_engineer_option(self):
        self.software_engineer_option.click()

    def click_search_button(self):
        self.search_button.click()

    def click_reset_button(self):
        self.reset_button.click()

    def click_vacancy_dropdown(self):
        self.vacancy_dropdown.click()

    def click_software_engineer_vacancy_option(self):
        self.software_engineer_vacancy_option.click()

    def click_hiring_manager_dropdown(self):
        self.hiring_manager_dropdown.click()

    def click_hiring_manager_dropdown_first_option(self):
        self.hiring_manager_dropdown_first_option.click()

    def click_status_dropdown(self):
        self.status_dropdown.click()

    def click_status_dropdown_application_initiated_option(self):
        self.status_dropdown_application_initiated_option.click()

    def click_keywords_textbox(self):
        self.keywords_textbox.click()

    def enter_keywords(self, keywords): 
        self.keywords_textbox.fill(keywords)
    
    def click_vacancies_submenu(self):
        self.vacancies_submenu.click()

    def click_job_title_dropdown_account_assistant_option(self):
        self.job_title_dropdown_account_assistant_option.click()
    
    
    
import re


class RecruitmentPage:

    def __init__(self, page):
        self.page = page
        self.recruitment_menu = page.get_by_role("link", name="Recruitment")
        self.job_title_dropdown = page.get_by_text("-- Select --").first
        self.software_engineer_option = page.get_by_role("listbox").get_by_text("Software Engineer", exact=True)
        self.search_button = page.get_by_role("button", name="Search")
        self.reset_button = page.get_by_role("button", name="Reset")
        self.vacancy_dropdown = page.get_by_text("-- Select --").nth(1)
        #self.software_engineer_vacancy_option = page.locator("div").filter(has_text=re.compile(r"^Software Engineer$")).nth(2)
        # page.get_by_role("option", name="Software Engineer")
        self.software_engineer_vacancy_option = page.get_by_role("option", name="Software Engineer")

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
    
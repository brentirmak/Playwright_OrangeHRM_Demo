class RecruitmentPage:

    def __init__(self, page):
        self.page = page
        self.recruitment_menu = page.get_by_role("link", name="Recruitment")
        self.job_title_dropdown = page.get_by_text("-- Select --").first
        self.software_engineer_option = page.get_by_role("listbox").get_by_text("Software Engineer", exact=True)
        self.search_button = page.get_by_role("button", name="Search")

    def click_recruitment_menu(self):
        self.recruitment_menu.click()

    def click_job_title_dropdown(self):
        self.job_title_dropdown.click()

    def click_software_engineer_option(self):
        self.software_engineer_option.click()

    def click_search_button(self):
        self.search_button.click()
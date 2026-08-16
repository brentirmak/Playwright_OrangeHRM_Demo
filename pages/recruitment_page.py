class RecruitmentPage:

    def __init__(self, page):
        self.page = page
        self.recruitment_menu = page.get_by_role("link", name="Recruitment")

    def click_recruitment_menu(self):
        self.recruitment_menu.click()
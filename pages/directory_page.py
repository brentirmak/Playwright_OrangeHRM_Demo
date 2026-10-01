class DirectoryPage:

    def __init__(self, page):
        self.page = page
        self.directory_menu = page.get_by_role("link", name="Directory")
        self.search_button = page.locator("//button[@type='submit'][contains(.,'Search')]")
        self.reset_button = page.locator("//button[contains(.,'Reset')]")
        self.employee_name_field = page.locator("//input[@placeholder='Type for hints...']")
        self.job_title_dropdown = page.locator("(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]")
        self.location_dropdown = page.locator("(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[2]")
        self.software_engineer_selection = page.locator("div[role='option']", has_text="Software Engineer")
        self.chief_financial_officer_selection = page.locator("div[role='option']", has_text="Chief Financial Officer")


    def click_directory_menu(self):
        self.directory_menu.click()

    def click_job_title_dropdown(self):
        self.job_title_dropdown.click()

    def click_software_engineer_selection(self):
        self.software_engineer_selection.click()

    def click_chief_financial_officer_selection(self):
        self.chief_financial_officer_selection.click()
        
    def click_search_button(self):
        self.search_button.click()
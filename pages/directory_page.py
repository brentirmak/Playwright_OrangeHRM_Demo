class DirectoryPage:

    def __init__(self, page):
        self.page = page
        self.directory_menu = page.get_by_role("link", name="Directory")
        self.search_button = page.locator("//button[@type='submit'][contains(.,'Search')]")
        self.reset_button = page.locator("//button[contains(.,'Reset')]")
        self.employee_name_field = page.locator("//input[@placeholder='Type for hints...']")
        self.job_title_dropdown = page.locator("(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]")
        self.location_dropdown = page.locator("(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[2]")



    def click_directory_menu(self):
        self.directory_menu.click()
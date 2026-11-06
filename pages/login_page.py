class LoginPage:

    def __init__(self, page):
        self.page = page
        self.dashboard_page_header = page.locator("xpath=//h6[contains(.,'Dashboard')]")

    def login(self, username, password):
        self.page.locator("//input[@name='username']").fill(username)
        self.page.locator("//input[@name='password']").fill(password)
        self.page.locator("//button[@type='submit']").click()
        self.page.wait_for_load_state("networkidle")

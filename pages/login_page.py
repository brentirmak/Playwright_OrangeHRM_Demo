class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):

        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

        self.page.locator("input[name='username']").fill(username)
        self.page.locator("input[name='password']").fill(password)
        self.page.locator("button[type='submit']").click()

        self.page.wait_for_url("**/dashboard/index")
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        #self.username = page.get_by_role("textbox", name="Username")
        self.username = page.locator("//input[@name='username']")    

        #self.password = page.get_by_role("textbox", name="Password")
        self.password = page.locator("//input[@name='password']")   

        #self.login_button = page.get_by_role("button", name="Login")
        self.login_button = page.locator("//button[@type='submit']") 

    def enter_username(self, username):
        self.username.fill(username)
        #self.nonEnglish_username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)
        #self.nonEnglish_password.fill(password)

    def click_login(self):
        self.login_button.click()
        #self.login_button.click()
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()      
    

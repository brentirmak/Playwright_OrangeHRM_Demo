class BuzzPage:

    def __init__(self, page):
        self.page = page
        self.buzz_menu = page.get_by_role("link", name="Buzz")

        ########################################################################################################################################
        # Buzz section/page
        #
        self.buzz_header = page.locator("xpath=//h6[contains(.,'Buzz')]")
        self.buzz_newsfeed_header = page.locator("xpath=//p[contains(.,'Buzz Newsfeed')]")
        self.buzz_most_recent_posts_button = page.locator("xpath=//button[@type='button'][contains(.,'Most Recent Posts')]")
        self.buzz_most_liked_posts_button = page.locator("xpath=//button[@type='button'][contains(.,'Most Liked Posts')]")
        self.buzz_most_commented_posts_button = page.locator("xpath=//button[@type='button'][contains(.,'Most Commented Posts')]")
        self.buzz_post_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/form/div/textarea")
        self.buzz_post_button = page.locator("xpath=//button[@type='submit'][contains(.,'Post')]")
        self.buzz_no_posts_available_header = page.locator("xpath=//p[contains(.,'No Posts Available')]")


    def click_buzz_menu(self):
        self.buzz_menu.click()

    ########################################################################################################################################
    # Buzz section/page methods
    #
    def click_buzz_most_recent_posts_button(self):
        self.buzz_most_recent_posts_button.click()

    def click_buzz_most_liked_posts_button(self):
        self.buzz_most_liked_posts_button.click()

    def click_buzz_most_commented_posts_button(self):
        self.buzz_most_commented_posts_button.click()

    def click_buzz_post_field(self):
        self.buzz_post_field.click()

    def enter_buzz_post_field_value(self,post_message):
        self.buzz_post_field.fill(post_message)

    def click_buzz_post_button(self):
        self.buzz_post_button.click()

    
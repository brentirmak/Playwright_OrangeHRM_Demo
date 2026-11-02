import re
from playwright.sync_api import Page, expect

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
        self.buzz_no_posts_available_header = page.locator("xpath=//p[contains(.,'No Posts Available')]")

        #
        # Add Post
        #
        self.buzz_post_field = page.locator("xpath=//textarea[@class='oxd-buzz-post-input']")
        self.buzz_post_button = page.locator("xpath=//button[@type='submit'][contains(.,'Post')]")
        self.buzz_post_successfully_saved_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")

        #
        # Delete Post
        #
        self.buzz_post_successfully_deleted_message = page.locator("xpath=//p[contains(.,'Successfully Deleted')]")

    def click_buzz_menu(self):
        self.buzz_menu.click()

    ########################################################################################################################################
    # Buzz section/page methods
    #

    # Add methods
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

    # Delete methods
    def delete_buzz_post(self, keyword):
        # Each post on the feed is a card with the class orangehrm-buzz
        post = (
            self.page.locator("div.orangehrm-buzz")
            .filter(has_text=re.compile(keyword, re.IGNORECASE))
            .first
        )
        expect(post).to_be_visible()
        print("Post is visible - will click on the 3 dots")

        post.locator(".orangehrm-buzz-post-header-config").click()
        print("Clicked on the 3 dots - will click on Delete Post")

        # Scope to the post so you don't hit another card's menu
        delete_item = post.get_by_text("Delete Post", exact=True)
        expect(delete_item).to_be_visible()
        delete_item.click()
        print("Clicked on Delete post - will click on Yes in the confirmation window")

        self.page.get_by_role("button", name="Yes, Delete").click()
        print("Clicked on Yes, Delete - will confirm the deletion was successful")
        expect(self.page.get_by_text("Successfully Deleted")).to_be_visible()
        print("Deletion was successful message was displayed")


    def delete_all_buzz_posts(self, max_posts=100):
        # Only posts that have the three-dots menu (i.e. ones the logged-in user owns)
        own_posts = self.page.locator("div.orangehrm-buzz").filter(
            has=self.page.locator(".orangehrm-buzz-post-header-config")
        )

        deleted = 0
        while deleted < max_posts:
            # Let the feed finish rendering / re-rendering
            self.page.wait_for_load_state("networkidle")

            if own_posts.count() == 0:
                # The feed loads more on scroll; try once before concluding we're done
                self.page.mouse.wheel(0, 3000)
                self.page.wait_for_timeout(1000)
                if own_posts.count() == 0:
                    break

            # Re-evaluated every loop, so it always targets the current top post
            post = own_posts.first
            expect(post).to_be_visible()
            print("Post is visible - will click on the 3 dots")

            post.locator(".orangehrm-buzz-post-header-config").click()
            print("Clicked on the 3 dots - will click on Delete Post")

            delete_item = post.get_by_text("Delete Post", exact=True)
            expect(delete_item).to_be_visible()
            delete_item.click()
            print("Clicked on Delete post - will click on Yes in the confirmation window")

            self.page.get_by_role("button", name="Yes, Delete").click()
            print("Clicked on Yes, Delete - will confirm the deletion was successful")

            toast = self.page.get_by_text("Successfully Deleted")
            expect(toast).to_be_visible()
            # Wait for the toast to disappear so the next iteration
            # can't pass on the previous delete's toast
            expect(toast).to_be_hidden()

            deleted += 1
            print(f"Deleted post #{deleted}")

        print(f"Cleanup finished - {deleted} post(s) deleted")




    
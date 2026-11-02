from datetime import datetime, timedelta
from playwright.sync_api import Page, expect
from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.buzz_page import BuzzPage
from pages.logout_page import LogoutPage
import time

def test_HomePage(shared_page):
    print("\nStarting test_HomePage transaction")
    print("Will go to home page")
    shared_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("Loaded home page")
    home_page = HomePage(shared_page)
    home_page.verify_branding_image_visible()
    print("Verified branding image is visible on the home page")
    print("Ended test_HomePage transaction")

def test_LoginPage(shared_page):
    print("\nStarting test_LoginPage transaction")
    login_page = LoginPage(shared_page)
    print("Enter username and password and click Login button")
    login_page.login("Admin", "admin123")
    print("Clicked Login button")
    shared_page.wait_for_url("**/dashboard/index", timeout=15000)
    shared_page.wait_for_selector("//p[@class='oxd-text oxd-text--p'][contains(.,'Time at Work')]")
    print("Verified Dashboard heading is visible on the dashboard page")
    print("Ended test_LoginPage transaction")

def test_BuzzPageAccessMostRecentPosts(shared_page):
    print("\nStarting test_BuzzPageAccessMostRecentPosts transaction")
    buzz_page = BuzzPage(shared_page)
    print("Will access the Buzz page")
    buzz_page.click_buzz_menu()
    print("Clicked on the Buzz menu - will verify that we're on the Buzz Newsfeed page")
    expect(buzz_page.buzz_newsfeed_header).to_be_visible(timeout=20000)
    print("Verified that we're on the Buzz Newsfeed page - will click on the Most Recent Posts button")
    buzz_page.click_buzz_most_recent_posts_button()
    print("Clicked on the Most Recent Posts button - will verify that No Posts Available is displayed")
    expect(buzz_page.buzz_no_posts_available_header).to_be_visible(timeout=20000)
    print("Verified that the No Posts Available message is displayed")
    print("\nEnded test_BuzzPageAccessMostRecentPosts transaction")

def test_BuzzPageAccessMostLikedPosts(shared_page):
    print("\nStarting test_BuzzPageAccessMostLikedPosts transaction")
    buzz_page = BuzzPage(shared_page)
    print("Will access the Buzz page")
    buzz_page.click_buzz_menu()
    print("Clicked on the Buzz menu - will verify that we're on the Buzz Newsfeed page")
    expect(buzz_page.buzz_newsfeed_header).to_be_visible(timeout=20000)
    print("Verified that we're on the Buzz Newsfeed page - will click on the Most Liked Posts button")
    buzz_page.click_buzz_most_liked_posts_button()
    print("Verified that the No Posts Available message is displayed - will verify that No Posts Available is displayed")
    expect(buzz_page.buzz_no_posts_available_header).to_be_visible(timeout=20000)
    print("Verified that the No Posts Available message is displayed")
    print("\nEnded test_BuzzPageAccessMostLikedPosts transaction")

def test_BuzzPageAccessMostCommentedPosts(shared_page):
    print("\nStarting test_BuzzPageAccessMostCommentedPosts transaction")
    buzz_page = BuzzPage(shared_page)
    print("Will access the Buzz page")
    buzz_page.click_buzz_menu()
    print("Clicked on the Buzz menu - will verify that we're on the Buzz Newsfeed page")
    expect(buzz_page.buzz_newsfeed_header).to_be_visible(timeout=20000)
    print("Verified that we're on the Buzz Newsfeed page - will click on the Most Commented Posts button")
    buzz_page.click_buzz_most_commented_posts_button()
    expect(buzz_page.buzz_no_posts_available_header).to_be_visible(timeout=20000)
    print("Verified that the No Posts Available message is displayed")
    print("\nEnded test_BuzzPageAccessMostCommentedPosts transaction")

'''
Create Post
'''
def test_BuzzPageAddPost(shared_page):
    print("\nStarting test_BuzzPageAddPost transaction")
    buzz_page = BuzzPage(shared_page)
    print("Will access the Buzz page")
    buzz_page.click_buzz_menu()
    print("Clicked on the Buzz menu - will verify that we're on the Buzz Newsfeed page")
    expect(buzz_page.buzz_newsfeed_header).to_be_visible(timeout=20000)
    print("Verified that we're on the Buzz Newsfeed page - will click on the Buzz field")
    buzz_page.click_buzz_post_field()
    buzz_page.enter_buzz_post_field_value("This is a test buzz post")
    print("Entered a buzz post - will now click on a Post button")
    buzz_page.click_buzz_post_button()
    print("Clicked on the Post button - will verify that the post was successfully saved")
    expect(buzz_page.buzz_post_successfully_saved_message).to_be_visible(timeout=20000)
    print("Verified that the post was successfully saved")
    print("\nEnded test_BuzzPageAddPost transaction")


def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")
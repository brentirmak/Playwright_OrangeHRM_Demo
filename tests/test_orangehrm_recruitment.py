import re
from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from pages.logout_page import LogoutPage

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
    expect(shared_page.get_by_role("heading", name="Dashboard")).to_be_visible()
    shared_page.wait_for_selector("//h6[contains(.,'Dashboard')]")
    print("Verified Dashboard heading is visible on the dashboard page")
    print("Ended test_LoginPage transaction")

def test_RecruitmentPage(shared_page):
    print("\nStarting test_RecruitmentPage transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on Recruitment menu")
    print("Will click on Job Title dropdown")
    recruitment_page.click_job_title_dropdown()
    print("Clicked on Job Title dropdown")
    print("Will select Software Engineer option from the dropdown")
    recruitment_page.click_software_engineer_option()
    print("Selected Software Engineer option from the dropdown")
    print("Will click on Search button")
    recruitment_page.click_search_button()
    print("Clicked on Search button")
    expect(shared_page.get_by_role("cell", name="Software Engineer").first).to_be_visible()
    print("Verified Software Engineer job title is visible in the search results")
    #expect(shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]"))
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible()
    print("Verified Records Found is visible in the search results")
    print("Ended test_RecruitmentPage transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

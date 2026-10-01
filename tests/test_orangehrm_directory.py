import re
from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.directory_page import DirectoryPage
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
    shared_page.wait_for_url("**/dashboard/index", timeout=15000)
    expect(shared_page.get_by_role("heading", name="Dashboard")).to_be_visible(timeout=10000)
    shared_page.wait_for_selector("//h6[contains(.,'Dashboard')]")
    print("Verified Dashboard heading is visible on the dashboard page")
    print("Ended test_LoginPage transaction")

def test_AccessDirectorySection(shared_page):
    print("\nAccessing the Directory section")
    directory_page = DirectoryPage(shared_page)
    print("Will click on the Directory menu item")
    directory_page.click_directory_menu()
    print("Clicked on the Directory menu item")
    expect(shared_page.locator("//h5[contains(.,'Directory')]")).to_be_visible(timeout=10000)
    print("Verified the Directory heading is visible on the Directory page")
    print("Ended test_AccessDirectorySection transaction")

def test_SearchDirectoryByJobTitle(shared_page):
    print("\nWill perform a search for Software Engineer")
    directory_page = DirectoryPage(shared_page)
    try:
        print("Clicking on the Job Title dropdown menu")
        directory_page.click_job_title_dropdown()
        print("Clicked on the Job Title dropdown - will select Software Engineer")
        directory_page.click_software_engineer_selection()
        print("Selected the Software Engineer option - will click on the Search button")
        directory_page.click_search_button()
        print("Clicked on the Search button - will verify that atleast 1 Record is found")
        shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
        print("Atleast one record was found")
    except:
        print("2nd try with different job title - Clicking on the Job Title dropdown menu")
        directory_page.click_job_title_dropdown()
        print("2nd try with different job title - Clicked on the Job Title dropdown - will select Chief Financial Officer")
        directory_page.click_chief_financial_officer_selection
        print("2nd try with different job title - Selected the Chief Financial Officer option - will click on the Search button")
        directory_page.click_search_button()
        print("2nd try with different job title - Clicked on the Search button - will verify that atleast 1 Record is found")
        shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
        print("Atleast one record was found")
    print("Ended test_SearchDirectoryByJobTitle transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

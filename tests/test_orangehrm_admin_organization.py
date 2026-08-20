import time

from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.pim_page import PIMPage
from pages.leave_page import LeavePage
from pages.time_page import TimePage
from pages.recruitment_page import RecruitmentPage
from pages.myinfo_page import MyInfoPage
from pages.performance_page import PerformancePage
from pages.directory_page import DirectoryPage
from pages.maintenance_page import MaintenancePage
from pages.claim_page import ClaimPage
from pages.buzz_page import BuzzPage
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

def test_OrganizationGeneralInformation(shared_page):
    print("\nStarting test_OrganizationGeneralInformation transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Admin menu")
    admin_page.click_admin_menu()
    print("Clicked on Admin menu")
    print("Will click on Organization submenu")
    admin_page.click_organization_submenu()
    print("Clicked on Organization submenu")
    admin_page.click_general_information_submenu()
    print("Clicked on General Information submenu")
    expect(shared_page.get_by_role("heading", name="General Information")).to_be_visible()
    print("Verified General Information heading is visible on the General Information page")
    print("Ended test_OrganizationGeneralInformation transaction")

def test_OrganizationLocations(shared_page):
    print("\nStarting test_OrganizationLocations transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Admin menu")
    admin_page.click_admin_menu()
    print("Clicked on Admin menu")
    print("Will click on Organization submenu")
    admin_page.click_organization_submenu()
    print("Clicked on Organization submenu")
    admin_page.click_locations_submenu()
    print("Clicked on Locations submenu")
    expect(shared_page.get_by_role("heading", name="Locations")).to_be_visible()
    print("Verified Locations heading is visible on the Locations page")
    shared_page.get_by_text("-- Select --").click()
    shared_page.get_by_role("listbox").get_by_text("United States", exact=True).click()
    shared_page.get_by_role("button", name="Search").click()
    shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
    print("Verified Records Found text is visible after searching for locations in United States")
    print("Ended test_OrganizationLocations transaction")

def test_OrganizationStructure(shared_page):
    print("\nStarting test_OrganizationStructure transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Admin menu")
    admin_page.click_admin_menu()
    print("Clicked on Admin menu")
    print("Will click on Organization submenu")
    admin_page.click_organization_submenu()
    print("Clicked on Organization submenu")
    admin_page.click_structure_submenu()
    print("Clicked on Structure submenu")
    expect(shared_page.get_by_role("heading", name="Organization Structure")).to_be_visible()
    print("Verified Organization Structure heading is visible on the Organization Structure page")
    print("Ended test_OrganizationStructure transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

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

def test_AccessAdminPage(shared_page):
    print("\nStarting test_AccessAdminPage transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu")
    expect(shared_page.get_by_role("heading", name="System Users")).to_be_visible()
    print("Verified System Users heading is visible on the admin page")
    print("Ended test_AccessAdminPage transaction")

def test_AdminPageUsernameSearch(shared_page):
    print("\nStarting test_AdminPageUsernameSearch transaction")
    admin_page = AdminPage(shared_page)
    print("Will enter username in the search field")
    admin_page.enter_username("Admin")
    print("Entered username in the search field")
    print("Will click on search button")
    admin_page.click_search_button()
    print("Clicked on search button")
    shared_page.wait_for_selector("//span[contains(.,'(1) Record Found')]")
    shared_page.get_by_role("table").get_by_text("Alexa Siri")
    print("Verified that the username 'Admin' is visible in the search results")
    print("Ended test_AdminPageUsernameSearch transaction")

def test_AccessAdminPageJobSubmenu(shared_page):
    print("\nStarting test_AccessAdminPageJobSubmenu transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Job submenu under Admin menu")
    admin_page.click_job_submenu()
    print("Clicked on Job submenu under Admin menu")
    expect(shared_page.get_by_role("menuitem", name="Job Titles")).to_be_visible()
    print("Verified Job Titles heading is visible on the Job submenu page")
    print("Ended test_AccessAdminPageJobSubmenu transaction")

def test_AccessAdminPageJobTitlesSubmenu(shared_page):
    print("\nStarting test_AccessAdminPageJobTitlesSubmenu transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Job Titles submenu under Job submenu")
    admin_page.click_job_titles_submenu()
    print("Clicked on Job Titles submenu under Job submenu")
    expect(shared_page.get_by_role("columnheader", name="Job Description")).to_be_visible()
    print("Verified Job Description column header is visible on the Job Titles submenu page")
    expect(shared_page.get_by_text("Automaton Tester")).to_be_visible()
    print("Verified Automaton Tester job title is visible on the Job Titles submenu page")
    print("Ended test_AccessAdminPageJobTitlesSubmenu transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

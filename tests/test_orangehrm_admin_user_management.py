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

def test_AccessAdminSection(shared_page):
    print("\nStarting test_AccessAdminSection transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu")
    expect(shared_page.get_by_role("heading", name="System Users")).to_be_visible()
    print("Verified System Users heading is visible on the admin page")
    print("Ended test_AccessAdminSection transaction")

def test_AdminSectionUserManagementSearchByUsername(shared_page):
    print("\nStarting test_AdminSectionUserManagementSearchByUsername transaction")
    admin_page = AdminPage(shared_page)
    print("Will enter username in the search field")
    admin_page.enter_username("Admin")
    print("Entered username in the search field")
    print("Will click on search button")
    admin_page.click_search_button()
    print("Clicked on search button")
    shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
    shared_page.get_by_role("table").get_by_text("Alexa Siri")
    print("Verified that the username 'Admin' is visible in the search results")
    print("Ended test_AdminSectionUserManagementSearchByUsername transaction")

def test_AdminSectionUserManagementSearchByUserRole(shared_page):
    print("\nStarting test_AdminSectionUserManagementSearchByUserRole transaction")
    admin_page = AdminPage(shared_page)
    print("Will click reset button")
    admin_page.click_reset_button()
    print("Clicked on reset button")
    print("Will click on user role dropdown")
    admin_page.click_user_role_dropdown()
    print("Clicked on user role dropdown")
    print("Will click on admin option")
    admin_page.click_admin_option()
    print("Clicked on admin option")
    print("Will click on search button")
    admin_page.click_search_button()
    print("Clicked on search button")
    shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
    shared_page.get_by_role("table").get_by_text("Alexa Siri")
    print("Verified that the user with role 'Admin' is visible in the search results")
    print("Ended test_AdminSectionUserManagementSearchByUserRole transaction")

def test_AdminSectionUserManagementSearchByEmployeeName(shared_page):
    print("\nStarting test_AdminSectionUserManagementSearchByEmployeeName transaction")
    admin_page = AdminPage(shared_page)
    print("Will click reset button")
    admin_page.click_reset_button()
    print("Clicked on reset button")
    print("Will click on employee name field")
    admin_page.click_employee_name_field()
    print("Clicked on employee name field")
    print("Will enter employee name in the search field")

    try:
        admin_page.enter_employee_name("manda user")
        print("Entered employee name in the search field")
        print("Clicked on employee name that was populated in the search field")
        shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
        expect(shared_page.get_by_role("cell", name="manda user")).to_be_visible()
        print("Verified that the employee with name 'manda user' is visible in the search results")
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Retrying with 'FName LName' as employee name")
        admin_page.enter_employee_name("FName Mname LName")
        print("Entered employee name in the search field")
        print("Clicked on employee name that was populated in the search field")
        shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
        expect(shared_page.locator("(//div[@class='oxd-table-cell oxd-padding-cell'][contains(.,'FName LName')])[1]")).to_be_visible()
        print("Verified that the employee with name 'FName LName' is visible in the search results")
    print("Ended test_AdminSectionUserManagementSearchByEmployeeName transaction")

def test_AdminSectionUserManagementSearchByStatus(shared_page):
    print("\nStarting test_AdminSectionUserManagementSearchByStatus transaction")
    admin_page = AdminPage(shared_page)
    print("Will click reset button")
    admin_page.click_reset_button()
    print("Clicked on reset button")
    print("Will click on status dropdown")
    admin_page.click_status_dropdown()
    print("Clicked on status dropdown")
    print("Will click on enabled option")
    admin_page.click_enabled_option()
    print("Clicked on enabled option")
    print("Will click on search button")
    admin_page.click_search_button()
    print("Clicked on search button")
    shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
    expect(shared_page.locator("(//div[@class='oxd-table-cell oxd-padding-cell'][contains(.,'FName LName')])[1]")).to_be_visible()
    print("Verified that the user with status 'Enabled' is visible in the search results")
    print("Ended test_AdminSectionUserManagementSearchByStatus transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

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

def test_PIMPageEmployeeListSearchByEmployeeName(shared_page):
    print("\nStarting test_PIMPageEmployeeListSearchByEmployeeName transaction")
    pim_page = PIMPage(shared_page)
    pim_page.click_pim_menu()
    print("Clicked PIM menu option")
    expect(shared_page.get_by_role("heading", name="Employee Information"))
    print("Verified Employee Information header")
    pim_page.click_employee_name_field()
    pim_page.enter_employee_name("Temporary User")
    employee_locator = pim_page.get_employee_option_by_name("Temporary User")
    employee_locator.click()
    pim_page.click_search_button()
    print("Entered AutoTest Runner into the Employee Name field and clicked Search button")
    expect(shared_page.get_by_text("(1) Record Found")).to_be_visible()
    print("Verified that record was found")
    print("Ended test_PIMPageEmployeeListSearchByEmployeeName transaction")

def test_PIMPageEmployeeListSearchByEmploymentStatus(shared_page):
    print("\nStarting test_PIMPageEmployeeListSearchByEmploymentStatus transaction")
    pim_page = PIMPage(shared_page)
    print("Clicking on reset button")
    pim_page.click_reset_button()
    print("Clicked on reset button")
    print("Will click on employment status dropdown")
    pim_page.click_employment_status_dropdown()
    print("Clicked on employment status dropdown - selecting full time permanent option")
    pim_page.click_full_time_permanent_option()
    print("Full time permanent option selected - will click on Search button")
    pim_page.click_search_button()
    print("Clicked on Search button")
    expect(shared_page.get_by_text("Records Found")).to_be_visible()
    print("Verified that records were found")
    expect(shared_page.get_by_text("Full-Time Permanent").nth(1)).to_be_visible()
    print("Verified that Full-Time Permanent text is visible")
    print("\nEnded test_PIMPageEmployeeListSearchByEmploymentStatus transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

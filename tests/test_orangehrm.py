import time

from playwright.sync_api import Page, expect
from pages.myinfo_page import MyInfoPage
from pages.performance_page import PerformancePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.pim_page import PIMPage
from pages.recruitment_page import RecruitmentPage
from pages.time_page import TimePage
from pages.leave_page import LeavePage
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
    login_page.login("Admin", "admin123")
    shared_page.wait_for_selector("//h6[contains(.,'Dashboard')]")
    print("Ended test_LoginPage transaction")

def test_AdminPage(shared_page):
    print("\nStarting test_AdminPage transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu")
    expect(shared_page.get_by_role("heading", name="System Users")).to_be_visible()
    print("Verified System Users heading is visible on the admin page")
    print("Ended test_AdminPage transaction")

def test_PIMPage(shared_page):
    print("\nStarting test_PIMPage transaction")
    pim_page = PIMPage(shared_page)
    print("Will click on PIM option on the menu")
    pim_page.click_pim_menu()
    print("Clicked on PIM option on the menu")
    shared_page.wait_for_selector("//h6[contains(.,'PIM')]")
    print("Verified PIM heading is visible on the PIM page")
    print("Ended test_PIMPage transaction")

def test_LeavePage(shared_page):
    print("\nStarting test_LeavePage transaction")
    leave_page = LeavePage(shared_page)
    print("Will click on leave option on the menu")
    leave_page.click_leave_menu()
    print("Clicked on leave option on the menu")
    expect(shared_page.get_by_role("heading", name="Leave List")).to_be_visible()
    print("Verified Leave List heading is visible on the leave page")
    expect(shared_page.get_by_role("button", name="Search")).to_be_visible()
    print("Verified Search button is visible on the leave page")
    print("Ended test_LeavePage transaction")

def test_TimePage(shared_page):
    print("\nStarting test_TimePage transaction")
    time_page = TimePage(shared_page)
    print("Will click on time option on the menu")
    time_page.click_time_menu()
    print("Clicked on time option on the menu")
    expect(shared_page.get_by_role("heading", name="Select Employee")).to_be_visible()
    print("Verified Select Employee heading is visible on the time page")
    expect(shared_page.locator("form.oxd-form").get_by_role("button", name="View")).to_be_visible()
    print("Verified View button is visible on the time page")
    print("Ended test_TimePage transaction")

def test_RecruitmentPage(shared_page):
    print("\nStarting test_RecruitmentPage transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on recruitment option on the menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on recruitment option on the menu")
    expect(shared_page.get_by_role("heading", name="Candidates")).to_be_visible()
    print("Verified Candidates heading is visible on the recruitment page")
    expect(shared_page.get_by_role("button", name="Search")).to_be_visible()
    print("Verified Search button is visible on the recruitment page")
    print("Ended test_RecruitmentPage transaction")

def test_MyInfoPage(shared_page):
    print("\nStarting test_MyInfoPage transaction")
    myinfo_page = MyInfoPage(shared_page)
    print("Will click on my info option on the menu")
    myinfo_page.click_myinfo_menu()
    print("Clicked on my info option on the menu")
    expect(shared_page.get_by_role("heading", name="Personal Details")).to_be_visible()
    print("Verified Personal Details heading is visible on the my info page")
    expect(shared_page.get_by_role("button", name="Save")).to_be_visible()
    print("Verified Save button is visible on the my info page")
    print("Ended test_MyInfoPage transaction")

def test_PerformancePage(shared_page):
    print("\nStarting test_PerformancePage transaction")
    performance_page = PerformancePage(shared_page)
    print("Will click on performance option on the menu")
    performance_page.click_performance_menu()
    print("Clicked on performance option on the menu")
    expect(shared_page.get_by_role("heading", name="Employee Reviews")).to_be_visible()
    print("Verified Employee Reviews heading is visible on the performance page")
    print("Ended test_PerformancePage transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

import time

from playwright.sync_api import Page, expect
from pages.performance_page import PerformancePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.leave_page import LeavePage
from pages.logout_page import LogoutPage

def test_HomePage(shared_page):
    print("\nWill go to home page")
    shared_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("Loaded home page")
    home_page = HomePage(shared_page)
    home_page.verify_branding_image_visible()
    print("Verified branding image is visible on the home page")

def test_LoginPage(shared_page):
    login_page = LoginPage(shared_page)
    login_page.login("Admin", "admin123")
    shared_page.wait_for_selector("//h6[contains(.,'Dashboard')]")

def test_PerformancePage(shared_page):
    performance_page = PerformancePage(shared_page)
    print("Will click on performance option on the menu")
    performance_page.click_performance_menu()
    print("Clicked on performance option on the menu")
    expect(shared_page.get_by_role("heading", name="Employee Reviews")).to_be_visible()
    print("Verified Employee Reviews heading is visible on the performance page")

def test_AdminPage(shared_page):
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu")
    expect(shared_page.get_by_role("heading", name="System Users")).to_be_visible()
    print("Verified System Users heading is visible on the admin page")

def test_LeavePage(shared_page):
    testLeavePage = LeavePage(shared_page)
    print("Will click on leave option on the menu")
    testLeavePage.click_leave_menu()
    print("Clicked on leave option on the menu")
    expect(shared_page.get_by_role("heading", name="Leave List")).to_be_visible()
    print("Verified Leave List heading is visible on the leave page")
    expect(shared_page.get_by_role("button", name="Search")).to_be_visible()
    print("Verified Search button is visible on the leave page")

def test_Logout(shared_page):
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    #time.sleep(2)
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    #time.sleep(2)
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")

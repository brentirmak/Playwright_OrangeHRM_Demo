import time

from playwright.sync_api import Page, expect
from pages.performance_page import PerformancePage
from pages.home_page import HomePage
#from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.leave_page import LeavePage
from pages.logout_page import LogoutPage

def test_HomePage(page: Page) -> None:
    print("\nWill go to home page")
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("Loaded home page")
    home_page = HomePage(page)
    home_page.verify_branding_image_visible()
    print("Verified branding image is visible on the home page")

#def test_LoginPage(page: Page) -> None:
    #login_page = LoginPage(page)
    #login_page.username.fill("Admin")
    #login_page.password.fill("admin123")
    #login_page.click_login()
    #expect(page.get_by_text("manda user")).to_be_visible()
'''
def test_PerformancePage(page: Page) -> None:
    performance_page = PerformancePage(page)
    print("Will click on performance option on the menu")
    performance_page.click_performance_menu()
    print("Clicked on performance option on the menu")
    expect(page.get_by_role("heading", name="Employee Reviews")).to_be_visible()
    print("Verified Employee Reviews heading is visible on the performance page")

def test_AdminPage(page: Page) -> None:
    admin_page = AdminPage(page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu")
    expect(page.get_by_role("heading", name="System Users")).to_be_visible()
    print("Verified System Users heading is visible on the admin page")

def test_LeavePage(page: Page) -> None:
    testLeavePage = LeavePage(page)
    print("Will click on leave option on the menu")
    testLeavePage.click_leave_menu()
    print("Clicked on leave option on the menu")
    expect(page.get_by_role("heading", name="Leave List")).to_be_visible()
    print("Verified Leave List heading is visible on the leave page")
    expect(page.get_by_role("button", name="Search")).to_be_visible()
    print("Verified Search button is visible on the leave page")

def test_Logout(page: Page) -> None:
    logout_page = LogoutPage(page)
    print("Will click on logout option on the menu")
    time.sleep(2)
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    time.sleep(2)
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
'''

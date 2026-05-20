import time

from playwright.sync_api import Page, expect
from pages.orangehrm_performance_page import PerformancePage
from pages.orangehrm_home_page import HomePage
#from pages.orangehrm_login_page import LoginPage
from pages.orangehrm_admin_page import AdminPage
from pages.orangehrm_leave_page import LeavePage
from pages.orangehrm_logout_page import LogoutPage

def test_HomePage(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    home_page = HomePage(page)

#def test_LoginPage(page: Page) -> None:
    #login_page = LoginPage(page)
    #login_page.username.fill("Admin")
    #login_page.password.fill("admin123")
    #login_page.click_login()
    #expect(page.get_by_text("manda user")).to_be_visible()

def test_PerformancePage(page: Page) -> None:
    performance_page = PerformancePage(page)
    performance_page.click_performance_menu()
    expect(page.get_by_role("heading", name="Employee Reviews")).to_be_visible()

def test_AdminPage(page: Page) -> None:
    admin_page = AdminPage(page)
    admin_page.click_admin_menu()
    expect(page.get_by_role("heading", name="System Users")).to_be_visible()

def test_LeavePage(page: Page) -> None:
    testLeavePage = LeavePage(page)
    testLeavePage.click_leave_menu()
    expect(page.get_by_role("heading", name="Leave List")).to_be_visible()
    expect(page.get_by_role("button", name="Search")).to_be_visible()

def test_Logout(page: Page) -> None:
    logout_page = LogoutPage(page)
    time.sleep(2)
    logout_page.click_logout()
    time.sleep(2)
    expect(page.get_by_role("button", name="Login")).to_be_visible()



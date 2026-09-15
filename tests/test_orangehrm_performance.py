import re

from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.performance_page import PerformancePage
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

def test_AccessPerformanceSection(shared_page):
    print("\nStarting test_AccessPerformanceSection transaction")
    performance_page = PerformancePage(shared_page)
    print("Will access the Performance section/page")
    performance_page.click_performance_menu()
    print("Clicked on the Performance menu item")
    expect(shared_page.locator("div").filter(has_text=re.compile(r"^PerformanceManage Reviews$"))).to_be_visible()
    expect(shared_page.get_by_role("heading", name="Employee Reviews")).to_be_visible()
    print("Verified that the Employee Reviews header was displayed")
    print("\nEnded test_AccessPerformanceSection transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

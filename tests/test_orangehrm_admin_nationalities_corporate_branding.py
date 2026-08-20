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

def test_NationalitiesCorporateBranding(shared_page):
    print("\nStarting test_NationalitiesCorporateBranding transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Admin menu")
    admin_page.click_admin_menu()
    print("Clicked on Admin menu")
    print("Will click on Nationalities submenu")
    admin_page.click_nationalities_submenu()
    print("Clicked on Nationalities submenu")
    expect(shared_page.get_by_role("heading", name="Nationalities")).to_be_visible()
    print("Verified Nationalities heading is visible on the Nationalities page")
    print("Will click on Corporate Branding submenu")
    admin_page.click_corporate_branding_submenu()
    print("Clicked on Corporate Branding submenu")
    expect(shared_page.get_by_role("heading", name="Corporate Branding")).to_be_visible()
    print("Verified Corporate Branding heading is visible on the Corporate Branding page")
    print("Ended test_NationalitiesCorporateBranding transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

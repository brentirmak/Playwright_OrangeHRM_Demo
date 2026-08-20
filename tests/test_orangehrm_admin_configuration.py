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

def test_AdminConfigurationEmailConfiguration(shared_page):
    print("\nStarting test_AdminConfigurationEmailConfiguration transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu")
    expect(shared_page.locator("h5")).to_contain_text("System Users")
    admin_page.click_configuration_submenu()
    print("Clicked on configuration submenu")
    admin_page.click_email_configuration_submenu()
    print("Clicked on email configuration submenu")
    expect(shared_page.locator("#app")).to_contain_text("Email Configuration")
    print("Verified System Users heading is visible on the admin page")
    print("Ended test_AdminConfigurationEmailConfiguration transaction")

def test_AdminConfigurationEmailSubscriptions(shared_page):
    print("\nStarting test_AdminConfigurationEmailSubscriptions transaction")
    admin_page = AdminPage(shared_page)
    admin_page.click_configuration_submenu()
    print("Clicked on configuration submenu")
    admin_page.click_email_subscription_submenu()
    print("Clicked on email subscription submenu")
    expect(shared_page.get_by_role("heading", name="Email Subscriptions")).to_be_visible()
    print("Verified Email Subscriptions heading is visible on the admin page")
    print("Ended test_AdminConfigurationEmailSubscriptions transaction")

def test_AdminConfigurationLocalization(shared_page):
    print("\nStarting test_AdminConfigurationLocalization transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_configuration_submenu()
    print("Clicked on configuration submenu")
    admin_page.click_localization_submenu()
    print("Clicked on localization submenu")
    expect(shared_page.get_by_role("heading", name="Localization")).to_be_visible()
    print("Verified Localization heading is visible on the admin page")
    print("Ended test_AdminConfigurationLocalization transaction")

def test_AdminConfigurationLanguagePackages(shared_page):
    print("\nStarting test_AdminConfigurationLanguagePackages transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_configuration_submenu()
    print("Clicked on configuration submenu")
    admin_page.click_language_packages_submenu()
    print("Clicked on language packages submenu")
    expect(shared_page.get_by_role("heading", name="Language Packages")).to_be_visible()
    print("Verified Language Packages heading is visible on the admin page")
    print("Ended test_AdminConfigurationLanguagePackages transaction")

def test_AdminConfigurationModules(shared_page):
    print("\nStarting test_AdminConfigurationModules transaction")
    admin_page = AdminPage(shared_page)
    admin_page.click_configuration_submenu()
    print("Clicked on configuration submenu")
    admin_page.click_modules_submenu()
    print("Clicked on modules submenu")
    expect(shared_page.get_by_role("heading", name="Module Configuration")).to_be_visible()
    print("Verified Modules heading is visible on the admin page")
    print("Ended test_AdminConfigurationModules transaction")

def test_AdminConfigurationSocialMediaAuthentication(shared_page):
    print("\nStarting test_AdminConfigurationSocialMediaAuthentication transaction")
    admin_page = AdminPage(shared_page)
    admin_page.click_configuration_submenu()
    print("Clicked on configuration submenu")
    admin_page.click_social_media_authentication_submenu()
    print("Clicked on social media authentication submenu")
    expect(shared_page.get_by_role("heading", name="Provider List")).to_be_visible()
    print("Verified Register OAuth Client heading is visible on the admin page")
    print("Ended test_AdminConfigurationSocialMediaAuthentication transaction")

def test_AdminConfigurationRegisterOAuthClient(shared_page):
    print("\nStarting test_AdminConfigurationRegisterOAuthClient transaction")
    admin_page = AdminPage(shared_page)
    admin_page.click_configuration_submenu()
    print("Clicked on configuration submenu")
    admin_page.click_register_oauth_client_submenu()
    print("Clicked on oauth client submenu")
    expect(shared_page.get_by_role("heading", name="OAuth Client List")).to_be_visible()
    print("Verified OAuth Client List heading is visible on the admin page")
    print("Ended test_AdminConfigurationRegisterOAuthClient transaction")

def test_AdminConfigurationLDAPConfiguration(shared_page):
    print("\nStarting test_AdminConfigurationLDAPConfiguration transaction")
    admin_page = AdminPage(shared_page)
    admin_page.click_configuration_submenu()
    print("Clicked on configuration submenu")
    admin_page.click_ldap_configuration_submenu()
    print("Clicked on ldap configuration submenu")
    expect(shared_page.get_by_role("heading", name="LDAP Configuration")).to_be_visible()
    print("Verified LDAP Configuration heading is visible on the admin page")
    print("Ended test_AdminConfigurationLDAPConfiguration transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

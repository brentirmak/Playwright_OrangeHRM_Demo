from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
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

def test_QualificationsSkills(shared_page):
    print("\nStarting test_QualificationsSkills transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Admin menu")
    admin_page.click_admin_menu()
    print("Clicked on Admin menu")
    print("Will click on Qualifications submenu")
    admin_page.click_qualifications_submenu()
    print("Clicked on Qualifications submenu")
    print("Will click on Skills submenu")
    admin_page.click_skills_submenu()
    print("Clicked on Skills submenu")
    expect(shared_page.get_by_role("heading", name="Skills")).to_be_visible()
    print("Verified Skills heading is visible on the Skills page")
    print("Ended test_QualificationsSkills transaction")

def test_QualificationsEducation(shared_page):
    print("\nStarting test_QualificationsEducation transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Admin menu")
    admin_page.click_admin_menu()
    print("Clicked on Admin menu")
    print("Will click on Qualifications submenu")
    admin_page.click_qualifications_submenu()
    print("Clicked on Qualifications submenu")
    print("Will click on Education submenu")
    admin_page.click_education_submenu()
    print("Clicked on Education submenu")
    expect(shared_page.get_by_role("heading", name="Education")).to_be_visible()
    print("Verified Education heading is visible on the Education page")
    print("Ended test_QualificationsEducation transaction")

def test_QualificationsLicenses(shared_page):
    print("\nStarting test_QualificationsLicenses transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Admin menu")
    admin_page.click_admin_menu()
    print("Clicked on Admin menu")
    print("Will click on Qualifications submenu")
    admin_page.click_qualifications_submenu()
    print("Clicked on Qualifications submenu")
    print("Will click on Licenses submenu")
    admin_page.click_licenses_submenu()
    print("Clicked on Licenses submenu")
    expect(shared_page.get_by_role("heading", name="Licenses")).to_be_visible()
    print("Verified Licenses heading is visible on the Licenses page")
    print("Ended test_QualificationsLicenses transaction")

def test_QualificationsLanguages(shared_page):
    print("\nStarting test_QualificationsLanguages transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Admin menu")
    admin_page.click_admin_menu()
    print("Clicked on Admin menu")
    print("Will click on Qualifications submenu")
    admin_page.click_qualifications_submenu()
    print("Clicked on Qualifications submenu")
    print("Will click on Languages submenu")
    admin_page.click_languages_submenu()
    print("Clicked on Languages submenu")
    expect(shared_page.get_by_role("heading", name="Languages")).to_be_visible()
    print("Verified Languages heading is visible on the Languages page")
    print("Ended test_QualificationsLanguages transaction")

def test_QualificationsMemberships(shared_page):
    print("\nStarting test_QualificationsMemberships transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Admin menu")
    admin_page.click_admin_menu()
    print("Clicked on Admin menu")
    print("Will click on Qualifications submenu")
    admin_page.click_qualifications_submenu()
    print("Clicked on Qualifications submenu")
    print("Will click on Memberships submenu")
    admin_page.click_memberships_submenu()
    print("Clicked on Memberships submenu")
    expect(shared_page.get_by_role("heading", name="Memberships")).to_be_visible()
    print("Verified Memberships heading is visible on the Memberships page")
    print("Ended test_QualificationsMemberships transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

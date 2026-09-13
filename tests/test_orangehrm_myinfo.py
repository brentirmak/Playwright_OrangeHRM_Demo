from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.myinfo_page import MyInfoPage
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

def test_AccessMyInfoSection(shared_page):
    print("\nStarting test_AccessMyInfoSection transaction")
    myinfo_page = MyInfoPage(shared_page)
    print("Will access the My Info section/page")
    myinfo_page.click_myinfo_menu()
    print("Clicked on the My Info menu item")
    expect(shared_page.get_by_role("heading", name="Personal Details")).to_be_visible()
    print("Verified that the Personal Details header was displayed")
    expect(shared_page.get_by_role("heading", name="Attachments")).to_be_visible()
    print("Verified that the Attachments header was displayed")
    print("\nEnded test_AccessMyInfoSection transaction")

def test_AccessMyInfoContactDetailsSubmenu(shared_page):
    print("\nStarting test_AccessMyInfoContactDetailsSubmenu transaction")
    myinfo_page = MyInfoPage(shared_page)
    print("Will access the Contact Details submenu under My Info section/page")
    myinfo_page.click_contact_details_submenu()
    print("Clicked on the Contact Details submenu item")
    expect(shared_page.get_by_role("heading", name="Contact Details")).to_be_visible()
    print("Verified that the Contact Details header was displayed")
    expect(shared_page.get_by_role("heading", name="Attachments")).to_be_visible()
    print("Verified that the Attachments header was displayed")
    print("\nEnded test_AccessMyInfoContactDetailsSubmenu transaction")

def test_AccessMyInfoEmergencyContactsSubmenu(shared_page):
    print("\nStarting test_AccessMyInfoEmergencyContactsSubmenu transaction")
    myinfo_page = MyInfoPage(shared_page)
    print("Will access the Emergency Contacts submenu under My Info section/page")
    myinfo_page.click_emergency_contacts_submenu()
    print("Clicked on the Emergency Contacts submenu item")
    expect(shared_page.get_by_role("heading", name="Assigned Emergency Contacts")).to_be_visible()
    print("Verified that the Assigned Emergency Contacts header was displayed")
    expect(shared_page.get_by_role("heading", name="Attachments")).to_be_visible()
    print("Verified that the Attachments header was displayed")
    print("\nEnded test_AccessMyInfoEmergencyContactsSubmenu transaction")

def test_AccessMyInfoDependentsSubmenu(shared_page):
    print("\nStarting test_AccessMyInfoDependentsSubmenu transaction")
    myinfo_page = MyInfoPage(shared_page)
    print("Will access the Dependents submenu under My Info section/page")
    myinfo_page.click_dependents_submenu()
    print("Clicked on the Dependents submenu item")
    expect(shared_page.get_by_role("heading", name="Assigned Dependents")).to_be_visible()
    print("Verified that the Assigned Dependents header was displayed")
    expect(shared_page.get_by_role("heading", name="Attachments")).to_be_visible()
    print("Verified that the Attachments header was displayed")
    print("\nEnded test_AccessMyInfoDependentsSubmenu transaction")

def test_AccessMyInfoImmigrationSubmenu(shared_page):
    print("\nStarting test_AccessMyInfoImmigrationSubmenu transaction")
    myinfo_page = MyInfoPage(shared_page)
    print("Will access the Immigration submenu under My Info section/page")
    myinfo_page.click_immigration_submenu()
    print("Clicked on the Immigration submenu item")
    expect(shared_page.get_by_role("heading", name="Assigned Immigration Records")).to_be_visible()
    print("Verified that the Assigned Immigration Records header was displayed")
    expect(shared_page.get_by_role("heading", name="Attachments")).to_be_visible()  
    print("Verified that the Attachments header was displayed")
    print("\nEnded test_AccessMyInfoImmigrationSubmenu transaction")

def test_AccessMyInfoJobSubmenu(shared_page):
    print("\nStarting test_AccessMyInfoJobSubmenu transaction")
    myinfo_page = MyInfoPage(shared_page)
    print("Will access the Job submenu under My Info section/page")
    myinfo_page.click_job_submenu()
    print("Clicked on the Job submenu item")
    expect(shared_page.get_by_role("heading", name="Job Details")).to_be_visible()
    print("Verified that the Job Details header was displayed")
    expect(shared_page.get_by_role("heading", name="Attachments")).to_be_visible()
    print("Verified that the Attachments header was displayed")
    print("\nEnded test_AccessMyInfoJobSubmenu transaction")

def test_AccessMyInfoSalarySubmenu(shared_page):
    print("\nStarting test_AccessMyInfoSalarySubmenu transaction")
    myinfo_page = MyInfoPage(shared_page)
    print("Will access the Salary submenu under My Info section/page")
    myinfo_page.click_salary_submenu()
    print("Clicked on the Salary submenu item")
    expect(shared_page.get_by_role("heading", name="Assigned Salary Components")).to_be_visible()
    print("Verified that the Assigned Salary Components header was displayed")
    expect(shared_page.get_by_role("heading", name="Attachments")).to_be_visible()
    print("Verified that the Attachments header was displayed")
    print("\nEnded test_AccessMyInfoSalarySubmenu transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

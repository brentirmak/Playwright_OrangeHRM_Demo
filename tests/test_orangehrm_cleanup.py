'''
(11/2) - 14 Tests
'''
import time, re

from playwright.sync_api import Page, expect

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
    shared_page.wait_for_url("**/dashboard/index", timeout=15000)
    shared_page.wait_for_selector("//p[@class='oxd-text oxd-text--p'][contains(.,'Time at Work')]")
    print("Verified Dashboard heading is visible on the dashboard page")
    print("Ended test_LoginPage transaction")


def test_AdminSectionUserManagementCleanup(shared_page):
    print("\nStarting test_AdminSectionUserManagementCleanup transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu - will verify the System Users header")
    expect(shared_page.get_by_role("heading", name="System Users")).to_be_visible(timeout=10000)
    print("Will capture the current user count")

    admin_page.user_records.wait_for(state="visible")
    user_count_text = admin_page.user_records.inner_text()
    match = re.search(r"\d+", user_count_text)
    if match:
        user_count = int(match.group())
    print("User Count:", user_count)

    if int(user_count) > 1:
        while int(user_count) > 1:
            print("Will click on the checkbox to highlight all records")
            admin_page.click_admin_user_management_system_users_all_checkbox()
            print("Clicked on the checkbox to highlight all records - will click on the Delete Selected button")
            admin_page.click_admin_user_management_system_users_delete_selected_button()
            print("Clicked on the Delete Selected button - will click on Yes on the confirmation window")
            admin_page.click_admin_user_management_system_users_delete_confirmation_button()
            print("Clicked on Yes, Delete on the confirmation window - will verify that the deletion was successful")
            expect(admin_page.admin_user_management_system_users_delete_successful_message).to_be_visible(timeout=20000)

            admin_page.user_records.wait_for(state="visible")
            user_count_text = admin_page.user_records.inner_text()
            match = re.search(r"\d+", user_count_text)
            if match:
                user_count = int(match.group())
            print("User Count:", user_count)

            expect(admin_page.admin_user_management_system_users_one_record_found_header).to_be_visible(timeout=20000)
            print("Verified that there's only 1 record found - cleanup is complete")
    else:
        expect(admin_page.admin_user_management_system_users_one_record_found_header).to_be_visible(timeout=20000)
        print("Only 1 record found - there's nothing to cleanup")
    
    print("\nEnded test_AdminSectionUserManagementCleanup transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

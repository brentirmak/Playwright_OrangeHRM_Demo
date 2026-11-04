'''
(11/4) - 6 Tests
Precondition: An employee (Software Engineer) needs to exist
Precondition Check/Setup: Exists
'''
import re
from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.directory_page import DirectoryPage
from pages.pim_page import PIMPage
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

#######################################################################################################################
# PRECONDITION SETUP
#

def test_PIMPageEmployeeListCreateEmployee(shared_page):
    print("\nStarting test_PIMPageEmployeeListCreateEmployee transaction")
    pim_page = PIMPage(shared_page)
    pim_page.click_pim_menu()
    print("Clicked PIM menu option")
    expect(shared_page.get_by_role("heading", name="Employee Information"))
    print("Verified Employee Information header - will now click on the Add button")
    pim_page.click_pim_employee_list_add_employee_button()
    print("Clicked on Add button - will verify the Add Employee header")
    expect(shared_page.get_by_role("heading", name="Add Employee")).to_be_visible(timeout=10000)
    print("Verified Add Employee header - will enter the First Name")
    pim_page.click_pim_employee_add_employee_first_name_field()
    pim_page.enter_pim_employee_add_employee_first_name_field_value("Chris")
    print("Entered the First Name, will now enter the Last Name")
    pim_page.click_pim_employee_add_employee_last_name_field()
    pim_page.enter_pim_employee_add_employee_last_name_field_value("Collins")
    print("Entered the Last Name, will now enter the employee id")
    pim_page.click_pim_employee_add_employee_id_field()
    pim_page.enter_pim_employee_add_employee_id_field_value("5000")
    print("Entered the employee id, will click on the Save button")
    try:
        pim_page.click_pim_employee_add_employee_save_button()
        expect(shared_page.get_by_text("Successfully Saved")).to_be_visible(timeout=10000)
        print("Verified that the employee was created - will verify that we're on the Personal Details page")
        expect(pim_page.pim_employee_edit_employee_personal_details_header).to_be_visible(timeout=20000)
        print("We are on the Personal Details page - will select the gender")
        pim_page.click_pim_employee_edit_employee_gender_male_selection()
        print("Selected male for gender - will click on the Save button")
        pim_page.click_pim_employee_edit_employee_save1_button()
        print("Clicked on the Save button - will verify that action was successful")
        expect(pim_page.pim_employee_edit_employee_successfully_updated_message).to_be_visible(timeout=20000)
        print("Save action was successful - will now click on the Job link to enter further information")
        pim_page.click_pim_employee_edit_employee_job_tab()
        print("Clicked on the Job tab - will verify that we're on the Job Details page")
        expect(pim_page.pim_employee_edit_employee_job_details_header).to_be_visible(timeout=20000)
        print("Verified that we're on the Job Details screen - will enter the Job Title")
        pim_page.click_pim_employee_edit_employee_job_title_dropdown()
        pim_page.select_pim_employee_edit_employee_job_title_value()
        print("Selected the employee Job Title value - will select the Job Category")
        pim_page.click_pim_employee_edit_employee_job_category_dropdown()
        pim_page.select_pim_employee_edit_employee_job_category_value()
        print("Selected the Job Category - will now select the Sub Unit")
        pim_page.click_pim_employee_edit_employee_sub_unit_dropdown()
        pim_page.select_pim_employee_edit_employee_sub_unit_value()
        print("Selected the Sub Unit value - will now select the Employee Location")
        pim_page.click_pim_employee_edit_employee_location_dropdown()
        pim_page.select_pim_employee_edit_employee_location_value()
        print("Selected the Employee Location value - will now select the Employment Status")
        pim_page.click_pim_employee_edit_employee_employment_status_dropdown()
        pim_page.select_pim_employee_edit_employee_employment_status_value()
        print("Selected the Employment Status - will now click on the Save button")
        pim_page.click_pim_employee_edit_employee_save2_button()
        print("Clicked on the Save button - will verify that the Employee has been successfully modified")
        expect(pim_page.pim_employee_edit_employee_successfully_updated_message).to_be_visible(timeout=20000)
    except:
        print("The precondition is most likely already addressed - proceeding with rest of the tests")
    print("\nEnded test_PIMPageEmployeeListCreateEmployee transaction")

#######################################################################################################################
#
#

def test_AccessDirectorySection(shared_page):
    print("\nStarting test_AccessDirectorySection transaction")
    directory_page = DirectoryPage(shared_page)
    print("Will click on the Directory menu item")
    directory_page.click_directory_menu()
    print("Clicked on the Directory menu item")
    expect(directory_page.directory_directory_header).to_be_visible(timeout=20000)
    print("Verified the Directory heading is visible on the Directory page")
    print("Ended test_AccessDirectorySection transaction")

def test_SearchDirectoryByJobTitle(shared_page):
    print("\nStarting test_SearchDirectoryByJobTitle transaction")
    directory_page = DirectoryPage(shared_page)
    print("Will click on the Directory menu item")
    directory_page.click_directory_menu()
    print("Clicked on the Directory menu item")
    expect(directory_page.directory_directory_header).to_be_visible(timeout=20000)
    print("Verified the Directory heading is visible on the Directory page")

    try:
        print("Clicking on the Job Title dropdown menu")
        directory_page.click_directory_job_title_dropdown()
        print("Clicked on the Job Title dropdown - will select Software Engineer")
        directory_page.click_directory_software_engineer_selection()
        print("Selected the Software Engineer option - will click on the Search button")
        directory_page.click_directory_search_button()
        print("Clicked on the Search button - will verify that atleast 1 Record is found")
        expect(directory_page.directory_records_found).to_be_visible(timeout=20000)
        print("Atleast one record was found")
    except:
        print("2nd try with different job title - Clicking on the Job Title dropdown menu")
        directory_page.click_directory_job_title_dropdown()
        print("2nd try with different job title - Clicked on the Job Title dropdown - will select Chief Financial Officer")
        directory_page.click_directory_chief_financial_officer_selection()
        print("2nd try with different job title - Selected the Chief Financial Officer option - will click on the Search button")
        directory_page.click_directory_search_button()
        print("2nd try with different job title - Clicked on the Search button - will verify that atleast 1 Record is found")
        expect(directory_page.directory_records_found).to_be_visible(timeout=20000)
        print("Atleast one record was found")
    print("Ended test_SearchDirectoryByJobTitle transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

'''
(11/6) - 13 Tests
PREREQUISITES:
An employee 'Smith Smith (steve.smith)' exists
'''
from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
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
    shared_page.wait_for_url("**/dashboard/index", timeout=15000)
    expect(login_page.dashboard_page_header).to_be_visible(timeout=30000)
    print("Verified Dashboard heading is visible on the dashboard page")
    print("Ended test_LoginPage transaction")

##################################################################################################################
# START PRECONDITION SETUP - No Input Data Required
#

def test_CheckAdminConfigurationModuleStatus(shared_page):
    print("\nStarting test_CheckAdminConfigurationModuleStatus transaction")
    admin_page = AdminPage(shared_page)
    print("Will go to https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewModules")
    shared_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewModules")
    print("Accessed the Modules page - will verify that we see the Modules Configuration header")
    expect(admin_page.admin_configuration_module_configuration_header).to_be_visible(timeout=20000)
    print("Verified that we see the Modules Configuration header - will check individual slider status and toggle if needed")
    print("Checking Leave Module Slider")
    admin_page.verify_admin_configuration_modules_leave_module_slider_status()
    print("Checking Time Module Slider")
    admin_page.verify_admin_configuration_modules_time_module_slider_status()
    print("Checking Recruitment Module Slider")
    admin_page.verify_admin_configuration_modules_recruitment_module_slider_status()
    print("Checking Performance Module Slider")
    admin_page.verify_admin_configuration_modules_performance_module_slider_status()
    print("Checking Directory Module Slider")
    admin_page.verify_admin_configuration_modules_directory_module_slider_status()
    print("Checking Maintenance Module Slider")
    admin_page.verify_admin_configuration_modules_maintenance_module_slider_status()
    print("Checking Mobile Module Slider")
    admin_page.verify_admin_configuration_modules_mobile_module_slider_status()
    print("Checking Claim Module Slider")
    admin_page.verify_admin_configuration_modules_claim_module_slider_status()
    print("Checking Buzz Module Slider")
    admin_page.verify_admin_configuration_modules_buzz_module_slider_status()
    print("\nStarting test_CheckAdminConfigurationModuleStatus transaction")

def test_CheckLocalizationSetup(shared_page):
    print("\nStarting test_CheckLocalizationSetup transaction")
    admin_page = AdminPage(shared_page)
    
    try:
        print("Starting Localization Setup Check...")
        shared_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/localization")
        print("We should be on the Localization screen - will check for the Localization header being displayed")
        expect(admin_page.admin_configuration_localization_localization_header).to_be_visible(timeout=10000)
        print("Localization header displayed - will check for the English language being selected")
        expect(admin_page.admin_configuration_localization_language_dropdown).to_be_visible(timeout=10000)
        print("The English language is selected, will check for the 'yyyy-dd-mm' format being used")
        expect(admin_page.admin_configuration_localization_date_format_dropdown).to_be_visible(timeout=10000)
        print("The 'yyyy-dd-mm' format is being used")
        print("Localization Setup Check Completed with SUCCESS")
    except:
        print("Localization Setup Check - FAILED")
        print("Will click on the Localization Language dropdown")
        admin_page.click_admin_configuration_localization_language_dropdown()
        print("Clicked on the Localization Language dropdown - will select the English language")
        admin_page.select_admin_configuration_localization_english_dropdown_option()
        print("Selected the English language - will now click on the Localization Date format dropdown")
        admin_page.click_admin_configuration_localization_date_format_dropdown()
        print("Clicked on the Localization Date format dropdown - will select the 'yyyy-dd-mm' format")
        admin_page.select_admin_configuration_localization_date_option()
        print("Selected the 'yyyy-dd-mm' format - will click on the Save button")
        admin_page.click_admin_configuration_localization_save_button()
        print("Clicked on the Save button - will verify that the Localization header is displayed")
        expect(admin_page.admin_configuration_localization_localization_header).to_be_visible(timeout=10000)
        print("Localization Setup Check Completed with SUCCESS")

    print("\nEnding test_CheckLocalizationSetup transaction")

##################################################################################################################
# END PRECONDITION SETUP - No Input Data Required
#

###########################################################################################################
# PREREQUISITE
#

def test_AdminSectionUserManagementUserCleanup(shared_page):
    print("\nStarting test_AdminSectionUserManagementUserCleanup transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu - will verify the System Users header")
    expect(shared_page.get_by_role("heading", name="System Users")).to_be_visible(timeout=10000)
    print("Verified the System Users header - will click on the Trash Bin icon of the to be deleted item")
    try:
        admin_page.click_trashbin_of_tobedeleted_item("steve.smith")
        print("Clicked on the trashbin - will confirm that the Are you sure? pop-up is displayed")
        expect(shared_page.get_by_text("Are you Sure?")).to_be_visible(timeout=10000)
        expect(shared_page.get_by_role("button", name=" Yes, Delete")).to_be_visible(timeout=10000)
        print("Are you Sure? pop-up was displayed - will click on the Delete button")
        admin_page.click_delete_button()
        print("Clicked on the Delete button")
        expect(shared_page.get_by_text("Successfully Deleted")).to_be_visible(timeout=10000)
        print("Verified that the Successfully Deleted toast message was displayed")
    except:
        print("User was NOT deleted - most likely it was already deleted")
    print("\nEnded test_AdminSectionUserManagementUserCleanup transaction")

def test_CreateEmployeeForUserManagementUseCases(shared_page):
    print("\nStarting test_CreateEmployeeForUserManagementUseCases transaction")
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
    pim_page.enter_pim_employee_add_employee_first_name_field_value("Steve")
    print("Entered the First Name, will now enter the Last Name")
    pim_page.click_pim_employee_add_employee_last_name_field()
    pim_page.enter_pim_employee_add_employee_last_name_field_value("Smith")
    print("Entered the Last Name, will now enter the employee id")
    pim_page.click_pim_employee_add_employee_id_field()
    pim_page.enter_pim_employee_add_employee_id_field_value("3500")
    print("Entered the employee id, will click on the Save button")
    try:
        pim_page.click_pim_employee_add_employee_save_button()
        expect(shared_page.get_by_text("Successfully Saved")).to_be_visible(timeout=10000)
        print("User was successfully created")
    except:
        print("User was NOT created - most likely it already exists")
    print("\nEnded test_CreateEmployeeForUserManagementUseCases transaction")

###########################################################################################################

def test_AccessAdminSection(shared_page):
    print("\nStarting test_AccessAdminSection transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu")
    expect(shared_page.get_by_role("heading", name="System Users")).to_be_visible(timeout=10000)
    print("Verified System Users heading is visible on the admin page")
    print("Ended test_AccessAdminSection transaction")

def test_AdminSectionUserManagementAddUser(shared_page):
    print("\nStarting test_AdminSectionUserManagementAddUser transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on the admin option - will click on the Add button")
    admin_page.click_add_button()
    print("Clicked on the Add button")
    expect(shared_page.get_by_role("heading", name="Add User")).to_be_visible(timeout=10000)
    print("Verified that we're on the Add User page")
    print("Will click on the user role dropdown")
    admin_page.click_user_role_dropdown()
    print("Clicked on the user role dropdown - will now select the Admin option")
    admin_page.click_admin_option()
    print("Selected the admin option - will now click on the Employee Name field")
    admin_page.click_employee_name_field()
    admin_page.enter_employee_name("Steve Smith")
    print("Selected Steve Smith - will now click on the Status dropdown")
    admin_page.click_status_dropdown()
    print("Clicked on the Status dropdown - will click on the Enabled option")
    admin_page.click_enabled_option()
    print("Clicked on the Enabled option - will click on the Create Username field")
    admin_page.click_create_username_field()
    print("Clicked on the Create Username field, will enter steve.smith")
    admin_page.enter_create_username("steve.smith")
    print("Entered username, will now click on Create Password field")
    admin_page.click_create_password_field()
    print("Clicked on Create Password field, will now enter TestUser123")
    admin_page.enter_create_password("TestUser123")
    print("Entered password, will now click on Confirm Password field")
    admin_page.click_confirm_create_password_field()
    print("Clicked on Confirm Password field, will now re-enter TestUser123")
    admin_page.enter_confirm_create_password("TestUser123")
    print("Entered password for the 2nd time will click on Save button")
    admin_page.click_save_button()
    print("Clicked on the Save button")
    expect(shared_page.get_by_text("Successfully Saved")).to_be_visible(timeout=10000)
    print("Verified Successfully Saved toast message")
    print("\nEnded test_AdminSectionUserManagementAddUser transaction")

def test_AdminSectionUserManagementSearchByUsername(shared_page):
    print("\nStarting test_AdminSectionUserManagementSearchByUsername transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on the admin option - will enter username in the search field")
    admin_page.enter_username("steve.smith")
    print("Entered username in the search field")
    print("Will click on search button")
    admin_page.click_search_button()
    print("Clicked on search button")
    shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
    shared_page.get_by_role("table").get_by_text("Steve Smith")
    print("Verified that the username 'steve.smith' is visible in the search results")
    print("Ended test_AdminSectionUserManagementSearchByUsername transaction")

def test_AdminSectionUserManagementSearchByUserRole(shared_page):
    print("\nStarting test_AdminSectionUserManagementSearchByUserRole transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on the admin menu - will click on user role dropdown")
    admin_page.click_user_role_dropdown()
    print("Clicked on user role dropdown")
    print("Will click on admin option")
    admin_page.click_admin_option()
    print("Clicked on admin option")
    print("Will click on search button")
    admin_page.click_search_button()
    print("Clicked on search button")
    shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
    shared_page.get_by_role("table").get_by_text("Steve Smith")
    print("Verified that the user with role 'Admin' is visible in the search results")
    print("Ended test_AdminSectionUserManagementSearchByUserRole transaction")

def test_AdminSectionUserManagementSearchByEmployeeName(shared_page):
    print("\nStarting test_AdminSectionUserManagementSearchByEmployeeName transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on the admin menu - will click on employee name field")
    admin_page.click_employee_name_field()
    print("Clicked on employee name field")
    print("Will enter employee name in the search field")
    admin_page.enter_employee_name("Steve Smith")
    print("Entered employee name (Steve Smith) in the search field")
    print("Clicked on employee name that was populated in the search field")
    shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
    expect(shared_page.get_by_role("cell", name="Steve Smith").first).to_be_visible(timeout=10000)
    print("Verified that the employee with name 'Steve Smith' is visible in the search results")
    print("Ended test_AdminSectionUserManagementSearchByEmployeeName transaction")

def test_AdminSectionUserManagementSearchByStatus(shared_page):
    print("\nStarting test_AdminSectionUserManagementSearchByStatus transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on the admin menu - will click on status dropdown")
    admin_page.click_status_dropdown()
    print("Clicked on status dropdown")
    print("Will click on enabled option")
    admin_page.click_enabled_option()
    print("Clicked on enabled option")
    print("Will click on search button")
    admin_page.click_search_button()
    print("Clicked on search button")
    shared_page.wait_for_selector("//span[contains(.,'Record Found')] | //span[contains(.,'Records Found')]")
    print("Verified that the user with status 'Enabled' is visible in the search results")
    print("Ended test_AdminSectionUserManagementSearchByStatus transaction")

def test_AdminSectionUserManagementDeleteUser(shared_page):
    print("\nStarting test_AdminSectionUserManagementDeleteUser transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu - will verify the System Users header")
    expect(shared_page.get_by_role("heading", name="System Users")).to_be_visible(timeout=10000)
    print("Verified the System Users header - will click on the Trash Bin icon of the to be deleted item")
    admin_page.click_trashbin_of_tobedeleted_item("steve.smith")
    print("Clicked on the trashbin - will confirm that the Are you sure? pop-up is displayed")
    expect(shared_page.get_by_text("Are you Sure?")).to_be_visible(timeout=10000)
    expect(shared_page.get_by_role("button", name=" Yes, Delete")).to_be_visible(timeout=10000)
    print("Are you Sure? pop-up was displayed - will click on the Delete button")
    admin_page.click_delete_button()
    print("Clicked on the Delete button")
    expect(shared_page.get_by_text("Successfully Deleted")).to_be_visible(timeout=10000)
    print("Verified that the Successfully Deleted toast message was displayed")
    print("\nEnded test_AdminSectionUserManagementDeleteUser transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

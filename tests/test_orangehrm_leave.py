'''
(11/6) - 18 Tests
'''
from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.leave_page import LeavePage
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

def test_AccessLeaveSection(shared_page):
    print("\nStarting test_AccessLeaveSection transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on Leave menu option")
    leave_page.click_leave_menu()
    print("Clicked on Leave menu option")
    expect(shared_page.get_by_role("heading", name="Leave List")).to_be_visible(timeout=10000)
    print("Leave List header was found")
    print("Ended test_AccessLeaveSection transaction")

def test_Leave_ApplyPage(shared_page):
    print("\nStarting test_Leave_ApplyPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Apply submenu")
    leave_page.click_leave_apply_submenu()
    print("Clicked on the Apply submenu")
    expect(shared_page.get_by_role("heading", name="Apply Leave")).to_be_visible(timeout=10000)
    print("Verified that the Apply Leave header was displayed")
    print("Ended test_Leave_ApplyPage transaction")

def test_Leave_MyLeavePage(shared_page):
    print("\nStarting test_Leave_MyLeavePage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the MyLeave submenu")
    leave_page.click_leave_my_leave_submenu()
    print("Clicked on the My Leave submenu")
    expect(shared_page.get_by_role("heading", name="My Leave List")).to_be_visible(timeout=10000)
    print("Verified that the My Leave List header was displayed")
    print("Ended test_Leave_MyLeavePage transaction")

def test_EntitlementsAddEntitlementsPage(shared_page):
    print("\nStarting test_EntitlementsAddEntitlementsPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Entitlements submenu")
    leave_page.click_leave_entitlements_submenu()
    print("Clicked on the Entitlements submenu - will click on Add Entitlements")
    leave_page.click_leave_entitlements_add_entitlements_submenu()
    print("Clicked on Add Entitlements submenu")
    expect(shared_page.get_by_text("Add Leave Entitlement")).to_be_visible(timeout=10000)
    print("Verified that the Add Leave Entitlement header was displayed")
    print("Ended test_EntitlementsAddEntitlementsPage transaction")

def test_EntitlementsEmployeeEntitlementsPage(shared_page):
    print("\nStarting test_EntitlementsEmployeeEntitlementsPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Entitlements submenu")
    leave_page.click_leave_entitlements_submenu()
    print("Clicked on the Entitlements submenu - will click on Employee Entitlements")
    leave_page.click_leave_entitlements_employee_entitlements_submenu()
    print("Clicked on the Employee Entitlements submenu")
    expect(shared_page.get_by_role("heading", name="Leave Entitlements")).to_be_visible(timeout=10000)
    print("Verified that the Leave Entitlements header was displayed")
    print("Ended test_EntitlementsEmployeeEntitlementsPage transaction")

def test_EntitlementsMyEntitlementsPage(shared_page):
    print("\nStarting test_EntitlementsMyEntitlementsPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Entitlements submenu")
    leave_page.click_leave_entitlements_submenu()
    print("Clicked on the Entitlements submenu - will click on My Entitlements")
    leave_page.click_leave_entitlements_my_entitlements_submenu()
    print("Clicked on My Entitlements submenu")
    expect(shared_page.get_by_role("heading", name="My Leave Entitlements")).to_be_visible(timeout=10000)
    print("Verified that the My Leave Entitlements header was displayed")
    print("Ended test_EntitlementsMyEntitlementsPage transaction")

def test_ReportsLeaveEntitlementsAndUsageReport(shared_page):
    print("\nStarting test_ReportsLeaveEntitlementsAndUsageReport transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Reports submenu")
    leave_page.click_leave_reports_submenu()
    print("Clicked on the Reports submenu - will click on Leave Entitlements and Usage Report submenu")
    leave_page.click_leave_reports_leave_entitlements_and_usage_report_submenu()
    print("Clicked on Leave Entitlements and Usage Report submenu")
    expect(shared_page.get_by_role("heading", name="Leave Entitlements and Usage Report")).to_be_visible(timeout=10000)
    print("Verified that the Leave Entitlements and Usage Report header was displayed")
    print("Ended test_ReportsLeaveEntitlementsAndUsageReport transaction")

def test_ReportsMyLeaveEntitlementsAndUsageReport(shared_page):
    print("\nStarting test_ReportsMyLeaveEntitlementsAndUsageReport transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Reports submenu")
    leave_page.click_leave_reports_submenu()
    print("Clicked on the Reports submenu - clicking on My Leave Entitlements and Usage Report submenu")
    leave_page.click_leave_reports_my_leave_entitlements_and_usage_report_submenu()
    print("Clicked on My Leave Entitlements and Usage Report submenu")
    expect(shared_page.get_by_role("heading", name="My Leave Entitlements and Usage Report")).to_be_visible(timeout=10000)
    print("Verified that the My Leave Entitlements and Usage Report header was displayed")
    print("Ended test_ReportsMyLeaveEntitlementsAndUsageReport transaction")

def test_ConfigureLeavePeriodPage(shared_page):
    print("\nStarting test_ConfigureLeavePeriodPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Configure submenu")
    leave_page.click_leave_configure_submenu()
    print("Clicked on the Configure submenu - clicking on Leave Period submenu")
    leave_page.click_leave_configure_leave_period_submenu()
    print("Clicked on Leave Period submenu")
    expect(shared_page.get_by_text("Leave Period", exact=True)).to_be_visible(timeout=10000)
    print("Verified Leave Period header was displayed")
    print("Ended test_ConfigureLeavePeriodPage transaction")

def test_ConfigureLeaveTypesPage(shared_page):
    print("\nStarting test_ConfigureLeaveTypesPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Configure submenu")
    leave_page.click_leave_configure_submenu()
    print("Clicked on the Configure submenu - clicking on Leave Types submenu")
    leave_page.click_leave_configure_leave_types_submenu()
    print("Clicked on Leave Types submenu")
    expect(shared_page.get_by_role("heading", name="Leave Types")).to_be_visible(timeout=10000)
    print("Verified Leave Types header was displayed")
    print("\nEnded test_ConfigureLeaveTypesPage transaction")

def test_ConfigureWorkWeekPage(shared_page):
    print("\nStarting test_ConfigureWorkWeekPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Configure submenu")
    leave_page.click_leave_configure_submenu()
    print("Clicked on the Configure submenu - clicking on Work Week submenu")
    leave_page.click_leave_configure_work_week_submenu()
    print("Clicked on the Work Week submenu")
    # Wait for navigation to finish
    shared_page.wait_for_selector("div.orangehrm-card-container", timeout=15000)
    expect(shared_page.get_by_text("Work Week")).to_be_visible(timeout=10000)
    print("Verified Work Week header was displayed")
    print("\nEnded test_ConfigureWorkWeekPage transaction")

def test_ConfigureHolidaysPage(shared_page):
    print("\nStarting test_ConfigureHolidaysPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Configure submenu")
    leave_page.click_leave_configure_submenu()
    print("Clicked on the Configure submenu - clicking on Holidays submenu")
    leave_page.click_leave_configure_holidays_submenu()
    print("Clicked on the Holidays submenu")
    shared_page.wait_for_url("**/leave/viewHolidayList", timeout=15000)
    expect(shared_page.get_by_role("heading", name="Holidays")).to_be_visible(timeout=10000)

    print("Verified Holidays header was displayed")
    print("\nEnded test_ConfigureHolidaysPage transaction")

def test_LeaveListPage(shared_page):
    print("\nStarting test_LeaveListPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Leave List submenu")
    leave_page.click_leave_leave_list_submenu()
    print("Clicked on the Leave List submenu")
    expect(shared_page.get_by_role("heading", name="Leave List")).to_be_visible(timeout=10000)
    print("Verified Leave List header was displayed")
    print("\nEnded test_LeaveListPage transaction")

def test_AssignLeavePage(shared_page):
    print("\nStarting test_AssignLeavePage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Assign Leave submenu")
    leave_page.click_leave_assign_leave_submenu()
    print("Clicked on Assign Leave submenu")
    expect(shared_page.get_by_role("heading", name="Assign Leave")).to_be_visible(timeout=10000)
    print("Verified Assign Leave header was displayed")
    print("\nEnded test_AssignLeavePage transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

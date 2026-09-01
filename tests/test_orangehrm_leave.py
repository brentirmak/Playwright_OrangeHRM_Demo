from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
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
    expect(shared_page.get_by_role("heading", name="Dashboard")).to_be_visible()
    shared_page.wait_for_selector("//h6[contains(.,'Dashboard')]")
    print("Verified Dashboard heading is visible on the dashboard page")
    print("Ended test_LoginPage transaction")

def test_AccessLeaveSection(shared_page):
    print("\nStarting test_AccessLeaveSection transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on Leave menu option")
    leave_page.click_leave_menu()
    print("Clicked on Leave menu option")
    expect(shared_page.get_by_role("heading", name="Leave List")).to_be_visible()
    print("Leave List header was found")
    print("Ended test_AccessLeaveSection transaction")

def test_Leave_ApplyPage(shared_page):
    print("\nStarting test_Leave_ApplyPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Apply submenu")
    leave_page.click_apply_submenu()
    print("Clicked on the Apply submenu")
    expect(shared_page.get_by_role("heading", name="Apply Leave")).to_be_visible()
    print("Verified that the Apply Leave header was displayed")
    print("Ended test_Leave_ApplyPage transaction")

def test_Leave_MyLeavePage(shared_page):
    print("\nStarting test_Leave_MyLeavePage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the MyLeave submenu")
    leave_page.click_my_leave_submenu()
    print("Clicked on the My Leave submenu")
    expect(shared_page.get_by_role("heading", name="My Leave List")).to_be_visible()
    print("Verified that the My Leave List header was displayed")
    print("Ended test_Leave_MyLeavePage transaction")

def test_EntitlementsAddEntitlementsPage(shared_page):
    print("\nStarting test_EntitlementsAddEntitlementsPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Entitlements submenu")
    leave_page.click_entitlements_submenu()
    print("Clicked on the Entitlements submenu - will click on Add Entitlements")
    leave_page.click_add_entitlements_submenu()
    print("Clicked on Add Entitlements submenu")
    expect(shared_page.get_by_text("Add Leave Entitlement")).to_be_visible()
    print("Verified that the Add Leave Entitlement header was displayed")
    print("Ended test_EntitlementsAddEntitlementsPage transaction")

def test_EntitlementsEmployeeEntitlementsPage(shared_page):
    print("\nStarting test_EntitlementsEmployeeEntitlementsPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Entitlements submenu")
    leave_page.click_entitlements_submenu()
    print("Clicked on the Entitlements submenu - will click on Employee Entitlements")
    leave_page.click_employee_entitlements_submenu()
    print("Clicked on the Employee Entitlements submenu")
    expect(shared_page.get_by_role("heading", name="Leave Entitlements")).to_be_visible()
    print("Verified that the Leave Entitlements header was displayed")
    print("Ended test_EntitlementsEmployeeEntitlementsPage transaction")

def test_EntitlementsMyEntitlementsPage(shared_page):
    print("\nStarting test_EntitlementsMyEntitlementsPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Entitlements submenu")
    leave_page.click_entitlements_submenu()
    print("Clicked on the Entitlements submenu - will click on My Entitlements")
    leave_page.click_my_entitlements_submenu()
    print("Clicked on My Entitlements submenu")
    expect(shared_page.get_by_role("heading", name="My Leave Entitlements")).to_be_visible()
    print("Verified that the My Leave Entitlements header was displayed")
    print("Ended test_EntitlementsMyEntitlementsPage transaction")

def test_ReportsLeaveEntitlementsAndUsageReport(shared_page):
    print("\nStarting test_ReportsLeaveEntitlementsAndUsageReport transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Reports submenu")
    leave_page.click_reports_submenu()
    print("Clicked on the Reports submenu - will click on Leave Entitlements and Usage Report submenu")
    leave_page.click_leave_entitlements_and_usage_report_submenu()
    print("Clicked on Leave Entitlements and Usage Report submenu")
    expect(shared_page.get_by_role("heading", name="Leave Entitlements and Usage Report")).to_be_visible()
    print("Verified that the Leave Entitlements and Usage Report header was displayed")
    print("Ended test_ReportsLeaveEntitlementsAndUsageReport transaction")

def test_ReportsMyLeaveEntitlementsAndUsageReport(shared_page):
    print("\nStarting test_ReportsMyLeaveEntitlementsAndUsageReport transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Reports submenu")
    leave_page.click_reports_submenu()
    print("Clicked on the Reports submenu - clicking on My Leave Entitlements and Usage Report submenu")
    leave_page.click_my_leave_entitlements_and_usage_report_submenu()
    print("Clicked on My Leave Entitlements and Usage Report submenu")
    expect(shared_page.get_by_role("heading", name="My Leave Entitlements and Usage Report")).to_be_visible()
    print("Verified that the My Leave Entitlements and Usage Report header was displayed")
    print("Ended test_ReportsMyLeaveEntitlementsAndUsageReport transaction")

def test_ConfigureLeavePeriodPage(shared_page):
    print("\nStarting test_ConfigureLeavePeriodPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Configure submenu")
    leave_page.click_configure_submenu()
    print("Clicked on the Configure submenu - clicking on Leave Period submenu")
    leave_page.click_leave_period_submenu()
    print("Clicked on Leave Period submenu")
    expect(shared_page.get_by_text("Leave Period", exact=True)).to_be_visible()
    print("Verified Leave Period header was displayed")
    print("Ended test_ConfigureLeavePeriodPage transaction")

def test_ConfigureLeaveTypesPage(shared_page):
    print("\nStarting test_ConfigureLeaveTypesPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Configure submenu")
    leave_page.click_configure_submenu()
    print("Clicked on the Configure submenu - clicking on Leave Types submenu")
    leave_page.click_leave_types_submenu()
    print("Clicked on Leave Types submenu")
    expect(shared_page.get_by_role("heading", name="Leave Types")).to_be_visible()
    print("Verified Leave Types header was displayed")
    print("\nEnded test_ConfigureLeaveTypesPage transaction")

def test_ConfigureWorkWeekPage(shared_page):
    print("\nStarting test_ConfigureWorkWeekPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Configure submenu")
    leave_page.click_configure_submenu()
    print("Clicked on the Configure submenu - clicking on Work Week submenu")
    leave_page.click_work_week_submenu()
    print("Clicked on the Work Week submenu")
    expect(shared_page.get_by_text("Work Week")).to_be_visible()
    print("Verified Work Week header was displayed")
    print("\nEnded test_ConfigureWorkWeekPage transaction")

def test_ConfigureHolidaysPage(shared_page):
    print("\nStarting test_ConfigureHolidaysPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Configure submenu")
    leave_page.click_configure_submenu()
    print("Clicked on the Configure submenu - clicking on Holidays submenu")
    leave_page.click_holidays_submenu()
    print("Clicked on the Holidays submenu")
    expect(shared_page.get_by_role("heading", name="Holidays")).to_be_visible()
    print("Verified Holidays header was displayed")
    print("\nEnded test_ConfigureHolidaysPage transaction")

def test_LeaveListPage(shared_page):
    print("\nStarting test_LeaveListPage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Leave List submenu")
    leave_page.click_leave_list_submenu()
    print("Clicked on the Leave List submenu")
    expect(shared_page.get_by_role("heading", name="Leave List")).to_be_visible()
    print("Verified Leave List header was displayed")
    print("\nEnded test_LeaveListPage transaction")

def test_AssignLeavePage(shared_page):
    print("\nStarting test_AssignLeavePage transaction")
    leave_page = LeavePage(shared_page)
    print("Clicking on the Assign Leave submenu")
    leave_page.click_assign_leave_submenu()
    print("Clicked on Assign Leave submenu")
    expect(shared_page.get_by_role("heading", name="Assign Leave")).to_be_visible()
    print("Verified Assign Leave header was displayed")
    print("\nEnded test_AssignLeavePage transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

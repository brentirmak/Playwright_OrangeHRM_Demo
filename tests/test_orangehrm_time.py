from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.time_page import TimePage
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

def test_AccessTimeSection(shared_page):
    print("\nStarting test_AccessTimeSection transaction")
    time_page = TimePage(shared_page)
    print("Will access the Time section/page")
    time_page.click_time_menu()
    print("Clicked on the Time menu item")
    time_page.click_timesheets_submenu()
    print("Clicked on the timesheets submenu")
    time_page.click_my_timesheets_submenu()
    print("Clicked on the My Timesheets submenu")
    expect(shared_page.get_by_role("heading", name="My Timesheet")).to_be_visible()
    print("Verified that the My Timesheet header was displayed")
    print("\nEnded test_AccessTimeSection transaction")

def test_AccessAttendanceMyRecordsPage(shared_page):
    print("\nStarting test_AccessAttendanceMyRecordsPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Attendance submenu")
    time_page.click_attendance_submenu()
    print("Clicked on the Attendance submenu")
    time_page.click_my_records_submenu()
    print("Clicked on the My Records submenu")
    expect(shared_page.get_by_role("heading", name="My Attendance Records")).to_be_visible()
    print("Verified that the My Attendance Records header was displayed")
    print("\nEnded test_AccessAttendanceMyRecordsPage transaction")

def test_AccessAttendancePunchInOutPage(shared_page):
    print("\nStarting test_AccessAttendancePunchInOutPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Attendance submenu")
    time_page.click_attendance_submenu()
    print("Clicked on the Attendance submenu")
    time_page.click_punchin_punchout_submenu()
    print("Clicked on PunchIn/Punchout submenu")
    expect(shared_page.get_by_role("heading", name="Punch In")).to_be_visible()
    print("Verified that the Punch In header was displayed")
    print("\nEnded test_AccessAttendancePunchInOutPage transaction")

def test_AccessAttendanceEmployeeRecordsPage(shared_page):
    print("\nStarting test_AccessAttendanceEmployeeRecordsPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Attendance submenu")
    time_page.click_attendance_submenu()
    print("Clicked on the Attendance submenu")
    time_page.click_employee_records_submenu()
    print("Clicked on the Employee Records submenu")
    expect(shared_page.get_by_role("heading", name="Employee Attendance Records")).to_be_visible()
    print("Verified that the Employee Attendance Reocrds header was displayed")
    print("\nEnded test_AccessAttendanceEmployeeRecordsPage transaction")

def test_AccessAttendanceConfigurationPage(shared_page):
    print("\nStarting test_AccessAttendanceConfigurationPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Attendance submenu")
    time_page.click_attendance_submenu()
    print("Clicked on the Attendance submenu")
    time_page.click_configuration_submenu()
    print("Clicked on the Configuration submenu")
    expect(shared_page.get_by_role("heading", name="Attendance Configuration")).to_be_visible()
    print("Verified that the Attendance Configuration header was displayed")
    print("\nEnded test_AccessAttendanceConfigurationPage transaction")

def test_AccessReportsProjectReportsPage(shared_page):
    print("\nStarting test_AccessReportsProjectReportsPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Reports submenu")
    time_page.click_reports_submenu()
    print("Clicked on the Reports submenu")
    time_page.click_project_reports_submenu()
    print("Clicked on the Project Reports submenu")
    expect(shared_page.get_by_role("heading", name="Project Report")).to_be_visible()
    print("Verified that the Project Report header was displayed")
    print("\nEnded test_AccessReportsProjectReportsPage transaction")

def test_AccessReportsEmployeeReportsPage(shared_page):
    print("\nStarting test_AccessReportsEmployeeReportsPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Reports submenu")
    time_page.click_reports_submenu()
    print("Clicked on the Reports submenu")
    time_page.click_employee_reports_submenu()
    print("Clicked on the Employee Reports submenu")
    expect(shared_page.get_by_role("heading", name="Employee Report")).to_be_visible()
    print("Verified that the Employee Report header was displayed")
    print("\nEnded test_AccessReportsEmployeeReportsPage transaction")

def test_AccessReportsAtendanceSummaryPage(shared_page):
    print("\nStarting test_AccessReportsAtendanceSummaryPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Reports submenu")
    time_page.click_reports_submenu()
    print("Clicked on the Reports submenu")
    time_page.click_attendance_summary_submenu()
    print("Clicked on the Attendance Summary submenu")
    expect(shared_page.get_by_role("heading", name="Attendance Total Summary")).to_be_visible()
    print("Verified that the Attendance Total Summary header was displayed")
    print("\nEnded test_AccessReportsAtendanceSummaryPage transaction")

def test_AccessProjectInfoCustomersPage(shared_page):
    print("\nStarting test_AccessProjectInfoCustomersPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Projects Info submenu")
    time_page.click_project_info_submenu()
    print("Will click on the Customers submenu")
    time_page.click_customers_submenu()
    print("Clicked on the Customers submenu")
    expect(shared_page.get_by_role("heading", name="Customers")).to_be_visible()
    print("Verified that the Customers heading was displayed")
    expect(shared_page.get_by_text("Records Found")).to_be_visible()
    print("Verified that the Records Found text was displayed")
    print("\nEnded test_AccessProjectInfoCustomersPage transaction")

def test_AccessProjectInfoProjectsPage(shared_page):
    print("\nStarting test_AccessProjectInfoProjectsPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Projects Info submenu")
    time_page.click_project_info_submenu()
    print("Will click on the Projects submenu")
    time_page.click_projects_submenu()
    print("Clicked on the Projects submenu")
    expect(shared_page.get_by_role("heading", name="Projects")).to_be_visible()
    print("Verified that the Projects heading was displayed")
    print("\nEnded test_AccessProjectInfoProjectsPage transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

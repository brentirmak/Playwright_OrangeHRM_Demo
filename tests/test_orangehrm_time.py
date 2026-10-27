from datetime import datetime, timedelta

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
    shared_page.wait_for_url("**/dashboard/index", timeout=15000)
    shared_page.wait_for_selector("//p[@class='oxd-text oxd-text--p'][contains(.,'Time at Work')]")
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
    expect(shared_page.get_by_role("heading", name="My Timesheet")).to_be_visible(timeout=10000)
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
    expect(shared_page.get_by_role("heading", name="My Attendance Records")).to_be_visible(timeout=10000)
    print("Verified that the My Attendance Records header was displayed")
    print("\nEnded test_AccessAttendanceMyRecordsPage transaction")

def test_AttendanceMyRecordsCleanup(shared_page):
    print("\nStarting test_AttendanceMyRecordsCleanup transaction")
    time_page = TimePage(shared_page)
    print("Will access the Time section/page")
    time_page.click_time_menu()
    print("Clicked on the Time menu item - will click on the Attendance submenu")
    time_page.click_attendance_submenu()
    print("Clicked on the Attendance submenu")
    time_page.click_my_records_submenu()
    print("Clicked on the My Records submenu")
    expect(shared_page.get_by_role("heading", name="My Attendance Records")).to_be_visible(timeout=10000)
    print("Verified that we're on the My Attendance Records page - will now perform the cleanup")

    try:
        expect(time_page.time_attendance_my_records_trash_icons.first).to_be_visible(timeout=10000)
        count = time_page.time_attendance_my_records_trash_icons.count()
        print("My Attendance Record count: ", count)
        print("Will click on the delete all checkbox to select all membership records")
        time_page.click_my_attendance_records_delete_all_checkbox()
        print("Clicked on the checkbox to select all membership records - will click on the Delete Selected button")
        time_page.click_my_attendance_records_delete_selected_button()
        print("Clicked on the Delete Selected button - will now click on the Yes, Delete button on the confirmation window")
        time_page.click_my_attendance_records_confirm_delete_button()
        print("Clicked on the Yes, Delete button - will confirm that the confirmation toast message is displayed")
        expect(time_page.time_attendance_my_records_successfully_deleted_message).to_be_visible(timeout=20000)
        print("Verified that all attendance records have been deleted")
    except:
        print("No attendance record found to delete - ending test cleanly.")

    print("Verified that the My Attendance Records header was displayed")
    print("\nEnded test_AttendanceMyRecordsCleanup transaction")

def test_AccessAttendancePunchInOutPage(shared_page):
    print("\nStarting test_AccessAttendancePunchInOutPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Attendance submenu")
    time_page.click_attendance_submenu()
    print("Clicked on the Attendance submenu")
    time_page.click_punchin_punchout_submenu()
    print("Clicked on PunchIn/Punchout submenu")

    try:
        expect(shared_page.get_by_role("heading", name="Punch In")).to_be_visible(timeout=10000)
        print("Verified that the Punch In header was displayed")
    except:
        expect(shared_page.get_by_role("heading", name="Punch Out")).to_be_visible(timeout=10000)
        print("Verified that the Punch Out header was displayed --- need to click out to Punch Out/reset")
        expect(time_page.time_attendance_punchinpunchedout_punched_in_time_label).to_be_visible(timeout=10000)
        print("Verified that the Punched in time lavel is displayed - will click on punch out")
        time_page.click_time_attendance_punchinpunchout_punchout_button()
        print("Clicked on the Out button - will verify that it has been clicked")
        expect(time_page.time_attendance_punchout_successfully_saved_message).to_be_visible(timeout=10000)
        print("Verified that the Punch Out was successfully completed")
    print("\nEnded test_AccessAttendancePunchInOutPage transaction")

def test_AttendancePunchIn(shared_page):
    print("\nStarting test_AttendancePunchIn transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Attendance submenu")
    time_page.click_attendance_submenu()
    print("Clicked on the Attendance submenu")
    time_page.click_punchin_punchout_submenu()
    print("Clicked on PunchIn/Punchout submenu")
    expect(shared_page.get_by_role("heading", name="Punch In")).to_be_visible(timeout=10000)
    print("Verified that the Punch In header was displayed - will enter Date")

    punch_in_date = datetime.now().strftime("%Y-%d-%m")
    print("Current punch in date: ", punch_in_date)

    punch_in_time = (datetime.now() - timedelta(minutes=15)).strftime("%I:%M %p")
    print("Current punch in time: ", punch_in_time)

    time_page.enter_time_attendance_punchinpunchout_punchin_date_field_value(punch_in_date)
    print("Entered the Punch In date - will now enter the Punch In time")
    time_page.enter_time_attendance_punchinpunchout_punchin_time_field_value(punch_in_time)
    print("Entered the Punch In time - will click on the In button")
    time_page.click_time_attendance_punchinpunchout_punchin_button()
    print("Clicked ont he Punch In button - will verify that the toast message was displayed")
    expect(time_page.time_attendance_punchin_successfully_saved_message).to_be_visible(timeout=10000)
    print("Punch in was successfully saved messaged was displayed")
    print("\nEnded test_AttendancePunchIn transaction")

def test_AttendancePunchOut(shared_page):
    print("\nStarting test_AttendancePunchOut transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Attendance submenu")
    time_page.click_attendance_submenu()
    print("Clicked on the Attendance submenu")
    time_page.click_punchin_punchout_submenu()
    print("Clicked on PunchIn/Punchout submenu")
    expect(shared_page.get_by_role("heading", name="Punch Out")).to_be_visible(timeout=10000)
    print("Verified that the Punch Out header was displayed - will enter Date")

    punch_out_date = datetime.now().strftime("%Y-%d-%m")
    print("Current punch out date: ", punch_out_date)

    punch_out_time = (datetime.now() - timedelta(minutes=5)).strftime("%I:%M %p")
    print("Current punch out time: ", punch_out_time)

    time_page.enter_time_attendance_punchinpunchout_punchout_date_field_value(punch_out_date)
    print("Entered the Punch Out date - will now enter the Punch Out time")
    time_page.enter_time_attendance_punchinpunchout_punchout_time_field_value(punch_out_time)
    print("Entered the Punch Out time - will click on the Out button")
    time_page.click_time_attendance_punchinpunchout_punchout_button()
    print("Clicked ont he Punch In button - will verify that the toast message was displayed")
    expect(time_page.time_attendance_punchout_successfully_saved_message).to_be_visible(timeout=10000)
    print("Punch out was successfully saved messaged was displayed")
    print("\nEnded test_AttendancePunchOut transaction")

def test_AccessAttendanceEmployeeRecordsPage(shared_page):
    print("\nStarting test_AccessAttendanceEmployeeRecordsPage transaction")
    time_page = TimePage(shared_page)
    print("Will click on the Attendance submenu")
    time_page.click_attendance_submenu()
    print("Clicked on the Attendance submenu")
    time_page.click_employee_records_submenu()
    print("Clicked on the Employee Records submenu")
    expect(shared_page.get_by_role("heading", name="Employee Attendance Records")).to_be_visible(timeout=10000)
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
    expect(shared_page.get_by_role("heading", name="Attendance Configuration")).to_be_visible(timeout=10000)
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
    expect(shared_page.get_by_role("heading", name="Project Report")).to_be_visible(timeout=10000)
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
    expect(shared_page.get_by_role("heading", name="Employee Report")).to_be_visible(timeout=10000)
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
    expect(shared_page.get_by_role("heading", name="Attendance Total Summary")).to_be_visible(timeout=10000)
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
    expect(shared_page.get_by_role("heading", name="Customers")).to_be_visible(timeout=10000)
    print("Verified that the Customers heading was displayed")
    expect(shared_page.get_by_text("Records Found")).to_be_visible(timeout=10000)
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
    expect(shared_page.get_by_role("heading", name="Projects")).to_be_visible(timeout=10000)
    print("Verified that the Projects heading was displayed")
    print("\nEnded test_AccessProjectInfoProjectsPage transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

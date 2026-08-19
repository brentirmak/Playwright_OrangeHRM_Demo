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

def test_AccessAdminSection(shared_page):
    print("\nStarting test_AccessAdminSection transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Clicked on admin option on the menu")
    expect(shared_page.get_by_role("heading", name="System Users")).to_be_visible()
    print("Verified System Users heading is visible on the admin page")
    print("Ended test_AccessAdminSection transaction")

def test_AdminSectionJobTitlesSubmenu(shared_page):
    print("\nStarting test_AdminSectionJobTitlesSubmenu transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Job submenu under Admin menu")
    admin_page.click_job_submenu()
    print("Clicked on Job submenu under Admin menu")
    print("Will click on Job Titles submenu under Job submenu")
    admin_page.click_job_titles_submenu()
    print("Clicked on Job Titles submenu under Job submenu")
    expect(shared_page.get_by_role("columnheader", name="Job Description")).to_be_visible()
    print("Verified Job Description column header is visible on the Job Titles submenu page")
    expect(shared_page.get_by_text("Automaton Tester")).to_be_visible()
    print("Verified Automaton Tester job title is visible on the Job Titles submenu page")
    print("Ended test_AdminSectionJobTitlesSubmenu transaction")

def test_AdminSectionPayGradesSubmenu(shared_page):
    print("\nStarting test_AdminSectionPayGradesSubmenu transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Job submenu under Admin menu")
    admin_page.click_job_submenu()
    print("Clicked on Job submenu under Admin menu")
    print("Will click on Pay Grades submenu under Job submenu")
    admin_page.click_pay_grades_submenu()
    print("Clicked on Pay Grades submenu under Job submenu")
    expect(shared_page.get_by_role("columnheader", name="Currency")).to_be_visible()
    print("Verified Currency column header is visible on the Pay Grades submenu page")
    print("Ended test_AdminSectionPayGradesSubmenu transaction")

def test_AdminSectionEmploymentStatusSubmenu(shared_page):
    print("\nStarting test_AdminSectionEmploymentStatusSubmenu transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Job submenu under Admin menu")
    admin_page.click_job_submenu()
    print("Clicked on Job submenu under Admin menu")
    print("Will click on Employment Status submenu under Job submenu")
    admin_page.click_employment_status_submenu()
    print("Clicked on Employment Status submenu under Job submenu")
    expect(shared_page.get_by_role("columnheader", name="Employment Status")).to_be_visible()
    print("Verified Employment Status column header is visible on the Employment Status submenu page")
    expect(shared_page.get_by_text("Full-Time Permanent")).to_be_visible()
    print("Verified Full-Time Permanent employment status is visible on the Employment Status submenu page")
    print("Ended test_AdminSectionEmploymentStatusSubmenu transaction")

def test_AdminSectionJobCategoriesSubmenu(shared_page):
    print("\nStarting test_AdminSectionJobCategoriesSubmenu transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Job submenu under Admin menu")
    admin_page.click_job_submenu()
    print("Clicked on Job submenu under Admin menu")
    print("Will click on Job Categories submenu under Job submenu")
    admin_page.click_job_categories_submenu()
    print("Clicked on Job Categories submenu under Job submenu")
    expect(shared_page.get_by_role("columnheader", name="Job Category")).to_be_visible()
    print("Verified Job Category column header is visible on the Job Categories submenu page")
    expect(shared_page.get_by_text("Officials and Managers")).to_be_visible()
    print("Verified Officials and Managers job category is visible on the Job Categories submenu page")
    print("Ended test_AdminSectionJobCategoriesSubmenu transaction")

def test_AdminSectionWorkShiftsSubmenu(shared_page):
    print("\nStarting test_AdminSectionWorkShiftsSubmenu transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Job submenu under Admin menu")
    admin_page.click_job_submenu()
    print("Clicked on Job submenu under Admin menu")
    print("Will click on Work Shifts submenu under Job submenu")
    admin_page.click_work_shifts_submenu()
    print("Clicked on Work Shifts submenu under Job submenu")
    expect(shared_page.get_by_role("columnheader", name="Hours Per Day")).to_be_visible()
    print("Verified Hours Per Day column header is visible on the Work Shifts submenu page")
    print("Ended test_AdminSectionWorkShiftsSubmenu transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible()
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

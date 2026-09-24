import re

from playwright.sync_api import Page, expect

from conftest import shared_page
from pages import performance_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.performance_page import PerformancePage
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
    expect(shared_page.get_by_role("heading", name="Dashboard")).to_be_visible(timeout=10000)
    shared_page.wait_for_selector("//h6[contains(.,'Dashboard')]")
    print("Verified Dashboard heading is visible on the dashboard page")
    print("Ended test_LoginPage transaction")

def test_AccessPerformanceSection(shared_page):
    print("\nStarting test_AccessPerformanceSection transaction")
    performance_page = PerformancePage(shared_page)
    print("Will access the Performance section/page")
    performance_page.click_performance_menu()
    print("Clicked on the Performance menu item")
    expect(shared_page.locator("div").filter(has_text=re.compile(r"^PerformanceManage Reviews$"))).to_be_visible(timeout=10000)
    expect(shared_page.get_by_role("heading", name="Employee Reviews")).to_be_visible(timeout=10000)
    print("Verified that the Employee Reviews header was displayed")
    print("\nEnded test_AccessPerformanceSection transaction")

def test_AccessPerformanceConfigureKPIsSubmenu(shared_page):
    print("\nStarting test_AccessPerformanceConfigureKPIsSubmenu transaction")
    performance_page = PerformancePage(shared_page)
    print("Will click on the Configure submenu under Performance section/page")
    performance_page.click_configure_submenu()
    print("Clicked on the Configure submenu item")
    print("Will click on the KPIs submenu under Configure submenu")
    performance_page.click_configure_kpis_submenu()
    print("Clicked on the KPIs submenu item")
    expect(shared_page.get_by_role("heading", name="Key Performance Indicators")).to_be_visible(timeout=10000)
    print("Verified that the Key Performance Indicators header was displayed")
    print("\nEnded test_AccessPerformanceConfigureKPIsSubmenu transaction")

def test_KPISearchByJobTitle(shared_page):
    print("\nStarting test_KPISearchByJobTitle transaction")
    performance_page = PerformancePage(shared_page)
    print("Will click on the Configure submenu under Performance section/page")
    performance_page.click_configure_submenu()
    print("Clicked on the Configure submenu item")
    print("Will click on the KPIs submenu under Configure submenu")
    performance_page.click_configure_kpis_submenu()
    print("Clicked on the KPIs submenu item")
    print("Will click on the Job Title dropdown")
    performance_page.click_job_title_dropdown()
    print("Clicked on the Job Title dropdown")
    print("Will select QA Lead option from the Job Title dropdown")
    performance_page.click_qa_lead_option()
    print("Selected QA Lead option from the Job Title dropdown")
    print("Will click on the Search button")
    performance_page.click_search_button()
    print("Clicked on the Search button")
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible(timeout=10000)
    print("Verified that Record(s) Found was displayed after searching by Job Title QA Lead")
    expect(shared_page.get_by_text("QA Lead").nth(1)).to_be_visible(timeout=10000)
    print("Verified that QA Lead was displayed after searching by Job Title QA Lead")
    print("\nEnded test_KPISearchByJobTitle transaction")

def test_AccessPerformanceTrackersSubmenu(shared_page):
    print("\nStarting test_AccessPerformanceTrackersSubmenu transaction")
    performance_page = PerformancePage(shared_page)
    print("Will click on the Configure submenu under Performance section/page")
    performance_page.click_configure_submenu()
    print("Clicked on the Configure submenu item")
    print("Will click on the Trackers submenu under Configure submenu")
    performance_page.click_trackers_submenu()
    print("Clicked on the Trackers submenu item")
    expect(shared_page.get_by_role("heading", name="Performance Trackers")).to_be_visible(timeout=10000)
    print("Verified that the Performance Trackers header was displayed")
    print("\nEnded test_AccessPerformanceTrackersSubmenu transaction")

def test_AccessPerformanceManageReviewsSubmenu(shared_page):
    print("\nStarting test_AccessPerformanceManageReviewsSubmenu transaction")
    performance_page = PerformancePage(shared_page)
    print("Will click on the Manage Reviews submenu under Performance section/page")
    performance_page.click_manage_reviews_submenu()
    print("Clicked on the Manage Reviews submenu item")
    performance_page.click_manage_reviews_manage_reviews_submenu()
    print("Clicked on the Manage Reviews submenu item under Manage Reviews")
    expect(shared_page.get_by_role("heading", name="Manage Performance Reviews")).to_be_visible(timeout=10000)
    print("Verified that the Manage Performance Reviews header was displayed")
    print("\nEnded test_AccessPerformanceManageReviewsSubmenu transaction")

def test_AccessPerformanceMyReviewsSubmenu(shared_page):
    print("\nStarting test_AccessPerformanceMyReviewsSubmenu transaction")
    performance_page = PerformancePage(shared_page)
    print("Will click on the Manage Reviews submenu under Performance section/page")
    performance_page.click_manage_reviews_submenu()
    print("Clicked on the Manage Reviews submenu item")
    print("Will click on the My Reviews submenu under Performance section/page")
    performance_page.click_my_reviews_submenu()
    print("Clicked on the My Reviews submenu item")
    expect(shared_page.get_by_role("heading", name="My Reviews")).to_be_visible(timeout=10000)
    print("Verified that the My Performance Reviews header was displayed")
    print("\nEnded test_AccessPerformanceMyReviewsSubmenu transaction")

def test_AccessPerformanceEmployeeReviewsSubmenu(shared_page):
    print("\nStarting test_AccessPerformanceEmployeeReviewsSubmenu transaction")
    performance_page = PerformancePage(shared_page)
    print("Will click on the Manage Reviews submenu under Performance section/page")
    performance_page.click_manage_reviews_submenu()
    print("Clicked on the Manage Reviews submenu item")
    print("Will click on the Employee Reviews submenu under Performance section/page")
    performance_page.click_employee_reviews_submenu()
    print("Clicked on the Employee Reviews submenu item")
    expect(shared_page.get_by_role("heading", name="Employee Reviews")).to_be_visible(timeout=10000)
    print("Verified that the Employee Performance Reviews header was displayed")
    print("\nEnded test_AccessPerformanceEmployeeReviewsSubmenu transaction")

def test_AccessPerformanceMyTrackersSubmenu(shared_page):
    print("\nStarting test_AccessPerformanceMyTrackersSubmenu transaction")
    performance_page = PerformancePage(shared_page)
    print("Will click on the My Trackers submenu under Performance section/page")
    performance_page.click_my_trackers_submenu()
    print("Clicked on the My Trackers submenu item")
    expect(shared_page.get_by_role("heading", name="My Performance Trackers")).to_be_visible(timeout=10000)
    print("Verified that the My Trackers header was displayed")
    print("\nEnded test_AccessPerformanceMyTrackersSubmenu transaction")

def test_AccessPerformanceEmployeeTrackersSubmenu(shared_page):
    print("\nStarting test_AccessPerformanceEmployeeTrackersSubmenu transaction")
    performance_page = PerformancePage(shared_page)
    print("Will click on the Employee Trackers submenu under Performance section/page")
    performance_page.click_employee_trackers_submenu()
    print("Clicked on the Employee Trackers submenu item")
    shared_page.get_by_role("link", name="Employee Trackers").click()
    shared_page.wait_for_url("**/performance/viewEmployeePerformanceTrackerList", timeout=15000)
    shared_page.wait_for_selector("div.orangehrm-paper-container", timeout=15000)
    expect(shared_page.get_by_role("heading", name="Employee Performance Trackers")).to_be_visible(timeout=10000)
    print("Verified that the Employee Trackers header was displayed")
    print("\nEnded test_AccessPerformanceEmployeeTrackersSubmenu transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

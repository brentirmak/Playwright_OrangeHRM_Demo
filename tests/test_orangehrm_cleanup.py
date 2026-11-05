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

def test_AdminSectionUserManagementBulkCleanup(shared_page):
    print("\nStarting test_AdminSectionUserManagementBulkCleanup transaction")
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
    
    print("\nEnded test_AdminSectionUserManagementBulkCleanup transaction")

def test_AdminSectionJobTitlesBulkCleanup(shared_page):
    print("\nStarting test_AdminSectionJobTitlesBulkCleanup transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on admin option on the menu")
    admin_page.click_admin_menu()
    print("Will click on Job submenu under Admin menu")
    admin_page.click_job_submenu()
    print("Clicked on Job submenu under Admin menu")
    print("Will click on Job Titles submenu under Job submenu")
    admin_page.click_job_titles_submenu()
    print("Clicked on Job Titles submenu under Job submenu")
    expect(shared_page.get_by_role("columnheader", name="Job Description")).to_be_visible(timeout=10000)
    expect(admin_page.admin_job_titles_header).to_be_visible(timeout=20000)
    try:
        print("Verified that we're on the Job Titles page - scanning for records to cleanup...")
        
        # Define the set of job titles to keep/preserve
        preserved_titles = {
            "Account Assistant", "Chief Executive Officer", "Chief Financial Officer", 
            "Chief Technical Officer", "Content Specialist", "Customer Success Manager", 
            "Database Administrator", "Finance Manager", "Financial Analyst", 
            "Head of Support", "HR Associate", "HR Manager", "IT Manager", 
            "Network Administrator", "Payroll Administrator", "Pre-Sales Coordinator", 
            "QA Engineer", "QA Lead", "Sales Representative", "Social Media Marketer", 
            "Software Architect", "Software Engineer", "Support Specialist", 
            "VP - Client Services", "VP - Sales & Marketing"
        }
        
        # Locate all job title cells in the table (adjust the selector if your page object has a specific locator for them)
        # OrangeHRM typically stores job titles in the second column of the table rows
        job_title_elements = admin_page.page.locator("div.oxd-table-body div.oxd-table-card div.oxd-table-cell:nth-child(2)")
        
        # Get all text contents currently displayed on the page
        current_titles = job_title_elements.all_inner_texts()
        
        # Filter out titles that are in our preserved list
        titles_to_delete = [title.strip() for title in current_titles if title.strip() and title.strip() not in preserved_titles]
        
        if titles_to_delete:
            print(f"Found {len(titles_to_delete)} unpreserved job title(s) to delete: {titles_to_delete}")
            
            # Select the checkboxes for each unpreserved job title using your existing page helper
            for title in titles_to_delete:
                admin_page.click_admin_job_titles_click_checkbox_by_jobtitle(title)
                print(f"Clicked on the checkbox associated with {title}")
                
            # Perform the bulk delete for all selected items
            admin_page.click_admin_job_titles_delete_job_title_delete_selected_button()
            print("Clicked on the Delete Selected button - will now click on the Yes, Delete button on the confirmation window")
            
            admin_page.click_admin_job_titles_delete_job_title_delete_confirmation_button()
            print("Clicked on the Yes, Delete button, will confirm that the records have been deleted")
            
            expect(admin_page.admin_job_titles_delete_job_title_delete_confirmation_message).to_be_visible(timeout=10000)
            print("Verified unpreserved job titles have been successfully deleted")
        else:
            print("No cleanup needed: All current job titles are in the preserved list.")

    except Exception as e:
        print(f"There was no record to delete/cleanup or an error occurred: {e} - will proceed with remaining tests execution")
    print("Ended test_AdminSectionJobTitlesBulkCleanup transaction")

def test_QualificationsSkillsBulkCleanup(shared_page):
    print("\nStarting test_QualificationsSkillsBulkCleanup transaction")
    admin_page = AdminPage(shared_page)
    print("Will click on Admin menu")
    admin_page.click_admin_menu()
    print("Clicked on Admin menu")
    print("Will click on Qualifications submenu")
    admin_page.click_qualifications_submenu()
    print("Clicked on Qualifications submenu")
    print("Will click on Skills submenu")
    admin_page.click_skills_submenu()
    print("Clicked on Skills submenu")
    expect(shared_page.get_by_role("heading", name="Skills")).to_be_visible(timeout=10000)
    print("Verified that the Skills header was displayed - will proceed with scanning for records to cleanup")
    
    try:
        preserved_skills = {
            "Content Creation", "Copywriting", "G Suite", "Google Analytics", 
            "Java", "JavaScript", "JIRA", "Office Suite", "Perl", "Photoshop", 
            "PHP", "Python", "React Native", "Ruby", "Search Engine Optimization (SEO)", 
            "SQL", "Swift", "Trello", "UI/UX Design", "Wireframing"
        }
        
        skill_name_elements = shared_page.locator("div.oxd-table-body div.oxd-table-card div.oxd-table-cell:nth-child(2)")
        current_skills = skill_name_elements.all_inner_texts()
        skills_to_delete = [skill.strip() for skill in current_skills if skill.strip() and skill.strip() not in preserved_skills]
        
        if skills_to_delete:
            print(f"Found {len(skills_to_delete)} unpreserved skill(s) to delete: {skills_to_delete}")
            
            for skill in skills_to_delete:
                try:
                    print(f"Attempting to delete skill: {skill}")
                    # Find the specific row and click its trash icon safely
                    row = shared_page.locator("div.oxd-table-row").filter(has_text=skill)
                    row.locator("button i.bi-trash").click()
                    
                    # Confirm deletion on the modal popup window that appears
                    confirm_btn = shared_page.locator("button.oxd-button--label-danger", has_text="Yes, Delete")
                    confirm_btn.click()
                    
                    # Wait for the success toast message and for the modal overlay to fully detach/disappear
                    expect(admin_page.qualifications_successfully_deleted_message).to_be_visible(timeout=10000)
                    shared_page.locator("div.oxd-dialog-container-default").wait_for(state="detached", timeout=10000)
                    
                    print(f"Successfully deleted skill: {skill}")
                except Exception as inner_e:
                    print(f"Could not delete skill '{skill}' due to error: {inner_e}")
        else:
            print("No cleanup needed: All current skills are in the preserved list.")
            
    except Exception as e:
        print(f"There was no record to delete/cleanup or an error occurred: {e} - OK to proceed")
    print("\nEnded test_QualificationsSkillsBulkCleanup transaction")

def test_PIMPageEmployeeBulkCleanup(shared_page):
    print("\nStarting test_PIMPageEmployeeBulkCleanup transaction")
    pim_page = PIMPage(shared_page)
    pim_page.click_pim_menu()
    print("Clicked PIM menu option")
    expect(shared_page.get_by_role("heading", name="Employee Information"))
    print("Verified Employee Information header")

    print("Will capture the current user count")

    pim_page.pim_employee_list_user_records.wait_for(state="visible")
    user_count_text = pim_page.pim_employee_list_user_records.inner_text()
    match = re.search(r"\d+", user_count_text)
    if match:
        user_count = int(match.group())
    print("User Count:", user_count)

    if int(user_count) > 1:
        while int(user_count) > 1:
            print("Will click on the checkbox to highlight all records")
            pim_page.click_pim_employee_list_bulk_delete_checkbox()
            print("Clicked on the checkbox to highlight all records - will click on the Delete Selected button")
            pim_page.click_pim_employee_list_bulk_delete_delete_selected_button()
            print("Clicked on the Delete Selected button - will click on Yes on the confirmation window")
            pim_page.click_pim_employee_list_bulk_delete_delete_confirmation_button()
            print("Clicked on Yes, Delete on the confirmation window - will verify that the deletion was successful")
            expect(pim_page.pim_employee_list_bulk_delete_successfully_deleted_message).to_be_visible(timeout=20000)

            pim_page.pim_employee_list_user_records.wait_for(state="visible")
            user_count_text = pim_page.pim_employee_list_user_records.inner_text()
            match = re.search(r"\d+", user_count_text)
            if match:
                user_count = int(match.group())
            print("User Count:", user_count)

            expect(pim_page.pim_employee_list_one_record_found_header).to_be_visible(timeout=20000)
            print("Verified that there's only 1 record found - cleanup is complete")
    else:
        expect(pim_page.pim_employee_list_one_record_found_header).to_be_visible(timeout=20000)
        print("Only 1 record found - there's nothing to cleanup")
    print("\nEnded test_PIMPageEmployeeBulkCleanup transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

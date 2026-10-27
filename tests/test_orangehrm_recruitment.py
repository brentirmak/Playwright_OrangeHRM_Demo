import re
import time
from playwright.sync_api import Page, expect

from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from pages.admin_page import AdminPage
from pages.recruitment_page import RecruitmentPage
from pages.logout_page import LogoutPage

'''
Preconditions:
(1) https://opensource-demo.orangehrmlive.com/web/index.php/admin/localization (English/yyyy-dd-mm)
(2) Under Admin->Job, Software Engineer entry
(3) Under PIM->Add Employee, Charles Carter entry
'''

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

##############################################################################################################
# START - PRECONDITION
##############################################################################################################
def test_RecruitmentPreconditionSetup(shared_page):
    print("\nStarting test_RecruitmentPreconditionSetup transaction")
    admin_page = AdminPage(shared_page)
    pim_page = PIMPage(shared_page)
    
    print("\n")

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

    print("\n")

    try:
        print("Starting 'Under Admin->Job, Software Engineer entry' Check...")
        shared_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")
        expect(shared_page.locator(".oxd-table-body .oxd-table-card").first).to_be_visible(timeout=20000)
        row = shared_page.get_by_role("row").filter(has=shared_page.get_by_text("Software Engineer", exact=True))
        print("Match count: ", row.count())

        if row.count() > 0:
            print("We already have a Software Engineer entry - no further action is needed")
            print("Software Engineer entry Check Completed with SUCCESS")
        else:
            print("We do NOT have a Software Engineer entry - we will need to create one")

            print("We need to click on the Job Title Add button")
            admin_page.click_admin_job_titles_add_button()
            print("Clicked on the Add button - will verify that we're on the Add Job Title page")
            expect(admin_page.admin_job_titles_add_job_title_header).to_be_visible(timeout=20000)
            print("We are on the Add Job Title page - will now enter the job Title")
            admin_page.click_admin_job_titles_add_job_title_field()
            admin_page.enter_admin_job_titles_add_job_title_field_value("Software Engineer")
            print("Entered the Software Engineer title - will click on the Save button")
            admin_page.click_admin_job_titles_add_job_title_save_button()
            print("Clicked on the Save button - will verify that the record was saved")
            expect(admin_page.admin_job_titles_add_job_title_successfully_saved_message).to_be_visible(timeout=20000)
    except:
        print("Was unable to check or add Software Engineer entry")

    print("\n")

    try:
        print("Starting Check 'Under PIM->Add Employee, Charles Carter entry'")
        shared_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        expect(shared_page.locator(".oxd-table-body .oxd-table-card").first).to_be_visible(timeout=20000)
        row = shared_page.get_by_role("row").filter(has=shared_page.get_by_text("Carter", exact=True))
        print("Match count: ", row.count())

        if row.count() > 0:
            print("We already have a Charles Carter entry - no further action is needed")
            print("'Under PIM->Add Employee, Charles Carter entry' Completed with SUCCESS")
        else:
            print("We do NOT have a Charles Carter entry - we will need to create one")
            pim_page.click_pim_employee_list_add_button()
            print("Clicked on the Add button - will now enter the First Name")
            pim_page.click_pim_employee_add_employee_first_name_field()
            pim_page.enter_pim_employee_add_employee_first_name_field_value("Charles")
            print("Entered the First Name, will now enter the Last Name")
            pim_page.click_pim_employee_add_employee_last_name_field()
            pim_page.enter_pim_employee_add_employee_last_name_field_value("Carter")
            print("Entered the Last Name, will click on the Save button")
            pim_page.click_pim_employee_add_employee_save_button()
            print("Clicked on the Save button - will verify that the employee was successfully added")
            expect(pim_page.pim_employee_add_employee_successfully_saved_message).to_be_visible(timeout=20000)
            print("Employee was successfully added message was displayed")
    except:
        print("Was unable to check or add 'Charles Carter' entry")

    print("Ended test_RecruitmentPreconditionSetup transaction\n")
##############################################################################################################
# END - PRECONDITION
##############################################################################################################

##############################################################################################################
# START: Cleanup Code
#

def test_RecruitmentPageCandidateCleanup(shared_page):
    print("\nStarting test_RecruitmentPageCandidateCleanup transaction")

    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on the Recruitment menu - will now click on the Candidates tab")
    recruitment_page.click_candidates_tab()
    try:
        print("Clicked on the candidates submenu/tab - will now click on the Delete All checkbox")
        recruitment_page.click_candidates_delete_candidate_delete_all_checkbox()
        print("Clicked on the Delete All checkbox - will now click on the Delete Selected button")
        recruitment_page.click_candidates_delete_candidate_delete_selected_button()
        print("Clicked on the Delete Selected button - will click on the Yes, Delete confirmation button")
        recruitment_page.click_candidates_delete_candidate_confirm_delete_button()
        print("Clicked on the Delete Confirmation button - will verify record has been deleted")
        expect(recruitment_page.candidates_delete_candidate_successfully_deleted_message).to_be_visible(timeout=15000)
        print("All records have been deleted for a successful cleanup")
    except:
        print("There are no records to delete/cleanup - proceeding....")
    print("\nEnded test_RecruitmentPageCandidateCleanup transaction")

def test_RecruitmentPageVacancyCleanup(shared_page):
    print("\nStarting test_RecruitmentPageVacancyCleanup transaction")

    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on the Recruitment menu - will now click on the Vacancies tab")
    recruitment_page.click_vacancies_submenu()
    try:
        print("Clicked on the vacancies submenu/tab - will now click on the Delete All checkbox")
        recruitment_page.click_vacancies_delete_vacancy_delete_all_checkbox()
        print("Clicked on the Delete All checkbox - will now click on the Delete Selected button")
        recruitment_page.click_vacancies_delete_vacancy_delete_selected_button()
        print("Clicked on the Delete Selected button - will click on the Yes, Delete confirmation button")
        recruitment_page.click_vacancies_delete_vacancy_confirm_delete_button()
        print("Clicked on the Delete Confirmation button - will verify record has been deleted")
        expect(recruitment_page.vacancies_delete_vacancy_successfully_deleted_message).to_be_visible(timeout=15000)
        print("Verified that the vacancy was successfully deleted message was displayed")
    except:
        print("There are no records to delete/cleanup - proceeding....")
    print("\nEnded test_RecruitmentPageVacancyCleanup transaction")

##############################################################################################################
# END: Cleanup Code
#

##############################################################################################################
# START: Candidates Tab
#
def test_RecruitmentPageCreateVacancy(shared_page):
    print("\nStarting test_RecruitmentPageCreateVacancy transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on the Recruitment menu - will now click on the Vacancies tab")
    recruitment_page.click_vacancies_submenu()
    print("Clicked on the vacancies submenu/tab - will click on the Add button")
    recruitment_page.click_vacancies_add_button()
    print("Clicked on the Add button - will verify that the 'Add Vacancy' page is displayed")
    expect(recruitment_page.vacancies_add_vacancy_header).to_be_visible(timeout=15000)
    print("Will add vacancy - first enter the Vacancy Name")
    recruitment_page.click_vacancies_add_vacancy_name_field()
    recruitment_page.enter_vacancies_add_vacancy_name_field_value("Principle QA Test")
    print("Entered 'Principle QA Test' as the vacancy name - will now select Job Title")
    recruitment_page.click_vacancies_add_vacancy_job_title_dropdown()
    recruitment_page.select_vacancies_add_vacancy_job_title_dropdown_option("Software Engineer")
    print("Selected the 'Software Engineer' option - will now enter a description")
    recruitment_page.click_vacancies_add_vacancy_description_field()
    recruitment_page.enter_vacancies_add_vacancy_description_field_value("Test position for automation purposes")
    print("Entered a description for the vacancy - will now select the hiring manager")
    recruitment_page.click_vacancies_add_vacancy_hiring_manager_field()
    recruitment_page.enter_vacancies_hiring_manager("Ch")
    print("Entered hiring manager - will now click on the Save button")
    recruitment_page.click_vacancies_add_vacancy_save_button()
    expect(recruitment_page.vacancies_edit_vacancy_edit_vacancy_title).to_be_visible(timeout=15000)
    print("Verified that the Edit Vacancy page was displayed upon saving the record")
    print("\nEnded test_RecruitmentPageCreateVacancy transaction")

def test_RecruitmentPageAddCandidate(shared_page):
    print("\nStarting test_RecruitmentPageAddCandidate transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on the Recruitment menu - will now click on the Candidates tab")
    recruitment_page.click_candidates_tab()
    print("Clicked on the Candidates tab - will click on Add button")
    recruitment_page.click_candidates_add_button()
    print("Clicked on the Add button - will check for 'Add Candidate' header")
    print("Add Candidate header found - will now enter the First Name")
    recruitment_page.click_candidates_add_candidate_first_name_field()
    recruitment_page.enter_candidates_add_candidate_first_name_field("Mike")
    print("Entered First Name - will now enter the Last Name")
    recruitment_page.click_candidates_add_candidate_last_name_field()
    recruitment_page.enter_candidates_add_candidate_last_name_field("Jones")
    print("Entered Last Name - will now enter the Email Address")
    recruitment_page.click_candidates_add_candidate_email_address_field()
    recruitment_page.enter_candidates_add_candidate_email_address_field("test@test.com")
    print("Entered the Email Address - will now select the Vacancy from the dropdown")
    recruitment_page.click_candidates_add_candidate_vacancy_dropdown()
    recruitment_page.select_candidates_add_candidate_select_principle_qa_test_option()
    print("Selected Principle QA Test option - will now click on the Save button")
    recruitment_page.click_candidates_add_candidate_save_button()
    print("Clicked on the Save button - will now verify that the new record has been crated")
    expect(recruitment_page.candidates_add_candidate_new_record_saved).to_be_visible(timeout=15000)
    print("New record has been created message has been displayed")
    print("\nEnded test_RecruitmentPageAddCandidate transaction")

def test_RecruitmentPageSearchCandidatesByName(shared_page):
    print("\nStarting test_RecruitmentPageSearchCandidatesByName transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on Recruitment menu - will now click on the Candidates tab")
    recruitment_page.click_candidates_tab()
    expect(recruitment_page.candidates_candidates_header).to_be_visible(timeout=15000)
    print("Verified that we're on the Candidates page - Will click on Name dropdown")
    recruitment_page.click_candidates_search_candidate_candidate_name_field()
    print("Will select Mike Jones option from the dropdown")
    recruitment_page.enter_candidates_search_candidate_candidate_name_field_value("Mike Jones")
    print("Selected candidate name, will click on will click on Search button")
    recruitment_page.click_candidates_search_candidate_search_button()
    print("Clicked on Search button - will verify a result was returned")
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible(timeout=10000)
    print("Verified Records Found is visible in the search results")
    print("Ended test_RecruitmentPageSearchCandidatesByName transaction")

def test_RecruitmentPageSearchCandidatesByVacancy(shared_page):
    print("\nStarting test_RecruitmentPageSearchByVacancy transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on Recruitment menu - will now click on the Candidates tab")
    recruitment_page.click_candidates_tab()
    expect(recruitment_page.candidates_candidates_header).to_be_visible(timeout=15000)
    print("Verified that we're on the Candidates page - Will click on Vacacy dropdown")
    recruitment_page.click_candidates_search_candidate_vacancy_dropdown()
    print("Clicked on Vacancy dropdown - Will select the vacancy option from the vacancy dropdown")
    recruitment_page.select_candidates_search_vacancy_vacancy_dropdown_option("Principle QA Test")
    print("Selected the vacancy option from the dropdown - will click on the Search button")
    recruitment_page.click_candidates_search_candidate_search_button()
    print("Clicked on Search button - will verify a result was returned")
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible(timeout=10000)
    print("Verified Records Found is visible in the search results")
    print("Ended test_RecruitmentPageSearchCandidatesByVacancy transaction")

def test_RecruitmentPageSearchCandidatesByHiringManager(shared_page):
    print("\nStarting test_RecruitmentPageSearchCandidatesByHiringManager transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on Recruitment menu - will now click on the Candidates tab")
    recruitment_page.click_candidates_tab()
    expect(recruitment_page.candidates_candidates_header).to_be_visible(timeout=15000)
    print("Verified that we're on the Candidates page - Will click on Hiring Manager dropdown")
    recruitment_page.click_candidates_search_vacancy_hiring_manager_dropdown()
    print("Clicked on Hiring Manager dropdown - will select option from the dropdown")
    recruitment_page.select_candidates_search_vacancy_hiring_manager_dropdown_option("Charles Carter")
    print("Selected option from the dropdown - will click on Search button")
    recruitment_page.click_candidates_search_candidate_search_button()
    print("Clicked on Search button")
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible(timeout=10000)
    print("Verified Records Found is visible in the search results")
    print("Ended test_RecruitmentPageSearchCandidatesByHiringManager transaction")

def test_RecruitmentPageSearchCandidatesByStatus(shared_page):
    print("\nStarting test_RecruitmentPageSearchCandidatesByStatus transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on Recruitment menu - will now click on the Candidates tab")
    recruitment_page.click_candidates_tab()
    expect(recruitment_page.candidates_candidates_header).to_be_visible(timeout=15000)
    print("Verified that we're on the Candidates page - Will click on Status dropdown")
    recruitment_page.click_candidates_search_candidate_status_dropdown()
    print("Clicked on Status dropdown")
    recruitment_page.select_candidates_search_candidate_status_application_initiated_option("Application Initiated")
    print("Selected Application Initiated option from the dropdown")
    print("Will click on Search button")
    recruitment_page.click_candidates_search_candidate_search_button()
    print("Clicked on Search button")
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible(timeout=10000)
    print("Verified Records Found is visible in the search results")
    print("Ended test_RecruitmentPageSearchCandidatesByStatus transaction")

def test_RecruitmentPageSearchCandidatesByKeywords(shared_page):
    print("\nStarting test_RecruitmentPageSearchCandidatesByKeywords transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on Recruitment menu - will now click on the Candidates tab")
    recruitment_page.click_candidates_tab()
    expect(recruitment_page.candidates_candidates_header).to_be_visible(timeout=15000)
    print("Verified that we're on the Candidates page - Will click on Keywords textbox")
    recruitment_page.click_candidates_search_candidate_keywords_field()
    print("Clicked on Keywords textbox - will enter keywords in the textbox")
    recruitment_page.enter_candidates_search_candidate_keywords_field_value("test@test.com")
    print("Entered keywords in the textbox - will click on Search button")
    recruitment_page.click_candidates_search_candidate_search_button()
    print("Clicked on Search button - will verify that records were found")
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible(timeout=10000)
    print("Verified Records Found is visible in the search results")
    print("Ended test_RecruitmentPageSearchCandidatesByKeywords transaction")

##############################################################################################################
# END: Candidates Tab
#

##############################################################################################################
# START: Vacancies Tab
#

def test_RecruitmentPageVacanciesSearchByJobTitle(shared_page):
    print("\nStarting test_RecruitmentPageVacanciesSearchByJobTitle transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Will click on Vacancies submenu")
    recruitment_page.click_vacancies_submenu()
    print("Clicked on the Vacancies submenu - will verify that we're on the Vacancies page")
    expect(recruitment_page.vacancies_vacancies_header).to_be_visible(timeout=10000)
    print("Verified that we're on the Vacancies page - will click on Job Title dropdown")
    recruitment_page.click_vacancies_search_vacancy_job_title_dropdown()
    print("Clicked on Job Title dropdown - will select Software Engineer option from the dropdown")
    recruitment_page.select_vacancies_search_vacancy_job_title_dropdown_option("Software Engineer")
    print("Selected Software Engineer option from the dropdown - will click on Search button")
    recruitment_page.click_vacancies_search_vacancy_search_button()
    print("Clicked on Search button - will verify that records were found")
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible(timeout=10000)
    print("Verified Records Found is visible in the search results")
    print("Ended test_RecruitmentPageVacanciesSearchByJobTitle transaction")

def test_RecruitmentPageVacanciesSearchByVacancy(shared_page):
    print("\nStarting test_RecruitmentPageVacanciesSearchByVacancy transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Will click on Vacancies submenu")
    recruitment_page.click_vacancies_submenu()
    print("Clicked on the Vacancies submenu - will verify that we're on the Vacancies page")
    expect(recruitment_page.vacancies_vacancies_header).to_be_visible(timeout=10000)
    print("Verified that we're on the Vacancies page - will click on the Vacancy dropdown")
    recruitment_page.click_vacancies_search_vacancy_vacancy_dropdown()
    print("Clicked on the Vacancy dropdown - will select Principle QA Test option from the dropdown")
    recruitment_page.select_vacancies_search_vacancy_job_title_principle_qa_test_dropdown_option("Principle QA Test")
    print("Selected Principle QA Test option from the dropdown - will click on Search button")
    recruitment_page.click_vacancies_search_vacancy_search_button()
    print("Clicked on Search button - will verify that records were found")
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible(timeout=10000)
    print("Verified Records Found is visible in the search results")
    print("Ended test_RecruitmentPageVacanciesSearchByVacancy transaction")

def test_RecruitmentPageVacanciesSearchByHiringManager(shared_page):
    print("\nStarting test_RecruitmentPageVacanciesSearchByHiringManager transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Will click on Vacancies submenu")
    recruitment_page.click_vacancies_submenu()
    print("Clicked on the Vacancies submenu - will verify that we're on the Vacancies page")
    expect(recruitment_page.vacancies_vacancies_header).to_be_visible(timeout=10000)
    print("Verified that we're on the Vacancies page - will click on the Hiring Manager dropdown")
    recruitment_page.click_vacancies_search_vacancy_hiring_manager_dropdown()
    print("Clicked on the Hiring Manager dropdown - will select Charles Carter option from the dropdown")
    recruitment_page.select_vacancies_search_vacancy_charles_carter_dropdown_option("Charles Carter")
    print("Selected Charles Carter option from the dropdown - will click on Search button")
    recruitment_page.click_vacancies_search_vacancy_search_button()
    print("Clicked on Search button - will verify that records were found")
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible(timeout=10000)
    print("Verified Records Found is visible in the search results")
    print("Ended test_RecruitmentPageVacanciesSearchByHiringManager transaction")

def test_RecruitmentPageVacanciesSearchByStatus(shared_page):
    print("\nStarting test_RecruitmentPageVacanciesSearchByStatus transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Will click on Vacancies submenu")
    recruitment_page.click_vacancies_submenu()
    print("Clicked on the Vacancies submenu - will verify that we're on the Vacancies page")
    expect(recruitment_page.vacancies_vacancies_header).to_be_visible(timeout=10000)
    print("Verified that we're on the Vacancies page - will click on the Status dropdown")
    recruitment_page.click_vacancies_search_vacancy_status_dropdown()
    print("Clicked on the Status dropdown - will select Active option from the dropdown")
    recruitment_page.select_vacancies_search_vacancy_active_dropdon_option("Active")
    print("Selected Charles Carter option from the dropdown - will click on Search button")
    recruitment_page.click_vacancies_search_vacancy_search_button()
    print("Clicked on Search button - will verify that records were found")
    expect(shared_page.locator("span", has_text=re.compile(r"Records? Found"))).to_be_visible(timeout=10000)
    print("Verified Records Found is visible in the search results")
    print("Ended test_RecruitmentPageVacanciesSearchByStatus transaction")

#def test_RecruitmentPageVacanciesUpdateTestRecord(shared_page):
#    print("\nStarting test_RecruitmentPageVacanciesUpdateTestRecord transaction")
#    recruitment_page = RecruitmentPage(shared_page)
#    print("Will click on Vacancies submenu")
#    recruitment_page.click_vacancies_submenu()
#    print("Clicked on Vacancies submenu - will search for test record")
#    recruitment_page.click_candidates_vacancy_dropdown()
#    print("Clicked on the Vacancy dropdown - will select the test record (Principle QA Test)")
#    recruitment_page.select_vacancies_vacancy_dropdown_test_value()
#    print("Selected the test record - will now click on the Search button")
#    recruitment_page.click_vacancies_search_button()
#    print("Clicked on the Search button - will verify that 1 record was found")
#    expect(recruitment_page.vacancies_vacancy_record_found).to_be_visible(timeout=10000)
#    recruitment_page.click_vacancies_search_result_pencil_icon()
#    print("Clicked on the pencil icon - will verify that we're on the Edit Vacancy page")
#    expect(recruitment_page.vacancies_edit_vacancy_header).to_be_visible(timeout=10000)
#    print("Edit Vacancy header found - will now edit the Description field")
#    recruitment_page.enter_vacancies_vacancy_description("Editing an existing record...")
#    print("Edited the description field - will click on the Save button")
#    recruitment_page.click_vacancies_save_button()
#    print("Clicked on the Save button")
#    expect(recruitment_page.vacancies_successfully_updated_message).to_be_visible(timeout=10000)
#    print("Successfully updated message was displayed")
#    print("Ended test_RecruitmentPageVacanciesUpdateTestRecord transaction")


def test_RecruitmentPageDeleteVacancy(shared_page):
    print("\nStarting test_RecruitmentPageDeleteVacancy transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on the Recruitment menu - will now click on the Vacancies tab")
    recruitment_page.click_vacancies_submenu()
    expect(recruitment_page.vacancies_vacancies_header).to_be_visible(timeout=10000)
    print("Clicked on the vacancies submenu/tab - will now search for the test record that was created")
    recruitment_page.click_vacancies_search_vacancy_job_title_dropdown()
    recruitment_page.select_vacancies_search_vacancy_job_title_dropdown_option("Software Engineer")
    print("Entered the search criteria - will click on the Search button")
    recruitment_page.click_vacancies_search_vacancy_search_button()
    print("Clicked on the Search button - will verify that a record was found")
    expect(recruitment_page.vacancies_search_vacancy_record_found_header).to_be_visible(timeout=10000)
    print("Verified that a record was found - will proceed with the deletion")
    recruitment_page.click_vacancies_delete_vacancy_delete_all_checkbox()
    print("Clicked on the Delete All checkbox - will now click on the Delete Selected button")
    recruitment_page.click_vacancies_delete_vacancy_delete_selected_button()
    print("Clicked on the Delete Selected button - will click on the Yes, Delete confirmation button")
    recruitment_page.click_vacancies_delete_vacancy_confirm_delete_button()
    print("Clicked on the Delete Confirmation button - will verify record has been deleted")
    expect(recruitment_page.vacancies_delete_vacancy_successfully_deleted_message).to_be_visible(timeout=15000)
    print("Verified that the vacancy was successfully deleted message was displayed")
print("\nEnded test_RecruitmentPageDeleteVacancy transaction")

def test_RecruitmentPageDeleteCandidate(shared_page):
    print("\nStarting test_RecruitmentPageDeleteCandidate transaction")
    recruitment_page = RecruitmentPage(shared_page)
    print("Will click on Recruitment menu")
    recruitment_page.click_recruitment_menu()
    print("Clicked on the Recruitment menu - will now click on the Candidates tab")
    recruitment_page.click_candidates_tab()
    expect(recruitment_page.candidates_candidates_header).to_be_visible(timeout=10000)
    print("Verified that we're on the Candidates page - will now search for the test record that was created")
    recruitment_page.click_candidates_search_candidate_candidate_name_field()
    recruitment_page.enter_candidates_search_candidate_candidate_name_field_value("Mike Jones")
    print("Entered the search criteria - will now click on the Search button")
    recruitment_page.click_candidates_search_candidate_search_button()
    print("Clicked on the Search button - will verify that the record is found")
    expect(recruitment_page.candidates_search_candidate_record_found_header).to_be_visible(timeout=10000)
    print("Verified that a record was found - will proceed with the deletion")
    recruitment_page.click_candidates_delete_candidate_delete_all_checkbox()
    print("Clicked on the Delete All checkbox - will now click on the Delete Selected button")
    recruitment_page.click_candidates_delete_candidate_delete_selected_button()
    print("Clicked on the Delete Selected button - will click on the Yes, Delete confirmation button")
    recruitment_page.click_candidates_delete_candidate_confirm_delete_button()
    print("Clicked on the Delete Confirmation button - will verify record has been deleted")
    expect(recruitment_page.candidates_delete_candidate_successfully_deleted_message).to_be_visible(timeout=15000)
    print("Verified that the candidate was successfully deleted message was displayed")
    print("Ended test_RecruitmentPageDeleteCandidate transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

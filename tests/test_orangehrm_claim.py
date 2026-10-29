from datetime import datetime, timedelta
from playwright.sync_api import Page, expect
from conftest import shared_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from pages.claim_page import ClaimPage
from pages.logout_page import LogoutPage
import time

shared_data = {}

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

##########################################################################################################
# PRECONDITION - Start - Create Employee for test
##########################################################################################################

def test_CreateEmployeeForClaimUseCases(shared_page):
    print("\nStarting test_CreateEmployeeForClaimUseCases transaction")
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
    pim_page.enter_pim_employee_add_employee_first_name_field_value("FN_ClaimTest")
    print("Entered the First Name, will now enter the Last Name")
    pim_page.click_pim_employee_add_employee_last_name_field()
    pim_page.enter_pim_employee_add_employee_last_name_field_value("LN_ClaimTest")
    print("Entered the Last Name, will now enter the employee id")
    pim_page.click_pim_employee_add_employee_id_field()
    pim_page.enter_pim_employee_add_employee_id_field_value("3000")
    print("Entered the employee id, will click on the Save button")
    try:
        pim_page.click_pim_employee_add_employee_save_button()
        expect(shared_page.get_by_text("Successfully Saved")).to_be_visible(timeout=10000)
        print("User was successfully created")
    except:
        print("User was NOT created - most likely it already exists")
    print("\nEnded test_CreateEmployeeForClaimUseCases transaction")

##########################################################################################################
# PRECONDITION - End - Create Employee for test
##########################################################################################################

def test_ClaimAssignClaim(shared_page):
    print("\nStarting test_ClaimAssignClaim")
    claim_page = ClaimPage(shared_page)
    print("Will click on the Claim menu")
    claim_page.click_claim_menu()
    print("Clicked on the Claim menu - will verify that we're on the Employee Claims page")
    expect(claim_page.claim_employee_claims_header).to_be_visible(timeout=20000)
    print("Verified that we're on the Employee Claims page - will click on the Assign Claim tab")
    claim_page.click_claim_assign_claim_tab()
    print("Clicked on the Assign Claim tab - will verify that we're on the Create Claim Request page")
    expect(claim_page.claim_assign_claim_create_claim_request_header).to_be_visible(timeout=20000)
    print("Verified that we're on the Create Claim Request page - will enter the Employee Name")
    claim_page.click_claim_assign_claim_create_claim_employee_name_field()
    claim_page.enter_claim_assign_claim_create_claim_employee_name_field_value("FN_ClaimTest LN_ClaimTest")
    print("Entered the employee name - will now select the Event from the Event dropdown")
    claim_page.click_claim_assign_claim_create_claim_event_dropdown()
    claim_page.click_claim_assign_claim_create_claim_event_option()
    print("Selected the Event - will now select the Currency from the Currency dropdown")
    claim_page.click_claim_assign_claim_create_claim_currency_dropdown()
    claim_page.select_claim_assign_claim_create_claim_currency_option()
    print("Selected the Currency - will now enter the Remarks value")
    claim_page.click_claim_assign_claim_create_claim_remarks_field()
    claim_page.enter_claim_assign_claim_create_claim_remarks_field_value("This is a test claim")
    print("Entered the remarks - will now click on the Create button")
    claim_page.click_claim_assign_claim_create_claim_create_button()
    print("Clicked on the Create button - will verify that the Claim has been assigned")
    expect(claim_page.claim_assign_claim_create_claim_successful_message).to_be_visible(timeout=20000)
    print("Verified that the Claim was successfully created")
    reference_id = claim_page.capture_reference_id_from_created_claim()
    shared_data["reference_id"] = reference_id
    print(f"The created claim has the following reference id: {reference_id}")
    print("\nEnded test_ClaimAssignClaim")

def test_ClaimSubmitClaim(shared_page):
    print("\nStarting test_ClaimSubmitClaim")
    claim_page = ClaimPage(shared_page)
    print("Will click on the Claim menu")
    claim_page.click_claim_menu()
    print("Clicked on the Claim menu - will verify that we're on the Employee Claims page")
    expect(claim_page.claim_employee_claims_header).to_be_visible(timeout=20000)
    print("Verified that we're on the Employee Claims page - will search for the record we just created")
    claim_page.click_claim_employee_claims_reference_id_field()
    claim_page.enter_claim_employee_claims_reference_id_field_value(shared_data["reference_id"])
    print("Entered the reference id captured from the claim that was just created - will click on the Search button")
    claim_page.click_claim_employee_claims_search_button()
    print("Clicked on the Search button - will verify that 1 record was found")
    expect(claim_page.claim_employee_claims_record_found_header).to_be_visible(timeout=20000)
    print("Record found header was displayed - will click on the view Details button")
    claim_page.click_claim_employee_claims_view_details_button()
    print("Clicked on the View Details button - will verify that we're on the Assign Claim page")
    expect(claim_page.claim_employee_claims_assign_claim_header).to_be_visible(timeout=20000)
    print("Confirmed that we're on the Assign Claim page - will now click on the Submit button")
    claim_page.click_claim_employee_claims_assign_claim_submit_button()
    print("Clicked on the Submit button - will verify that the Claim was successfully saved")
    expect(claim_page.claim_employee_claims_assign_claim_submit_successful_message).to_be_visible(timeout=20000)
    print("Claim was saved message was displayed - will click on the Back button")
    claim_page.click_claim_employee_claims_assign_claim_back_button()
    print("Clicked on the Back button - will verify that the Status is set to Paid")
    claim_page.click_claim_employee_claims_reference_id_field()
    claim_page.enter_claim_employee_claims_reference_id_field_value(shared_data["reference_id"])
    print("Entered the reference id captured from the claim that was just created - will click on the Search button")
    claim_page.click_claim_employee_claims_search_button()
    print("Clicked on the Search button - will verify that 1 record was found")
    expect(claim_page.claim_employee_claims_record_found_header).to_be_visible(timeout=20000)
    status = claim_page.capture_claim_status()
    assert status == "Paid", f"Expected status Paid but got {status}"
    print("\nEnded test_ClaimSubmitClaim")

def test_DeleteEmployeeForClaimUseCases(shared_page):
    print("\nStarting test_DeleteEmployeeForClaimUseCases transaction")
    pim_page = PIMPage(shared_page)
    pim_page.click_pim_menu()
    print("Clicked PIM menu option")
    expect(shared_page.get_by_role("heading", name="Employee Information"))
    print("Verified Employee Information header")
    pim_page.click_pim_employee_list_employee_name_field()
    pim_page.enter_pim_employee_list_employee_name_field_value("FN_ClaimTest LN_ClaimTest")
    employee_locator = pim_page.get_pim_employee_list_employee_option_by_name("FN_ClaimTest LN_ClaimTest")
    employee_locator.click()
    pim_page.click_pim_employee_list_employee_search_button()
    print("Entered Temporary User into the Employee Name field and clicked Search button")
    expect(shared_page.get_by_text("(1) Record Found")).to_be_visible(timeout=10000)
    print("Verified that record was found")
    pim_page.click_pim_employee_list_delete_employee_checkbox_field()
    print("Clicked on the checkbox associated with the record to delete")
    pim_page.click_pim_employee_list_delete_employee_delete_selected_button()
    print("Clicked on the delete button")
    expect(shared_page.get_by_text("Are you Sure?")).to_be_visible(timeout=10000)
    pim_page.click_pim_reports_delete_report_confirm_button()
    print("Clicked on the confirm delete button")
    expect(shared_page.get_by_text("Successfully deleted")).to_be_visible(timeout=10000)
    print("Verified that the Successfully Deleted toast message was displayed")
    print("\nEnded test_DeleteEmployeeForClaimUseCases transaction")

def test_Logout(shared_page):
    print("\nStarting test_Logout transaction")
    logout_page = LogoutPage(shared_page)
    print("Will click on logout option on the menu")
    logout_page.click_logout()
    print("Clicked on logout option on the menu")
    expect(shared_page.get_by_role("button", name="Login")).to_be_visible(timeout=10000)
    print("Verified Login button is visible on the login page after logout")
    print("Ended test_Logout transaction")

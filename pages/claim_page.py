import time

class ClaimPage:

    def __init__(self, page):
        self.page = page
        self.claim_menu = page.locator("xpath=//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Claim')]")
        self.claim_employee_claims_tab = page.locator("xpath=//a[contains(.,'Employee Claims')]")
        self.claim_configuration_tab = page.locator("xpath=//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'Configuration')]")
        self.claim_confirguration_events_tab = page.locator("xpath=//a[contains(.,'Events')]")
        self.claim_confirguration_expense_types_tab = page.locator("xpath=//a[contains(.,'Expense Types')]")

        # Precondition - Employee Name exists

        #####################################################################################################################
        # Claim - Employee Claims identifiers
        #####################################################################################################################
        self.claim_employee_claims_header  = page.locator("xpath=//h5[contains(.,'Employee Claims')]")

        #####################################################################################################################
        # Claim - Employee Claims - Search identifiers
        #####################################################################################################################
        self.claim_employee_claims_search_button = page.locator("xpath=//button[contains(.,'Search')]")
        self.claim_employee_claims_employee_name_field = page.locator("xpath=(//input[@placeholder='Type for hints...'])[1]")
        self.claim_employee_claims_reference_id_field = page.locator("xpath=(//input[@placeholder='Type for hints...'])[2]")
        self.claim_employee_claims_record_found_header = page.locator("xpath=//span[contains(.,'(1) Record Found')]")
        self.claim_employee_claims_view_details_button = page.locator("xpath=//button[@type='button'][contains(.,'View Details')]")
        self.claim_employee_claims_assign_claim_header = page.locator("xpath=//h6[contains(.,'Assign Claim')]")
        self.claim_employee_claims_assign_claim_submit_button = page.locator("xpath=//button[contains(.,'Submit')]")
        self.claim_employee_claims_assign_claim_submit_successful_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")
        self.claim_employee_claims_assign_claim_back_button = page.locator("xpath=//button[contains(.,'Back')]")
        self.claim_employee_claims_search_result_status_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[7]/div")

        #####################################################################################################################
        # Claim - Employee Claims - Create identifiers
        #####################################################################################################################
        self.claim_employee_claims_submit_claim_button = page.locator("xpath=//button[contains(.,'Submit Claim')]")
        self.claim_employee_claims_create_claim_request_header = page.locator("xpath=//h6[contains(.,'Create Claim Request')]")
        self.claim_employee_claims_create_claim_employee_name_field = page.locator("xpath=//input[@placeholder='Type for hints...']")
        self.claim_employee_claims_create_claim_event_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]")
        self.claim_employee_claims_create_claim_event_option = page.locator("xpath=//span[contains(.,'Medical Reimbursement')]")
        self.claim_employee_claims_create_claim_currency_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]")
        self.claim_employee_claims_create_claim_currency_option = page.locator("xpath=//span[contains(.,'United States Dollar')]")
        self.claim_employee_claims_create_claim_remarks_field = page.locator("xpath=//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
        self.claim_employee_claims_create_claim_create_button = page.locator("xpath=//button[contains(.,'Create')]")
        self.claim_employee_claims_create_claim_successful_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")

        #####################################################################################################################
        # Claim - Assign Claim - Create identifiers
        #####################################################################################################################
        self.claim_assign_claim_tab = page.locator("xpath=//a[contains(.,'Assign Claim')]")
        self.claim_assign_claim_create_claim_request_header = page.locator("xpath=//h6[contains(.,'Create Claim Request')]")
        self.claim_assign_claim_create_claim_employee_name_field = page.locator("xpath=//input[@placeholder='Type for hints...']")
        self.claim_assign_claim_create_claim_event_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]")
        self.claim_assign_claim_create_claim_event_option = page.locator("xpath=//span[contains(.,'Medical Reimbursement')]")
        self.claim_assign_claim_create_claim_currency_dropdown = page.locator("xpath=(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]")
        self.claim_assign_claim_create_claim_currency_option = page.locator("xpath=//span[contains(.,'United States Dollar')]")
        self.claim_assign_claim_create_claim_remarks_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/textarea")
        self.claim_assign_claim_create_claim_create_button = page.locator("xpath=//button[contains(.,'Create')]")
        self.claim_assign_claim_create_claim_successful_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")

        #####################################################################################################################
        # Configuration - Create/Add Events identifiers
        #####################################################################################################################
        self.claim_configuration_events_header = page.locator("xpath=//h5[contains(.,'Events')]")
        self.claim_configuration_events_add_button = page.locator("xpath=//button[contains(.,'Add')]")
        self.claim_configuration_add_event_header = page.locator("xpath=//h6[contains(.,'Add Event')]")
        self.claim_configuration_add_event_name_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input")
        self.claim_configuration_add_event_description_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/textarea")
        self.claim_configuration_add_event_save_button = page.locator("xpath=//button[contains(.,'Save')]")
        self.claim_configuration_add_event_successful_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")

        #####################################################################################################################
        # Configuration - Search/Delete Events identifiers
        #####################################################################################################################
        self.claim_configuration_search_event_event_name_field = page.locator("xpath=//input[@placeholder='Type for hints...']")
        self.claim_configuration_search_event_search_button = page.locator("xpath=//button[contains(.,'Search')]")
        self.claim_configuration_search_event_record_found = page.locator("xpath=//span[contains(.,'(1) Record Found')]")
        self.claim_configuration_search_event_trash_icon = page.locator("xpath=//i[@class='oxd-icon bi-trash']")
        self.claim_configuration_search_event_delete_confirmation_button = page.locator("xpath=//button[contains(.,'Yes, Delete')]")
        self.claim_configuration_delete_event_successful_message = page.locator("xpath=//p[contains(.,'Successfully Deleted')]")
    
    def click_claim_menu(self):
        self.claim_menu.click()

    def click_claim_configuration_tab(self):
        self.claim_configuration_tab.click()

    def click_claim_employee_claims_tab(self):
        self.claim_employee_claims_tab.click()

    def click_claim_confirguration_events_tab(self):
        self.claim_confirguration_events_tab.click()

    def click_claim_confirguration_expense_types_tab(self):
        self.claim_confirguration_expense_types_tab.click()

    #########################################################################################################################
    # Claim - Configuration Events - Add Event Methods
    #########################################################################################################################

    def click_claim_configuration_events_add_button(self):
        self.claim_configuration_events_add_button.click()

    def click_claim_configuration_add_event_name_field(self):
        self.claim_configuration_add_event_name_field.click()

    def enter_claim_configuration_add_event_name_field_value(self, event_name):
        self.claim_configuration_add_event_name_field.fill(event_name)

    def click_claim_configuration_add_event_description_field(self):
        self.claim_configuration_add_event_description_field.click()

    def enter_claim_configuration_add_event_description_field_value(self, event_description):
        self.claim_configuration_add_event_description_field.fill(event_description)

    def click_claim_configuration_add_event_save_button(self):
        self.claim_configuration_add_event_save_button.click()

    #########################################################################################################################
    # Claim - Configuration Events - Delete Event Methods
    #########################################################################################################################

    def click_claim_configuration_search_event_event_name_field(self):
        self.claim_configuration_search_event_event_name_field.click()

    def enter_claim_configuration_search_event_event_name_field_value(self, event_name):
        self.claim_configuration_search_event_event_name_field.fill(event_name)

    def click_claim_configuration_search_event_search_button(self):
        self.claim_configuration_search_event_search_button.click()

    def click_claim_configuration_search_event_trash_icon(self):
        self.claim_configuration_search_event_trash_icon.click()

    def click_claim_configuration_search_event_delete_confirmation_button(self):
        self.claim_configuration_search_event_delete_confirmation_button.click()

    #########################################################################################################################
    # Claim - Search Claim - Search Methods
    #########################################################################################################################
    def click_claim_employee_claims_reference_id_field(self):
        self.claim_employee_claims_reference_id_field.click()

    def enter_claim_employee_claims_reference_id_field_value(self, reference_id):
        self.claim_employee_claims_reference_id_field.fill(reference_id)

    def click_claim_employee_claims_search_button(self):
        self.claim_employee_claims_search_button.click()

    def click_claim_employee_claims_view_details_button(self):
        self.claim_employee_claims_view_details_button.click()

    def click_claim_employee_claims_assign_claim_submit_button(self):
        self.claim_employee_claims_assign_claim_submit_button.click()

    def click_claim_employee_claims_assign_claim_back_button(self):
        self.claim_employee_claims_assign_claim_back_button.click()

    def capture_claim_status(self):
        status = self.claim_employee_claims_search_result_status_field.inner_text().strip()
        return status

    #########################################################################################################################
    # Claim - Assign Claim - Create Methods
    #########################################################################################################################

    def click_claim_assign_claim_tab(self):
        self.claim_assign_claim_tab.click()

    def click_claim_assign_claim_create_claim_employee_name_field(self):
        self.claim_assign_claim_create_claim_employee_name_field.click()

    def enter_claim_assign_claim_create_claim_employee_name_field_value(self, employee_name):
        self.claim_assign_claim_create_claim_employee_name_field.fill(employee_name)
        time.sleep(1)
        self.page.locator("xpath=//span[contains(.,'FN_ClaimTest  LN_ClaimTest')]").click()

    def click_claim_assign_claim_create_claim_event_dropdown(self):
        self.claim_assign_claim_create_claim_event_dropdown.click()

    def click_claim_assign_claim_create_claim_event_option(self):
        self.claim_assign_claim_create_claim_event_option.click()

    def click_claim_assign_claim_create_claim_currency_dropdown(self):
        self.claim_assign_claim_create_claim_currency_dropdown.click()

    def select_claim_assign_claim_create_claim_currency_option(self):
        self.claim_assign_claim_create_claim_currency_option.click()

    def click_claim_assign_claim_create_claim_remarks_field(self):
        self.claim_assign_claim_create_claim_remarks_field.click()

    def enter_claim_assign_claim_create_claim_remarks_field_value(self, remarks):
        self.claim_assign_claim_create_claim_remarks_field.fill(remarks)

    def click_claim_assign_claim_create_claim_create_button(self):
        self.claim_assign_claim_create_claim_create_button.click()

    def capture_reference_id_from_created_claim(self):
        locator = self.page.locator("//label[normalize-space()='Reference Id']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        locator.wait_for(state="visible")
        self.page.wait_for_timeout(1000)

        reference_id = locator.input_value()
        return reference_id
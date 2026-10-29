import time

class ClaimPage:

    def __init__(self, page):
        self.page = page
        self.claim_menu = page.get_by_role("link", name="Claim")
        self.claim_employee_claims_header = page.locator("xpath=//h5[contains(.,'Employee Claims')]")

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

    def click_claim_menu(self):
        self.claim_menu.click()

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
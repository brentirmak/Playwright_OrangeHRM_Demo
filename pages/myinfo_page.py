class MyInfoPage:

    def __init__(self, page):
        self.page = page
        self.myinfo_menu = page.get_by_role("link", name="My Info")
        self.contact_details_submenu = page.get_by_role("link", name="Contact Details")
        self.emergency_contacts_submenu = page.get_by_role("link", name="Emergency Contacts")
        self.dependents_submenu = page.get_by_role("link", name="Dependents")
        self.immigration_submenu = page.get_by_role("link", name="Immigration")
        self.job_submenu = page.get_by_role("link", name="Job")
        self.salary_submenu = page.get_by_role("link", name="Salary")
        self.report_to_submenu = page.get_by_role("link", name="Report-to")
        self.qualifications_submenu = page.get_by_role("link", name="Qualifications")
        self.memberships_submenu = page.get_by_role("link", name="Memberships")
        
        # Personal Details
        self.personal_details_firstname_field = page.locator("//input[@name='firstName']")
        self.personal_details_middlename_field = page.get_by_role("textbox", name="Middle Name")
        self.personal_details_lastname_field = page.locator("//input[@name='lastName']")
        self.personal_details_employeeid_field = page.get_by_role("textbox").nth(4)
        self.personal_details_otherid_field = page.get_by_role("textbox").nth(5)
        self.personal_details_drivers_license_field = page.locator("div:nth-child(2) > div > .oxd-input-group > div:nth-child(2) > .oxd-input")
        self.personal_details_save_button = page.locator("(//button[contains(.,'Save')])[1]")
        
        # Contact Details
        self.contact_details_street1_field = page.get_by_role("textbox").nth(1)
        self.contact_details_street2_field = page.get_by_role("textbox").nth(2)
        self.contact_details_city_field = page.get_by_role("textbox").nth(3)
        self.contact_details_state_field = page.get_by_role("textbox").nth(4)
        self.contact_details_zipcode_field = page.get_by_role("textbox").nth(5)
        self.contact_details_country_dropdown_menu = page.get_by_text("-- Select --")
        self.contact_details_country_dropdown_US_value = page.get_by_role("option", name="United States", exact=True)
        self.contact_details_work_email_field = page.locator("div:nth-child(9) > .oxd-grid-3 > div > .oxd-input-group > div:nth-child(2) > .oxd-input").first
        self.contact_details_save_button = page.get_by_role("button", name="Save")

        # Emergency Contacts
        self.emergency_contacts_header = page.locator("xpath=//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title'][contains(.,'Assigned Emergency Contacts')]")
        self.emergency_contacts_add_button = page.locator("(//button[@type='button'][contains(.,'Add')])[1]")
        self.save_emergency_contact_header = page.locator("xpath=//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title'][contains(.,'Save Emergency Contact')]")
        self.emergency_contact_name_field = page.get_by_role("textbox").nth(1)
        self.emergency_contact_relationship_field = page.get_by_role("textbox").nth(2)
        self.emergency_contact_home_phone_field = page.get_by_role("textbox").nth(3)
        self.emergency_contact_mobile_phone_field = page.get_by_role("textbox").nth(4)
        self.emergency_contact_work_phone_field = page.get_by_role("textbox").nth(5)
        self.emergency_contact_save_button = page.get_by_role("button", name="Save")
        self.emergency_contact_trash_icon = page.locator("//i[contains(@class,'oxd-icon bi-trash')]")
        self.emergency_contact_record_found = page.locator("//span[contains(.,'(1) Record Found')]")
        self.emergency_contact_delete_button = page.locator("//button[@type='button'][contains(.,'Yes, Delete')]")
        self.emergency_contact_successfully_deleted_message = page.locator("//p[contains(.,'Successfully Deleted')]")
        self.emergency_contact_successfully_saved_message = page.locator("//p[contains(.,'Successfully Saved')]")

        # Dependents
        self.dependents_add_dependents_button = page.locator("(//button[@type='button'][contains(.,'Add')])[1]")
        self.dependents_name_field = page.get_by_role("textbox").nth(1)
        self.dependents_relationship_field = page.locator("//div[@class='oxd-select-text-input'][contains(.,'-- Select --')]")
        self.dependents_relationship_child_option = page.get_by_role("option", name="Child")
        self.dependents_date_of_birth_field = page.get_by_role("textbox", name="yyyy-mm-dd")
        self.dependents_date_of_birth_field = page.locator("//input[contains(@placeholder,'yyyy-dd-mm')]")
        self.dependents_save_button = page.get_by_role("button", name="Save")
        self.dependents_successfully_saved_message = page.locator("//p[contains(.,'Successfully Saved')]")
        self.dependents_record_found = page.locator("//span[contains(.,'(1) Record Found')]")
        self.dependents_trash_icon = page.locator("//i[contains(@class,'oxd-icon bi-trash')]")
        self.dependents_delete_button = page.locator("//button[@type='button'][contains(.,'Yes, Delete')]")
        
        self.successfully_updated_message = page.locator("xpath=//p[contains(.,'Successfully Updated')]")
        self.successfully_deleted_message = page.locator("xpath=//p[contains(.,'Successfully Deleted')]")
    
    def click_myinfo_menu(self):
        self.myinfo_menu.click()

    def click_contact_details_submenu(self):
        self.contact_details_submenu.click()

    def click_emergency_contacts_submenu(self):
        self.emergency_contacts_submenu.click()

    def click_dependents_submenu(self):
        self.dependents_submenu.click()

    def click_immigration_submenu(self):
        self.immigration_submenu.click()

    def click_job_submenu(self):
        self.job_submenu.click()

    def click_salary_submenu(self):
        self.salary_submenu.click()

    def click_report_to_submenu(self):
        self.report_to_submenu.click()

    def click_qualifications_submenu(self):
        self.qualifications_submenu.click()
    
    def click_memberships_submenu(self):
        self.memberships_submenu.click()

    ######################################################################################################
    # Personal Details methods
    #
    def click_personal_details_firstname_field(self):
        self.personal_details_firstname_field.click()

    def enter_personal_details_firstname_value(self):
        self.personal_details_firstname_field.fill("John")

    def click_personal_details_middlename_field(self):
        self.personal_details_middlename_field.click()

    def enter_personal_details_middlename_value(self):
        self.personal_details_middlename_field.fill("Mike")

    def click_personal_details_lastname_field(self):
        self.personal_details_lastname_field.click()
    
    def enter_personal_details_lastname_value(self):
        self.personal_details_lastname_field.fill("Doe")

    def click_personal_details_employeeid_field(self):
        self.personal_details_employeeid_field.click()

    def enter_personal_details_employeeid_value(self):
        self.personal_details_employeeid_field.fill("55555")

    def click_personal_details_otherid_field(self):
        self.personal_details_otherid_field.click()

    def enter_personal_details_otherid_value(self):
        self.personal_details_otherid_field.fill("ABCXYZ")

    def click_personal_details_drivers_license_field(self):
        self.personal_details_drivers_license_field.click()

    def enter_personal_details_drivers_license_value(self):
        self.personal_details_drivers_license_field.fill("B12345678")

    def click_personal_details_save_button(self):
        self.personal_details_save_button.click()
    
    ######################################################################################################
    # Contact Details methods
    #
    def click_contact_details_street1_field(self):
        self.contact_details_street1_field.click()

    def enter_contact_details_street1_value(self):
        self.contact_details_street1_field.fill("123 Street Ave")

    def click_contact_details_street2_field(self):
        self.contact_details_street2_field.click()

    def enter_contact_details_street2_value(self):
        self.contact_details_street2_field.fill("Apt 456")

    def click_contact_details_city_field(self):
        self.contact_details_city_field.click()

    def enter_contact_details_city_value(self):
        self.contact_details_city_field.fill("San Jose")

    def click_contact_details_state_field(self):
        self.contact_details_state_field.click()

    def enter_contact_details_state_value(self):
        self.contact_details_state_field.fill("CA")

    def click_contact_details_zipcode_field(self):
        self.contact_details_zipcode_field.click()

    def enter_contact_details_zipcode_value(self):
        self.contact_details_zipcode_field.fill("95112")

    def click_contact_details_country_dropdown_menu(self):
        self.contact_details_country_dropdown_menu.click()

    def select_contact_details_country_dropdown_US_value(self):
        self.contact_details_country_dropdown_US_value.click()

    def click_contact_details_work_email_field(self):
        self.contact_details_work_email_field.click()
            
    def enter_contact_details_work_email_value(self):
        self.contact_details_work_email_field.fill("test@test.com")

    def click_contact_details_save_button(self):
        self.contact_details_save_button.click()

    ######################################################################################################
    # Emergency Contact Details methods
    #
    def click_emergency_contacts_add_button(self):
        self.emergency_contacts_add_button.click()

    def click_emergency_contact_name_field(self):
        self.emergency_contact_name_field.click()

    def enter_emergency_contact_name_value(self):
        self.emergency_contact_name_field.fill("John Smith")

    def click_emergency_contact_relationship_field(self):
        self.emergency_contact_relationship_field.click()
    
    def enter_emergency_contact_relationship_value(self):
        self.emergency_contact_relationship_field.fill("Cousin")

    def click_emergency_contact_home_phone_field(self):
        self.emergency_contact_home_phone_field.click()
    
    def enter_emergency_contact_home_phone_value(self):
        self.emergency_contact_home_phone_field.fill("111-222-3333")

    def click_emergency_contact_mobile_phone_field(self):
        self.emergency_contact_mobile_phone_field.click()
        
    def enter_emergency_contact_mobile_phone_value(self):
        self.emergency_contact_mobile_phone_field.fill("777-666-5555")

    def click_emergency_contact_work_phone_field(self):
        self.emergency_contact_work_phone_field.click()
        
    def enter_emergency_contact_work_phone_value(self):
        self.emergency_contact_work_phone_field.fill("999-888-7777")
    
    def click_emergency_contact_save_button(self):
        self.emergency_contact_save_button.click()

    def click_emergency_contact_trash_icon(self):
        self.emergency_contact_trash_icon.click()

    def click_emergency_contact_delete_button(self):
        self.emergency_contact_delete_button.click()

    ######################################################################################################
    # Dependents methods
    #
    def click_dependents_add_dependents_button(self):
        self.dependents_add_dependents_button.click()

    def click_dependents_name_field(self):
        self.dependents_name_field.click()

    def enter_dependents_name_value(self):
        self.dependents_name_field.fill("Mehmet")

    def click_dependents_relationship_field(self):
        self.dependents_relationship_field.click()

    def click_dependents_relationship_child_option(self):
        self.dependents_relationship_child_option.click()

    def click_dependents_date_of_birth_field(self):
        self.dependents_date_of_birth_field.click()

    def enter_dependents_date_of_birth_value(self):
        self.dependents_date_of_birth_field.fill("1980-11-11")

    def click_dependents_save_button(self):
        self.dependents_save_button.click()

    def click_dependents_trash_icon(self):
        self.dependents_trash_icon.click()

    def click_dependents_delete_button(self):
        self.dependents_delete_button.click()
            
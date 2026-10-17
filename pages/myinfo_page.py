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

        self.successfully_updated_message = page.locator("//p[contains(.,'Successfully Updated')]")
    
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
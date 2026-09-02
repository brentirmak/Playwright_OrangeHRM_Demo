class AdminPage:

    def __init__(self, page):
        self.page = page

        #####################################################################################################################
        # Admin section identifiers
        #####################################################################################################################
        self.admin_menu = page.get_by_role("link", name="Admin")

        #####################################################################################################################
        # User Management section identifiers
        #####################################################################################################################
        self.search_button = page.get_by_role("button", name="Search")
        self.username_field = page.get_by_role("textbox").nth(1)
        self.reset_button = page.get_by_role("button", name="Reset")
        self.user_role_dropdown = page.get_by_text("-- Select --").first
        self.admin_option = page.get_by_role("option", name="Admin")
        self.employee_name_field = page.get_by_role("textbox", name="Type for hints...")
        self.status_dropdown = page.get_by_text("Status-- Select --")
        self.enabled_option = page.get_by_role("option", name="Enabled")
        self.add_button = page.locator("//button[contains(.,'Add')]")
        self.user_role_dropdown = page.locator("(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]")
        self.employee_name_field_suggestion = page.get_by_text("FName Mname LName")
        self.create_username_field = page.get_by_role("textbox").nth(2)
        self.create_password_field = page.get_by_role("textbox").nth(3)
        self.confirm_create_password_field = page.get_by_role("textbox").nth(4)
        self.save_button = page.get_by_role("button", name="Save")
        self.delete_button = page.get_by_role("button", name=" Yes, Delete")

        #####################################################################################################################
        # Job section indentifiers
        #####################################################################################################################
        self.job_submenu = page.get_by_role("listitem").filter(has_text="Job")
        self.job_titles_submenu = page.get_by_role("menuitem", name="Job Titles")
        self.pay_grades_submenu = page.get_by_role("menuitem", name="Pay Grades")
        self.employment_status_submenu = page.get_by_role("menuitem", name="Employment Status")
        self.job_categories_submenu = page.get_by_role("menuitem", name="Job Categories")
        self.work_shifts_submenu = page.get_by_role("menuitem", name="Work Shifts")

        #####################################################################################################################
        # Organization section identifiers
        #####################################################################################################################
        self.organization_submenu = page.get_by_text("Organization")
        self.general_information_submenu = page.get_by_role("menuitem", name="General Information")
        self.locations_submenu = page.get_by_role("menuitem", name="Locations")
        self.structure_submenu = page.get_by_role("menuitem", name="Structure")

        #####################################################################################################################
        # Qualifications section identifiers
        #####################################################################################################################
        self.qualifications_submenu = page.get_by_text("Qualifications")
        self.skills_submenu = page.get_by_role("menuitem", name="Skills")
        self.education_submenu = page.get_by_role("menuitem", name="Education")
        self.licenses_submenu = page.get_by_role("menuitem", name="Licenses")
        self.languages_submenu = page.get_by_role("menuitem", name="Languages")
        self.memberships_submenu = page.get_by_role("menuitem", name="Memberships")

        #####################################################################################################################
        # Nationalities/Corporate Branding section
        #####################################################################################################################
        self.nationalities_submenu = page.get_by_role("link", name="Nationalities")
        self.corporate_branding_submenu = page.get_by_role("link", name="Corporate Branding")

        #####################################################################################################################
        # Configuration section
        #####################################################################################################################
        self.configuration_submenu = page.get_by_role("listitem").filter(has_text="Configuration")
        self.email_configuration_submenu = page.get_by_role("menuitem", name="Email Configuration")
        self.email_subscription_submenu = page.get_by_role("menuitem", name="Email Subscriptions")
        self.localization_submenu = page.get_by_role("menuitem", name="Localization")
        self.language_packages_submenu = page.get_by_role("menuitem", name="Language Packages")
        self.modules_submenu = page.get_by_role("menuitem", name="Modules")
        self.social_media_authentication_submenu = page.get_by_role("menuitem", name="Social Media Authentication")
        self.register_oauth_client_submenu = page.get_by_role("menuitem", name="Register OAuth Client")
        self.ldap_configuration_submenu = page.get_by_role("menuitem", name="LDAP Configuration")

    #####################################################################################################################
    # Admin page/section methods
    #####################################################################################################################
    def click_admin_menu(self):
        self.admin_menu.click()
        self.page.wait_for_load_state("networkidle")
    ################################################

    #####################################################################################################################
    # User Management section methods
    #####################################################################################################################
    def enter_username(self, username):
        self.username_field.fill(username)
        self.page.wait_for_load_state("networkidle")

    def click_search_button(self):
        self.search_button.click()
        self.page.wait_for_load_state("networkidle")

    def click_reset_button(self):
        self.reset_button.click()
        self.page.wait_for_load_state("networkidle")
    
    def click_user_role_dropdown(self):
        self.user_role_dropdown.click()
        self.page.wait_for_load_state("networkidle")
    
    def click_admin_option(self):
        self.admin_option.click()
        self.page.wait_for_load_state("networkidle")

    def click_employee_name_field(self):
        self.employee_name_field.click()
        self.page.wait_for_load_state("networkidle")

    def enter_employee_name(self, employee_name):
        if employee_name == "FName Mname LName":
            self.employee_name_field.fill(employee_name)
            self.page.wait_for_load_state("networkidle")
            self.page.get_by_text(employee_name).click()
            self.page.wait_for_load_state("networkidle")
        else:
            employee_name = "FName Mname LName"
            self.employee_name_field.clear()
            self.employee_name_field.fill(employee_name)
            self.page.wait_for_load_state("networkidle")
            self.page.get_by_text(employee_name).click()
            self.page.wait_for_load_state("networkidle")

    def click_status_dropdown(self):
        self.status_dropdown.click()
        self.page.wait_for_load_state("networkidle")

    def click_enabled_option(self):
        self.enabled_option.click()
        self.page.wait_for_load_state("networkidle")

    def click_add_button(self):
        self.add_button.click()
        self.page.wait_for_load_state("networkidle")

    def click_user_role_dropdown(self):
        self.user_role_dropdown.click()
        self.page.wait_for_load_state("networkidle")

    def click_create_username_field(self):
        self.create_username_field.click()
        self.page.wait_for_load_state("networkidle")

    def enter_create_username(self):
        self.create_username_field.fill("TestUser123")
        self.page.wait_for_load_state("networkidle")

    def click_create_password_field(self):
        self.create_password_field.click()
        self.page.wait_for_load_state("networkidle")

    def enter_create_password(self):
        self.create_password_field.fill("TestUser123")
        self.page.wait_for_load_state("networkidle")

    def click_confirm_create_password_field(self):
        self.confirm_create_password_field.click()
        self.page.wait_for_load_state("networkidle")

    def enter_confirm_create_password(self):
        self.confirm_create_password_field.fill("TestUser123")
        self.page.wait_for_load_state("networkidle")

    def click_save_button(self):
        self.save_button.click()
        self.page.wait_for_load_state("networkidle")

    def click_trashbin_of_tobedeleted_item(self):
        row = self.page.locator("div.oxd-table-card").filter(has_text="TestUser123")
        row.get_by_role("button").filter(has=self.page.locator("i.bi-trash")).click()
        self.page.wait_for_load_state("networkidle")

    def click_delete_button(self):
        self.delete_button.click()
        self.page.wait_for_load_state("networkidle")

    #####################################################################################################################
    # Job section methods
    #####################################################################################################################
    def click_job_submenu(self):
        self.job_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_job_titles_submenu(self):
        self.job_titles_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_pay_grades_submenu(self):
        self.pay_grades_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_employment_status_submenu(self):
        self.employment_status_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_job_categories_submenu(self):
        self.job_categories_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_work_shifts_submenu(self):
        self.work_shifts_submenu.click()
        self.page.wait_for_load_state("networkidle")
    ################################################


    #####################################################################################################################
    # Organization section methods
    #####################################################################################################################
    def click_organization_submenu(self):
        self.organization_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_general_information_submenu(self):
        self.general_information_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_locations_submenu(self):
        self.locations_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_structure_submenu(self):
        self.structure_submenu.click()
        self.page.wait_for_load_state("networkidle")

    #####################################################################################################################
    # Qualifications section methods
    #####################################################################################################################
    def click_qualifications_submenu(self):
        self.qualifications_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_skills_submenu(self):
        self.skills_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_education_submenu(self):
        self.education_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_licenses_submenu(self):
        self.licenses_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_languages_submenu(self):
        self.languages_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_memberships_submenu(self):
        self.memberships_submenu.click()
        self.page.wait_for_load_state("networkidle")

    #####################################################################################################################
    # Nationalities/Corporate Branding section methods
    #####################################################################################################################
    def click_nationalities_submenu(self):
        self.nationalities_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_corporate_branding_submenu(self):
        self.corporate_branding_submenu.click()
        self.page.wait_for_load_state("networkidle")

    #####################################################################################################################
    # Configuration section methods
    #####################################################################################################################
    def click_configuration_submenu(self):
        self.configuration_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_email_configuration_submenu(self):
        self.email_configuration_submenu.click()
        self.page.wait_for_load_state("networkidle")    

    def click_email_subscription_submenu(self):
        self.email_subscription_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_localization_submenu(self):
        self.localization_submenu.click()
        self.page.wait_for_load_state("networkidle")    

    def click_language_packages_submenu(self):
        self.language_packages_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_modules_submenu(self):
        self.modules_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_social_media_authentication_submenu(self):
        self.social_media_authentication_submenu.click()
        self.page.wait_for_load_state("networkidle")
        
    def click_register_oauth_client_submenu(self):
        self.register_oauth_client_submenu.click()
        self.page.wait_for_load_state("networkidle")   

    def click_ldap_configuration_submenu(self):
        self.ldap_configuration_submenu.click()
        self.page.wait_for_load_state("networkidle")    


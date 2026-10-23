import time, re
from playwright.sync_api import Page, expect

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
        self.emergency_contact_trash_icons = page.locator("//i[contains(@class,'oxd-icon bi-trash')]")
        self.emergency_contact_delete_button = page.locator("//button[@type='button'][contains(.,'Yes, Delete')]")
        self.emergency_contact_record_found = page.locator("span", has_text=re.compile(r"\(\d+\) Records? Found"))
        self.emergency_contact_successfully_deleted_message = page.locator("//p[contains(.,'Successfully Deleted')]")
        self.emergency_contact_successfully_saved_message = page.locator("//p[contains(.,'Successfully Saved')]")

        # Dependents
        self.dependents_add_dependents_button = page.locator("(//button[@type='button'][contains(.,'Add')])[1]")
        self.dependents_name_field = page.get_by_role("textbox").nth(1)
        self.dependents_relationship_field = page.locator("//div[@class='oxd-select-text-input'][contains(.,'-- Select --')]")
        self.dependents_relationship_child_option = page.get_by_role("option", name="Child")
        self.dependents_date_of_birth_field_opt1 = page.locator("//input[contains(@placeholder,'dd-mm-yyyy')]")
        self.dependents_date_of_birth_field_opt2 = page.locator("//input[contains(@placeholder,'yyyy-dd-mm')]")
        self.dependents_date_of_birth_clear_button = page.locator("xpath=//div[@class='oxd-date-input-link --clear'][contains(.,'Clear')]")
        self.dependents_save_button = page.get_by_role("button", name="Save")
        self.dependents_successfully_saved_message = page.locator("//p[contains(.,'Successfully Saved')]")
        self.dependents_record_found = page.locator("span", has_text=re.compile(r"\(\d+\) Records? Found"))
        self.dependents_trash_icons = page.locator("//div[contains(@class, 'orangehrm-container')]//i[contains(@class,'oxd-icon bi-trash')]")
        self.dependents_delete_button = page.locator("//button[@type='button'][contains(.,'Yes, Delete')]")

        # Immigration
        self.immigration_add_record_button = page.locator("(//button[@type='button'][contains(.,'Add')])[1]")
        self.add_immigration_header = page.locator("xpath=//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title'][contains(.,'Add Immigration')]")
        self.immigration_document_type_passport_radio_button = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/div/label/span")
        self.immigration_document_type_visa_radio_button = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/div/label/span")
        self.immigration_number_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input")
        self.immigration_issued_date_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input")
        self.immigration_expiry_date_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/div/div/input")
        self.immigration_eligible_status_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/input")
        self.immigration_issued_by_dropdown = page.locator("xpath=//i[contains(@class,'oxd-icon bi-caret-down-fill oxd-select-text--arrow')]")
        self.immigration_eligible_review_date_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[6]/div/div[2]/div/div/input")
        self.immigration_save_button = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]")
        self.immigration_record_successfully_saved = page.locator("xpath=//div[@class='oxd-toast-content oxd-toast-content--success'][contains(.,'SuccessSuccessfully Saved')]")
        self.immigration_documents_trash_icons = page.locator("//div[contains(@class, 'orangehrm-container')]//i[contains(@class,'oxd-icon bi-trash')]")
        self.immigration_assigned_immigration_records_delete_all_checkbox = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span/i")
        self.immigration_delete_selected_button = page.locator("xpath=//button[@type='button'][contains(.,'Delete Selected')]")
        self.immigration_confirm_delete_button = page.locator("xpath=//button[@type='button'][contains(.,'Yes, Delete')]")
        self.immigration_successfully_deleted_message = page.locator("xpath=//p[contains(.,'Successfully Deleted')]")

        # Qualifications - Work Experience
        self.qualifications_work_experience_add_button = page.locator("xpath=(//button[@type='button'][contains(.,'Add')])[1]")
        self.qualifications_work_experience_add_work_experience_header = page.locator("xpath=//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title'][contains(.,'Add Work Experience')]")
        self.qualifications_work_experience_company_field = page.get_by_role("textbox").nth(1)
        self.qualifications_work_experience_job_title_field = page.get_by_role("textbox").nth(2)
        self.qualifications_work_experience_save_button = page.get_by_role("button", name="Save")
        self.qualifications_work_experience_successfully_saved_message = page.locator("xpath=//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text'][contains(.,'Successfully Saved')]")
        self.qualifications_work_experience_record_found = page.locator("span", has_text=re.compile(r"\(\d+\) Records? Found"))
        self.qualifications_work_experience_trash_icons = page.locator("//i[contains(@class,'oxd-icon bi-trash')]")
        self.qualifications_work_experience_delete_selected_button = page.locator("xpath=//button[@type='button'][contains(.,'Delete Selected')]")
        self.qualifications_work_experience_confirm_delete_button = page.locator("xpath=//button[@type='button'][contains(.,'Yes, Delete')]")
        self.qualifications_work_experience_deleted_message = page.locator("//p[contains(.,'Successfully Deleted')]")
        
        # Qualifications - Education
        self.qualifications_education_add_button = page.locator("xpath=(//button[@type='button'][contains(.,'Add')])[2]")
        self.qualifications_add_education_header = page.locator("xpath=//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title'][contains(.,'Add Education')]")
        self.qualifications_add_education_level_dropdown = page.get_by_text("-- Select --")
        self.qualifications_add_education_level_bachleor_degree_option = page.get_by_role("listbox").get_by_text("Bachelor's Degree")
        self.qualifications_add_education_institute_field = page.get_by_role("textbox").nth(1)
        self.qualifications_add_education_major_field = page.get_by_role("textbox").nth(2)
        self.qualifications_add_education_year_field = page.get_by_role("textbox").nth(3)
        self.qualifications_add_education_gpa_field = page.get_by_role("textbox").nth(4)
        self.qualifications_add_education_start_date_field = page.get_by_role("textbox", name="yyyy-dd-mm").first
        self.qualifications_add_education_end_date_field = page.get_by_role("textbox", name="yyyy-dd-mm").nth(1)
        self.qualifications_add_education_save_button = page.get_by_role("button", name="Save")
        self.qualifications_education_successfully_saved_message = page.locator("//p[contains(.,'Successfully Saved')]")

        # Skills
        self.qualifications_skills_add_button = page.locator("xpath=(//button[@type='button'][contains(.,'Add')])[3]")
        self.qualifications_add_skills_header = page.locator("xpath=//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title'][contains(.,'Add Skill')]")
        self.qualifications_add_skill_skill_dropdown = page.locator("xpath=//div[@class='oxd-select-text-input'][contains(.,'-- Select --')]")
        self.qualifications_add_skill_skill_dropdown_content_creation_option = page.locator("xpath=//span[contains(.,'Content Creation')]")
        self.qualifications_add_skill_skill_dropdown_jira_option = page.locator("xpath=//div[@role='option'][contains(.,'JIRA')]")
        self.qualifications_add_skill_skill_dropdown_sql_option = page.locator("xpath=//div[@class='oxd-select-text-input'][contains(.,'SQL')]")
        self.qualifications_add_skill_years_of_experience_field = page.get_by_role("textbox").nth(1)
        self.qualifications_add_skill_comments_field = page.locator("textarea")        
        self.qualifications_add_skill_save_button = page.get_by_role("button", name="Save")
        self.qualifications_skill_successfully_saved_message = page.locator("//p[contains(.,'Successfully Saved')]")
        self.qualifications_skill_delete_selected_button = page.locator("xpath=//button[@type='button'][contains(.,'Delete Selected')]")

        # Languages
        self.qualifications_languages_add_button = page.locator("xpath=(//button[@type='button'][contains(.,'Add')])[4]")
        self.qualifications_add_languages_header = page.locator("xpath=//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title'][contains(.,'Add Language')]")
        self.qualifications_add_language_language_dropdown = page.get_by_text("-- Select --").first
        self.qualifications_add_language_language_spanish_option = page.get_by_role("option", name="Spanish")
        self.qualifications_add_language_fluency_dropdown = page.get_by_text("-- Select --").first
        self.qualifications_add_language_fluency_writing_option = page.get_by_role("option", name="Writing")
        self.qualifications_add_language_competency_dropdown = page.get_by_text("-- Select --").first
        self.qualifications_add_language_competency_mother_tongue_option = page.get_by_role("option", name="Mother Tongue")
        self.qualifications_add_language_save_button = page.get_by_role("button", name="Save")
        self.qualifications_language_successfully_saved_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")
        self.qualifications_languages_delete_selected_button = page.locator("xpath=//button[@type='button'][contains(.,'Delete Selected')]")

        # Licenses
        self.qualifications_licenses_delete_selected_button = page.locator("xpath=//button[@type='button'][contains(.,'Delete Selected')]")

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

    def enter_personal_details_firstname_value(self, firstname):
        self.personal_details_firstname_field.fill(firstname)

    def click_personal_details_middlename_field(self):
        self.personal_details_middlename_field.click()

    def enter_personal_details_middlename_value(self,middlename):
        self.personal_details_middlename_field.fill(middlename)

    def click_personal_details_lastname_field(self):
        self.personal_details_lastname_field.click()
    
    def enter_personal_details_lastname_value(self,lastname):
        self.personal_details_lastname_field.fill(lastname)

    def click_personal_details_employeeid_field(self):
        self.personal_details_employeeid_field.click()

    def enter_personal_details_employeeid_value(self,employeeid):
        self.personal_details_employeeid_field.fill(employeeid)

    def click_personal_details_otherid_field(self):
        self.personal_details_otherid_field.click()

    def enter_personal_details_otherid_value(self,otherid):
        self.personal_details_otherid_field.fill(otherid)

    def click_personal_details_drivers_license_field(self):
        self.personal_details_drivers_license_field.click()

    def enter_personal_details_drivers_license_value(self,license_num):
        self.personal_details_drivers_license_field.fill(license_num)

    def click_personal_details_save_button(self):
        self.personal_details_save_button.click()
    
    ######################################################################################################
    # Contact Details methods
    #
    def click_contact_details_street1_field(self):
        self.contact_details_street1_field.click()

    def enter_contact_details_street1_value(self,street1):
        self.contact_details_street1_field.fill(street1)

    def click_contact_details_street2_field(self):
        self.contact_details_street2_field.click()

    def enter_contact_details_street2_value(self,street2):
        self.contact_details_street2_field.fill(street2)

    def click_contact_details_city_field(self):
        self.contact_details_city_field.click()

    def enter_contact_details_city_value(self,city):
        self.contact_details_city_field.fill(city)

    def click_contact_details_state_field(self):
        self.contact_details_state_field.click()

    def enter_contact_details_state_value(self,state):
        self.contact_details_state_field.fill(state)

    def click_contact_details_zipcode_field(self):
        self.contact_details_zipcode_field.click()

    def enter_contact_details_zipcode_value(self,zipcode):
        self.contact_details_zipcode_field.fill(zipcode)

    def click_contact_details_country_dropdown_menu(self):
        self.contact_details_country_dropdown_menu.click()

    def select_contact_details_country_dropdown_US_value(self):
        self.contact_details_country_dropdown_US_value.click()

    def click_contact_details_work_email_field(self):
        self.contact_details_work_email_field.click()
            
    def enter_contact_details_work_email_value(self, work_email):
        self.contact_details_work_email_field.fill(work_email)

    def click_contact_details_save_button(self):
        self.contact_details_save_button.click()

    ######################################################################################################
    # Emergency Contact Details methods
    #
    def click_emergency_contacts_add_button(self):
        self.emergency_contacts_add_button.click()

    def click_emergency_contact_name_field(self):
        self.emergency_contact_name_field.click()

    def enter_emergency_contact_name_value(self, name):
        self.emergency_contact_name_field.fill(name)

    def click_emergency_contact_relationship_field(self):
        self.emergency_contact_relationship_field.click()
    
    def enter_emergency_contact_relationship_value(self, relationship):
        self.emergency_contact_relationship_field.fill(relationship)

    def click_emergency_contact_home_phone_field(self):
        self.emergency_contact_home_phone_field.click()
    
    def enter_emergency_contact_home_phone_value(self, home_phone):
        self.emergency_contact_home_phone_field.fill(home_phone)

    def click_emergency_contact_mobile_phone_field(self):
        self.emergency_contact_mobile_phone_field.click()
        
    def enter_emergency_contact_mobile_phone_value(self,mobile_phone):
        self.emergency_contact_mobile_phone_field.fill(mobile_phone)

    def click_emergency_contact_work_phone_field(self):
        self.emergency_contact_work_phone_field.click()
        
    def enter_emergency_contact_work_phone_value(self,work_phone):
        self.emergency_contact_work_phone_field.fill(work_phone)
    
    def click_emergency_contact_save_button(self):
        self.emergency_contact_save_button.click()

    def click_emergency_contact_trash_icon(self):
        self.emergency_contact_trash_icons.first.click()

    def click_emergency_contact_delete_button(self):
        self.emergency_contact_delete_button.click()

    ######################################################################################################
    # Dependents methods
    #
    def click_dependents_add_dependents_button(self):
        self.dependents_add_dependents_button.click()

    def click_dependents_name_field(self):
        self.dependents_name_field.click()

    def enter_dependents_name_value(self,name):
        self.dependents_name_field.fill(name)

    def click_dependents_relationship_field(self):
        self.dependents_relationship_field.click()

    def click_dependents_relationship_child_option(self):
        self.dependents_relationship_child_option.click()

    def click_dependents_date_of_birth_field(self, date_format):
        if date_format == "dd-mm-yyyy":
            print("Trying 1st method - dd-mm-yyyy")
            self.dependents_date_of_birth_field_opt1.click()
            print("1st method - dd-mm-yyyy has been clicked.")
        else:
            print("Trying 2nd method - yyyy-dd-mm")
            self.dependents_date_of_birth_field_opt2.click()
            print("2nd method - yyyy-dd-mm has been clicked.")

    def enter_dependents_date_of_birth_value1(self, dob):
        print("Trying 1st method - dd-mm-yyyy")
        self.dependents_date_of_birth_field_opt1.fill(dob)
        print("1st method - dd-mm-yyyy has been entered.")

    def enter_dependents_date_of_birth_value2(self, dob):
        print("Trying 2nd method - yyyy-dd-mm")
        self.dependents_date_of_birth_field_opt2.fill(dob)
        print("2nd method - yyyy-dd-mm has been entered.")

    def click_dependents_save_button(self):
        self.dependents_save_button.click()

    def click_dependents_trash_icon(self):
        self.dependents_trash_icons.first.click()

    def click_dependents_delete_button(self):
        self.dependents_delete_button.click()

    ######################################################################################################
    # Immigration methods
    #
    def click_immigration_add_record_button(self):
        self.immigration_add_record_button.click()

    def click_immigration_document_type_passport_radio_button(self):
        self.immigration_document_type_passport_radio_button.click()

    def click_immigration_document_type_visa_radio_button(self):
        self.immigration_document_type_visa_radio_button.click()

    def click_immigration_number_field(self):
        self.immigration_number_field.click()

    def enter_immigration_number_value(self, immigration_number):
        self.immigration_number_field.fill(immigration_number)

    def click_immigration_issued_date_field(self):
        self.immigration_issued_date_field.click()

    def enter_immigration_issued_date_value(self,immigration_issued_date):
        self.immigration_issued_date_field.fill(immigration_issued_date)

    def click_immigration_expiry_date_field(self):
        self.immigration_expiry_date_field.click()

    def enter_immigration_expiry_date_value(self,expiry_date):
        self.immigration_expiry_date_field.fill(expiry_date)

    def click_immigration_eligible_status_field(self):
        self.immigration_eligible_status_field.click()

    def enter_immigration_eligible_status_value(self,eligible_status):
        self.immigration_eligible_status_field.fill(eligible_status)

    def click_immigration_issued_by_dropdown(self):
        self.immigration_issued_by_dropdown.click()

    def select_immigration_issued_by_value(self, country):
        if country == "United States":
            self.page.locator("//div[@role='listbox']//span[text()='United States']").click()
        else:
            print("Country isn't United States")

    def click_immigration_eligible_review_date_field(self):
        self.immigration_eligible_review_date_field.click()

    def enter_immigration_eligible_review_date_value(self,eligible_review_date):
        self.immigration_eligible_review_date_field.fill(eligible_review_date)

    def click_immigration_save_button(self):
        self.immigration_save_button.click()

    def click_immigration_assigned_immigration_records_delete_all_checkbox(self):
        self.immigration_assigned_immigration_records_delete_all_checkbox.click()

    def delete_immigration_records_by_id(self, record_id):
        matching_rows = self.page.get_by_role("row", name=re.compile(record_id))
        print("Numbers of records to delete: ", matching_rows.count())

        print("Will loop through the number of records to delete them 1 by 1")
        while matching_rows.count() > 0:
            print("Will click on the first item")
            matching_rows.first.locator("//i[contains(@class,'oxd-icon bi-trash')]").click()
            print("Clicked on the first item - will click on the Confirm button")
            self.click_immigration_confirm_delete_button()
            print("Clicked on the Confirm button - verifying success toast")
            success_toast = self.page.locator(".oxd-toast-content--success").first
            expect(success_toast).to_be_visible(timeout=10000)
            success_toast.wait_for(state="hidden", timeout=10000)

    def click_immigration_delete_selected_button(self):
        self.immigration_delete_selected_button.click()

    def click_immigration_confirm_delete_button(self):
        self.immigration_confirm_delete_button.click()


    ######################################################################################################
    # Qualifications - Work Experience methods
    #

    def click_qualifications_work_experience_add_button(self):
        self.qualifications_work_experience_add_button.click()

    def click_qualifications_work_experience_company_field(self):
        self.qualifications_work_experience_company_field.click()

    def enter_qualifications_work_experience_company_value(self, company):
        self.qualifications_work_experience_company_field.fill(company)

    def click_qualifications_work_experience_job_title_field(self):
        self.qualifications_work_experience_job_title_field.click()

    def enter_qualifications_work_experience_job_title_value(self, title):
        self.qualifications_work_experience_job_title_field.fill(title)

    def click_qualifications_work_experience_save_button(self):
        self.qualifications_work_experience_save_button.click()

    def click_qualifications_work_experience_trash_icon(self):
        self.qualifications_work_experience_trash_icons.first.click()

    def click_qualifications_work_experience_delete_selected_button(self):
        self.qualifications_work_experience_delete_selected_button.click()

    def click_qualifications_work_experience_confirm_delete_button(self):
        self.qualifications_work_experience_confirm_delete_button.click()

    def get_qualifications_work_experience_record_count(self):
        record_count_locator = self.page.locator("xpath=(//span[@class='oxd-text oxd-text--span'])[1]")

        record_count_text = record_count_locator.inner_text()
        print(f"Record count text:{record_count_text}")

        record_count = int(re.search(r"\((\d+)\)", record_count_text).group(1))
        print(f"Record count (integer): {record_count}")

        return record_count

    ######################################################################################################
    # Qualifications - Education methods
    #

    def click_qualifications_education_add_button(self):
        self.qualifications_education_add_button.click()

    def click_qualifications_add_education_level_dropdown(self):
        self.qualifications_add_education_level_dropdown.click()

    def select_qualifications_add_education_level_bachleor_degree_option(self):
        self.qualifications_add_education_level_bachleor_degree_option.click()

    def click_qualifications_add_education_institute_field(self):
        self.qualifications_add_education_institute_field.click()

    def enter_qualifications_add_education_institute_value(self):
        self.qualifications_add_education_institute_field.fill("Stanford University")

    def click_qualifications_add_education_major_field(self):
        self.qualifications_add_education_major_field.click()

    def enter_qualifications_add_education_major_value(self):
        self.qualifications_add_education_major_field.fill("Computer Engineering")

    def click_qualifications_add_education_year_field(self):
        self.qualifications_add_education_year_field.click()

    def enter_qualifications_add_education_year_value(self):
        self.qualifications_add_education_year_field.fill("2020")
    
    def click_qualifications_add_education_gpa_field(self):
        self.qualifications_add_education_gpa_field.click()

    def enter_qualifications_add_education_gpa_value(self):
        self.qualifications_add_education_gpa_field.fill("3.8")

    def click_qualifications_add_education_start_date_field(self):
        self.qualifications_add_education_start_date_field.click()

    def enter_qualifications_add_education_start_date_value(self):
        self.qualifications_add_education_start_date_field.fill("2015-09-09")

    def click_qualifications_add_education_end_date_field(self):
        self.qualifications_add_education_end_date_field.click()

    def enter_qualifications_add_education_end_date_value(self):
        self.qualifications_add_education_end_date_field.fill("2020-05-05")

    def click_qualifications_add_education_save_button(self):
        self.qualifications_add_education_save_button.click()

    ######################################################################################################
    # Qualifications - Skills methods
    #

    def click_qualifications_skills_add_button(self):
        self.qualifications_skills_add_button.click()

    def click_qualifications_add_skill_skill_dropdown(self):
        self.qualifications_add_skill_skill_dropdown.click()

    def select_qualifications_add_skill_skill_dropdown_content_creation_option(self):
        self.qualifications_add_skill_skill_dropdown_content_creation_option.click()

    def select_qualifications_add_skill_skill_dropdown_jira_option(self):
        self.qualifications_add_skill_skill_dropdown_jira_option.click()

    def select_qualifications_add_skill_skill_dropdown_sql_option(self):
        self.qualifications_add_skill_skill_dropdown_sql_option.click()

    def click_qualifications_add_skill_years_of_experience_field(self):
        self.qualifications_add_skill_years_of_experience_field.click()

    def enter_qualifications_add_skill_years_of_experience_value(self,yrs):
        self.qualifications_add_skill_years_of_experience_field.fill(yrs)

    def click_qualifications_add_skill_comments_field(self):
        self.qualifications_add_skill_comments_field.click()

    def enter_qualifications_add_skill_comments_value(self, comment):
        self.qualifications_add_skill_comments_field.fill(comment)

    def click_qualifications_add_skill_save_button(self):
        self.qualifications_add_skill_save_button.click()

    def delete_qualifications_by_skill_name(self, skill_name):
        row = self.page.locator(f"xpath=//h6[text()='Skills']/following::div[@class='orangehrm-container'][1]//div[@role='row'][.//*[text()='{skill_name}']]")
        row.locator("button i.bi-trash").click()
        self.page.get_by_role("button", name="Yes, Delete").click()

    def delete_qualifications_skill_delete_selected_button(self):
        self.qualifications_skill_delete_selected_button.click()

    ######################################################################################################
    # Qualifications - Languages methods
    #
    def click_qualifications_languages_add_button(self):
        self.qualifications_languages_add_button.click()

    def click_qualifications_add_language_language_dropdown(self):
        self.qualifications_add_language_language_dropdown.click()

    def select_qualifications_add_language_spanish_option(self):
        self.qualifications_add_language_language_spanish_option.click()

    def click_qualifications_add_language_fluency_dropdown(self):
        self.qualifications_add_language_fluency_dropdown.click()

    def select_qualifications_add_language_fluency_writing_option(self):
        self.qualifications_add_language_fluency_writing_option.click()

    def click_qualifications_add_language_competency_dropdown(self):
        self.qualifications_add_language_competency_dropdown.click()

    def select_qualification_add_language_competency_mother_tongue_option(self):
        self.qualifications_add_language_competency_mother_tongue_option.click()

    def click_qualifications_add_language_save_button(self):
        self.qualifications_add_language_save_button.click()

    def click_qualifications_languages_delete_selected_button(self):
        self.qualifications_languages_delete_selected_button.click()

    def delete_qualifications_by_language_name(self, language_name):
        row = self.page.locator(f"xpath=//h6[text()='Languages']/following::div[@class='orangehrm-container'][1]//div[@role='row'][.//*[text()='{language_name}']]")
        row.locator("button i.bi-trash").click()
        self.page.get_by_role("button", name="Yes, Delete").click()

    ######################################################################################################
    # Qualifications - License Type methods
    #

    def click_qualifications_licenses_delete_selected_button(self):
        self.qualifications_licenses_delete_selected_button.click()
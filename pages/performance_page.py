import re

class PerformancePage:

    def __init__(self, page):
        
        self.page = page
        
        ########################################################################################################################################
        # Performance - Menu/Tab Options
        ########################################################################################################################################
        self.performance_menu = page.get_by_role("link", name="Performance")
        self.performance_configure_submenu = page.locator("//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'Configure')]")
        self.performance_configure_kpis_submenu = page.get_by_role("listitem").filter(has_text=re.compile(r"^KPIs$"))
        self.performance_configure_trackers_submenu = page.get_by_role("menuitem", name="Trackers")
        self.performance_manage_reviews_submenu = page.locator("xpath=//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'Manage Reviews')]")
        self.performance_manage_reviews_manage_reviews_submenu = page.locator("xpath=//a[contains(.,'Manage Reviews')]")
        self.performance_manage_reviews_myreviews_submenu = page.locator("xpath=//a[contains(.,'My Reviews')]")
        self.performance_manage_reviews_employee_reviews_submenu = page.get_by_role("menuitem", name="Employee Reviews")
        self.performance_my_trackers_submenu = page.locator("//a[@class='oxd-topbar-body-nav-tab-item'][contains(.,'My Trackers')]")
        self.performance_employee_trackers_submenu = page.get_by_role("link", name="Employee Trackers")

        ########################################################################################################################################
        # Performance - Configure KPI section/page
        ########################################################################################################################################
        # Search
        self.performance_configure_kpis_job_title_dropdown = page.get_by_text("-- Select --")
        self.performance_configure_kpis_job_title_qa_lead_option = page.get_by_role("listbox").get_by_text("QA Lead")
        self.performance_configure_kpis_job_title_search_button = page.get_by_role("button", name="Search")
        
        # Add
        self.performance_configure_kpis_add_button = page.locator("xpath=//button[contains(.,'Add')]")
        self.performance_configure_kpis_add_kpi_header = page.locator("xpath=//p[contains(.,'Add Key Performance Indicator')]")
        self.performance_configure_kpis_add_kpi_name_field = page.locator("xpath=/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input")
        self.performance_configure_kpis_add_kpi_job_title_dropdown = page.locator("xpath=//i[contains(@class,'oxd-icon bi-caret-down-fill oxd-select-text--arrow')]")
        self.performance_configure_kpis_add_kpi_job_title_software_engineer_option = page.locator("xpath=//span[contains(.,'Software Engineer')]")
        self.performance_configure_kpis_add_kpi_job_title_save_button = page.locator("xpath=//button[contains(.,'Save')]")
        self.performance_configure_kpis_add_kpi_successfully_saved_message = page.locator("xpath=//p[contains(.,'Successfully Saved')]")

        ########################################################################################################################################
        # Performance - Configure Trackers section/page
        ########################################################################################################################################
        self.performance_configure_trackers_performance_header = page.locator("xpath=//h5[@class='oxd-text oxd-text--h5 oxd-table-filter-title'][contains(.,'Performance Trackers')]")
        self.performance_configure_trackers_performance_tracker_employee_name_field = page.locator("xpath=//input[@placeholder='Type for hints...']")
        self.performance_configure_trackers_performance_tracker_search_button = page.get_by_role("button", name="Search")

        # Add Tracker identifier
        self.performance_configure_trackers_performance_tracker_add_button = page.locator("xpath=//button[@type='button'][contains(.,'Add')]")

        ########################################################################################################################################
        # Performance - Manage Reviews section/page
        #
        self.performance_manage_reviews_employee_reviews_header = page.locator("xpath=//h5[contains(.,'Employee Reviews')]")

    ########################################################################################################################################
    # Performance - Menu/Tab Options Methods
    ########################################################################################################################################
    def click_performance_menu(self):
        self.performance_menu.click()

    def click_performance_configure_submenu(self):
        self.performance_configure_submenu.click()

    def click_performance_configure_kpis_submenu(self):
        self.performance_configure_kpis_submenu.click()

    def click_performance_configure_trackers_submenu(self):
        self.performance_configure_trackers_submenu.click()

    def click_performance_manage_reviews_submenu(self):
        self.performance_manage_reviews_submenu.click()

    def click_performance_manage_reviews_manage_reviews_submenu(self):
        self.performance_manage_reviews_manage_reviews_submenu.click()

    def click_performance_manage_reviews_myreviews_submenu(self):
        self.performance_manage_reviews_myreviews_submenu.click()

    def click_performance_manage_reviews_employee_reviews_submenu(self):
        self.performance_manage_reviews_employee_reviews_submenu.click()

    def click_performance_my_trackers_submenu(self):
        self.performance_my_trackers_submenu.click()

    def click_performance_employee_trackers_submenu(self):
        self.performance_employee_trackers_submenu.click()

    ########################################################################################################################################
    # Performance - Configure KPI section/page Methods
    ########################################################################################################################################
    # Search
    def click_performance_configure_kpis_job_title_dropdown(self):
        self.performance_configure_kpis_job_title_dropdown.click()

    def click_performance_configure_kpis_job_title_qa_lead_option(self):
        self.performance_configure_kpis_job_title_qa_lead_option.click()

    def click_performance_configure_kpis_job_title_search_button(self):
        self.performance_configure_kpis_job_title_search_button.click()

    # Add
    def click_performance_configure_kpis_add_button(self):
        self.performance_configure_kpis_add_button.click()

    def click_performance_configure_kpis_add_kpi_name_field(self):
        self.performance_configure_kpis_add_kpi_name_field.click()

    def enter_performance_configure_kpis_add_kpi_name_field_value(self, kpi_name):
        self.performance_configure_kpis_add_kpi_name_field.fill(kpi_name)

    def click_performance_configure_kpis_add_kpi_job_title_dropdown(self):
        self.performance_configure_kpis_add_kpi_job_title_dropdown.click()

    def select_performance_configure_kpis_add_kpi_job_title_value(self):
        self.performance_configure_kpis_add_kpi_job_title_software_engineer_option.click()

    def click_performance_configure_kpis_add_kpi_job_title_save_button(self):
        self.performance_configure_kpis_add_kpi_job_title_save_button.click()







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
        self.performance_configure_kpis_job_title_dropdown = page.get_by_text("-- Select --")
        self.performance_configure_kpis_job_title_qa_lead_option = page.get_by_role("listbox").get_by_text("QA Lead")
        self.performance_configure_kpis_job_title_search_button = page.get_by_role("button", name="Search")

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
    def click_performance_configure_kpis_job_title_dropdown(self):
        self.performance_configure_kpis_job_title_dropdown.click()

    def click_performance_configure_kpis_job_title_qa_lead_option(self):
        self.performance_configure_kpis_job_title_qa_lead_option.click()

    def click_performance_configure_kpis_job_title_search_button(self):
        self.performance_configure_kpis_job_title_search_button.click()







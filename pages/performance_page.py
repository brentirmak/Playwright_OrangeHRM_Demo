import re

class PerformancePage:

    def __init__(self, page):
        self.page = page
        self.performance_menu = page.get_by_role("link", name="Performance")
        self.configure_submenu = page.locator("//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'Configure')]")
        self.configure_kpis_submenu = page.get_by_role("listitem").filter(has_text=re.compile(r"^KPIs$"))
        self.job_title_dropdown = page.get_by_text("-- Select --")
        self.qa_lead_option = page.get_by_role("listbox").get_by_text("QA Lead")
        self.search_button = page.get_by_role("button", name="Search")
        self.trackers_submenu = page.get_by_role("menuitem", name="Trackers")
        self.manage_reviews_submenu = page.locator("//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'Manage Reviews')]")
        self.manage_reviews_manage_reviews_submenu = page.locator("//a[contains(.,'Manage Reviews')]")
        self.my_reviews_submenu = page.get_by_role("menuitem", name="My Reviews")
        self.employee_reviews_submenu = page.get_by_role("menuitem", name="Employee Reviews")
        self.my_trackers_submenu = page.locator("//a[@class='oxd-topbar-body-nav-tab-item'][contains(.,'My Trackers')]")
        self.employee_trackers_submenu = page.get_by_role("link", name="Employee Trackers")

    def click_performance_menu(self):
        self.performance_menu.click()

    def click_configure_submenu(self):
        self.configure_submenu.click()

    def click_configure_kpis_submenu(self):
        self.configure_kpis_submenu.click()

    def click_job_title_dropdown(self):
        self.job_title_dropdown.click()

    def click_qa_lead_option(self):
        self.qa_lead_option.click()

    def click_search_button(self):
        self.search_button.click()

    def click_trackers_submenu(self):
        self.trackers_submenu.click()

    def click_manage_reviews_submenu(self):
        self.manage_reviews_submenu.click()

    def click_manage_reviews_manage_reviews_submenu(self):
        self.manage_reviews_manage_reviews_submenu.click()

    def click_my_reviews_submenu(self):
        self.my_reviews_submenu.click()

    def click_employee_reviews_submenu(self):
        self.employee_reviews_submenu.click()

    def click_my_trackers_submenu(self):
        self.my_trackers_submenu.click()

    def click_employee_trackers_submenu(self):
        self.employee_trackers_submenu.click()

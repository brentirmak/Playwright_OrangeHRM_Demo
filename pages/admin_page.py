class AdminPage:

    def __init__(self, page):
        self.page = page

        # Admin section
        self.admin_menu = page.get_by_role("link", name="Admin")

        # User Management section
        self.search_button = page.get_by_role("button", name="Search")
        self.username_field = page.get_by_role("textbox").nth(1)
        self.reset_button = page.get_by_role("button", name="Reset")
        self.user_role_dropdown = page.get_by_text("-- Select --").first
        self.admin_option = page.get_by_role("option", name="Admin")
        self.employee_name_field = page.get_by_role("textbox", name="Type for hints...")
        

        # Job section
        self.job_submenu = page.get_by_role("listitem").filter(has_text="Job")
        self.job_titles_submenu = page.get_by_role("menuitem", name="Job Titles")
        self.pay_grades_submenu = page.get_by_role("menuitem", name="Pay Grades")
        self.employment_status_submenu = page.get_by_role("menuitem", name="Employment Status")
        self.job_categories_submenu = page.get_by_role("menuitem", name="Job Categories")
        self.work_shifts_submenu = page.get_by_role("menuitem", name="Work Shifts")

    ################################################
    # Admin page/section methods
    def click_admin_menu(self):
        self.admin_menu.click()
        self.page.wait_for_load_state("networkidle")
    ################################################

    ################################################
    # User Management section methods
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
        self.employee_name_field.fill(employee_name)
        self.page.wait_for_load_state("networkidle")
    ################################################

    ################################################
    # Job section methods
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

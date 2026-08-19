class AdminPage:

    def __init__(self, page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.search_button = page.get_by_role("button", name="Search")
        self.username_field = page.get_by_role("textbox").nth(1)
        self.job_submenu = page.get_by_text("Job", exact=True)
        self.job_titles_submenu = page.get_by_role("menuitem", name="Job Titles")

    def click_admin_menu(self):
        self.admin_menu.click()
        self.page.wait_for_load_state("networkidle")

    def enter_username(self, username):
        self.username_field.fill(username)
        self.page.wait_for_load_state("networkidle")

    def click_search_button(self):
        self.search_button.click()
        self.page.wait_for_load_state("networkidle")

    def click_job_submenu(self):
        self.job_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def click_job_titles_submenu(self):
        self.job_titles_submenu.click()
        self.page.wait_for_load_state("networkidle")

    '''
    page.get_by_text("Job", exact=True).click()
    page.get_by_role("menuitem", name="Job Titles").click()
    expect(page.get_by_role("heading", name="Job Titles")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Job Description")).to_be_visible()
    expect(page.get_by_text("Automaton Tester")).to_be_visible()
    page.get_by_role("listitem").filter(has_text="Job").locator("i").click()
    page.get_by_role("menuitem", name="Pay Grades").click()
    expect(page.get_by_role("heading", name="Pay Grades")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Currency")).to_be_visible()
    expect(page.get_by_text("United States Dollar").first).to_be_visible()
    page.get_by_role("listitem").filter(has_text="Job").click()
    page.get_by_role("menuitem", name="Employment Status").click()
    expect(page.get_by_role("heading", name="Employment Status")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Employment Status")).to_be_visible()
    expect(page.get_by_text("Full-Time Permanent")).to_be_visible()
    page.get_by_label("Topbar Menu").get_by_text("Job").click()
    page.get_by_role("menuitem", name="Job Categories").click()
    expect(page.get_by_role("heading", name="Job Categories")).to_be_visible()
    expect(page.get_by_role("columnheader", name="Job Category")).to_be_visible()
    expect(page.get_by_text("Officials and Managers")).to_be_visible()
    page.get_by_label("Topbar Menu").get_by_text("Job").click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^Work Shifts$")).click()
    expect(page.get_by_role("heading", name="Work Shifts")).to_be_visible()
    page.get_by_role("columnheader", name="Hours Per Day").click()
    page.get_by_text("General").click()
    '''
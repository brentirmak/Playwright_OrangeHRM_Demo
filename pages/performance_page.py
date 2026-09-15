import re

class PerformancePage:

    def __init__(self, page):
        self.page = page
        self.performance_menu = page.get_by_role("link", name="Performance")

        #self.configure_submenu = page.get_by_text("Configure")
        self.configure_submenu = page.locator("//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'Configure')]")



        self.configure_kpis_submenu = page.get_by_role("listitem").filter(has_text=re.compile(r"^KPIs$"))

        self.trackers_submenu = page.get_by_role("menuitem", name="Trackers")

        self.manage_reviews_submenu = page.get_by_role("menuitem", name="Manage Reviews")
        self.manage_reviews_manage_reviews_submenu = page.get_by_label("Topbar Menu").get_by_text("Manage Reviews")
        self.my_reviews_submenu = page.get_by_role("menuitem", name="My Reviews")
        self.employee_reviews_submenu = page.get_by_role("menuitem", name="Employee Reviews")
        self.my_trackers_submenu = page.get_by_role("link", name="My Trackers")
        self.employee_trackers_submenu = page.get_by_role("link", name="Employee Trackers")

    def click_performance_menu(self):
        self.performance_menu.click()

    def click_configure_submenu(self):
        self.configure_submenu.click()

    def click_configure_kpis_submenu(self):
        self.configure_kpis_submenu.click()

    def click_trackers_submenu(self):
        self.trackers_submenu.click()

    def click_manage_reviews_submenu(self):
        self.manage_reviews_submenu.click()

    def click_my_reviews_submenu(self):
        self.my_reviews_submenu.click()

    def click_employee_reviews_submenu(self):
        self.employee_reviews_submenu.click()

    def click_my_trackers_submenu(self):
        self.my_trackers_submenu.click()

    def click_employee_trackers_submenu(self):
        self.employee_trackers_submenu.click()


'''
    page.get_by_role("link", name="Performance").click()
    expect(page.locator("div").filter(has_text=re.compile(r"^PerformanceManage Reviews$"))).to_be_visible()
    expect(page.get_by_role("heading", name="Employee Reviews")).to_be_visible()
    page.get_by_text("Configure").click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^KPIs$")).click()
    expect(page.get_by_role("heading", name="Key Performance Indicators")).to_be_visible()
    page.get_by_text("-- Select --").click()
    page.get_by_role("listbox").get_by_text("QA Lead").click()
    page.get_by_role("button", name="Search").click()
    expect(page.get_by_text("(5) Records Found")).to_be_visible()
    expect(page.get_by_text("QA Lead").nth(1)).to_be_visible()
    page.get_by_label("Topbar Menu").get_by_text("Configure").click()
    page.get_by_role("menuitem", name="Trackers").click()
    expect(page.get_by_role("heading", name="Performance Trackers")).to_be_visible()
    page.get_by_text("Manage Reviews").click()
    page.get_by_role("menuitem", name="Manage Reviews").click()
    expect(page.get_by_role("heading", name="Manage Performance Reviews")).to_be_visible()
    page.get_by_label("Topbar Menu").get_by_text("Manage Reviews").click()
    page.get_by_role("menuitem", name="My Reviews").click()
    expect(page.get_by_role("heading", name="My Reviews")).to_be_visible()
    page.get_by_label("Topbar Menu").get_by_text("Manage Reviews").click()
    page.get_by_role("menuitem", name="Employee Reviews").click()
    expect(page.get_by_role("heading", name="Employee Reviews")).to_be_visible()
    page.get_by_role("link", name="My Trackers").click()
    expect(page.get_by_role("heading", name="My Performance Trackers")).to_be_visible()
    page.get_by_role("link", name="Employee Trackers").click()
    expect(page.get_by_role("heading", name="Employee Performance Trackers")).to_be_visible()

'''
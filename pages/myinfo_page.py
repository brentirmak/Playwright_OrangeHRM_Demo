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

    
    '''
    page.get_by_role("link", name="Contact Details").click()
                expect(page.get_by_role("heading", name="Contact Details")).to_be_visible()
    
    expect(page.get_by_role("heading", name="Attachments")).to_be_visible()
                page.get_by_role("link", name="Emergency Contacts").click()
    
    expect(page.get_by_role("heading", name="Assigned Emergency Contacts")).to_be_visible()
    expect(page.get_by_role("heading", name="Attachments")).to_be_visible()
                page.get_by_role("link", name="Dependents").click()
    
    expect(page.get_by_role("heading", name="Assigned Dependents")).to_be_visible()
    expect(page.get_by_role("heading", name="Attachments")).to_be_visible()
                page.get_by_role("link", name="Immigration").click()

    expect(page.get_by_role("heading", name="Assigned Immigration Records")).to_be_visible()
    expect(page.get_by_role("heading", name="Attachments")).to_be_visible()
    page.get_by_role("link", name="Job").click()
    expect(page.get_by_role("heading", name="Job Details")).to_be_visible()
    expect(page.get_by_role("heading", name="Attachments")).to_be_visible()
    page.get_by_role("link", name="Salary").click()
    expect(page.get_by_role("heading", name="Assigned Salary Components")).to_be_visible()
    page.get_by_role("heading", name="Attachments").click()
    page.get_by_role("link", name="Report-to").click()
    expect(page.get_by_role("heading", name="Report to")).to_be_visible()
    expect(page.get_by_role("heading", name="Assigned Subordinates")).to_be_visible()
    expect(page.get_by_role("heading", name="Attachments")).to_be_visible()
    page.get_by_role("link", name="Qualifications").click()
    expect(page.get_by_role("heading", name="Qualifications")).to_be_visible()
    expect(page.get_by_role("heading", name="Work Experience")).to_be_visible()
    expect(page.get_by_role("heading", name="Education")).to_be_visible()
    page.get_by_role("link", name="Memberships").click()
    expect(page.get_by_role("heading", name="Assigned Memberships")).to_be_visible()
    expect(page.get_by_role("heading", name="Attachments")).to_be_visible()
    '''





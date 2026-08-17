class ClaimPage:

    def __init__(self, page):
        self.page = page
        self.claim_menu = page.get_by_role("link", name="Claim")

    def click_claim_menu(self):
        self.claim_menu.click()
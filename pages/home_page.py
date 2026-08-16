from playwright.sync_api import expect

class HomePage:

    def __init__(self, page):
        self.page = page
        self.brandingImage = page.get_by_alt_text('company-branding');

    def verify_branding_image_visible(self):
        expect(self.brandingImage).to_be_visible()

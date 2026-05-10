from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page=page
        self.dropdown=page.locator(".oxd-icon.bi-caret-down-fill.oxd-userdropdown-icon")
        self.recruitment=page.get_by_role("link", name="Recruitment")
        self.logout=page.get_by_role("menuitem", name="Logout")
        
    def click_dropdown(self):
        self.dropdown.click()
        
    def click_recruitment(self):
        self.recruitment.click()
        
    def click_logout(self):
        self.dropdown.click()
        self.logout.click()
        
    
    
    
    
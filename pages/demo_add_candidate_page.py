from playwright.sync_api import Page

class AddCandidate:
    
    def __init__(self, page: Page):
        self.first_name=page.get_by_role("textbox", name="First Name")
        self.last_name=page.get_by_role("textbox", name="Last Name")
        self.email=page.get_by_role("textbox", name="Type here").nth(0)
        self.save_button=page.get_by_role("button", name="Save")
        
    def enter_first_name(self, firstname):
        self.first_name.fill(firstname)
    
    def enter_last_name(self, lastname):
        self.last_name.fill(lastname)
    
    def enter_email(self,mail):
        self.email.fill(mail)
        
    def click_save(self):
        self.save_button.click()
    
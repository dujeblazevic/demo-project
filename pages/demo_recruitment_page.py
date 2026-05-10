from playwright.sync_api import Page

class RecruitmentPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.candidate_name = page.get_by_role("textbox", name="Type for hints...")
        self.search_button = page.get_by_role("button", name="Search")
        self.add_button = page.get_by_role("button", name="Add")
    
    def search_by_name(self, cand_name):
        name_input = self.page.get_by_role("textbox", name="Type for hints...")
        name_input.fill(cand_name)
        self.page.get_by_role("option", name=cand_name).first.click()
        
    def search(self):
        self.search_button.click()
    
    def add(self):
        self.add_button.click()
    
    
from playwright.sync_api import Page, expect
from pages.demo_home_page import HomePage
from pages.demo_login_page import LoginPage

def test_home(page: Page):
    login_page=LoginPage(page)
    home_page=HomePage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    home_page.click_dropdown()
    expect(page.get_by_role("menuitem", name="About")).to_be_visible()
    expect(page.get_by_role("menuitem", name="Support")).to_be_visible()
    expect(page.get_by_role("menuitem", name="Change Password")).to_be_visible()
    expect(page.get_by_role("menuitem", name="Logout")).to_be_visible()
    home_page.click_recruitment()
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
    
    
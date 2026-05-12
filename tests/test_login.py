from playwright.sync_api import Page, expect
from pages.demo_login_page import LoginPage

def test_login(page: Page):
    login_page=LoginPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.click_login()
    expect(page.get_by_text("Required").nth(0)).to_be_visible()
    expect(page.get_by_text("Required").nth(1)).to_be_visible()
    login_page.enter_username("Admin")
    login_page.enter_password("admin1234")
    login_page.click_login()
    expect(page.get_by_role("alert").filter(has_text="Invalid credentials")).to_be_visible()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    
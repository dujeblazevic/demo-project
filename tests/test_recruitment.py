from playwright.sync_api import Page, expect
from pages.demo_home_page import HomePage
from pages.demo_login_page import LoginPage
from pages.demo_recruitment_page import RecruitmentPage
from pages.demo_add_candidate_page import AddCandidate

def test_recruitment(page: Page):
    login_page=LoginPage(page)
    home_page=HomePage(page)
    recruitment_page=RecruitmentPage(page)
    add_candidate=AddCandidate(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    home_page.click_recruitment()
    recruitment_page.add()
    add_candidate.enter_first_name("Branimir")
    add_candidate.enter_last_name("Kovacevic")
    add_candidate.enter_email("branimir@example.com")
    add_candidate.click_save()
    home_page.click_recruitment()
    recruitment_page.search_by_name("Branimir")
    recruitment_page.search()
    expect(page.get_by_text("(1) Record Found")).to_be_visible()

    
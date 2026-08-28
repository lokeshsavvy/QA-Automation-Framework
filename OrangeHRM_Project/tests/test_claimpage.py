from OrangeHRM_Project.pages.loginpage import LoginPage
from OrangeHRM_Project.pages.claimpage import ClaimPage

def test_create_claim(driver):

    login = LoginPage(driver)
    claim = ClaimPage(driver)

    login.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")

    claim.click_claim()
    claim.click_create_claim()
    claim.enter_employee_name("Amelia Brown")
    claim.click_event()
    claim.click_currency()
    claim.enter_remarks("Medical claim")
    claim.create_claim()
    claim.add_expenses()
    claim.click_expense_type()
    claim.enter_date("2026-27-08")
    claim.enter_amount("5000")
    claim.enter_note("Medical Claim")
    claim.click_save()
    assert claim.is_expence_record_displayed()

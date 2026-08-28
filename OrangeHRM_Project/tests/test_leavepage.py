from OrangeHRM_Project.pages.loginpage import LoginPage
from OrangeHRM_Project.pages.leavepage import LeavePage

def test_assign_leave(driver):

    login = LoginPage(driver)
    leave = LeavePage(driver)
    login.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login.login("Admin", "admin123")

    leave.click_leave()
    leave.click_assign_leave()
    leave.enter_employee_name("Charlotte Smith")
    leave.select_leave_type()
    leave.enter_from_date("2026-08-27")
    leave.enter_to_date("2026-08-28")
    leave.select_partial()
    leave.select_duration()
    leave.enter_comments("Personal Leave")
    leave.click_assign()
    assert leave.is_confirm_popup_displayed()
    leave.click_ok()

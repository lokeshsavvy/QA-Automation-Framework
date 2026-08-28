

from OrangeHRM_Project.pages.adminpage import AdminPage
from OrangeHRM_Project.pages.loginpage import LoginPage
import time

def test_add_new_user(driver):

    login = LoginPage(driver)
    admin = AdminPage(driver)

    login.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login.login("Admin","admin123")

    admin.click_admin()
    admin.click_add()
    admin.select_user_role()
    admin.enter_employee_name("Ranga Akunuri")
    admin.select_status()
    admin.enter_user_name("loki12345")
    admin.enter_password("Spider@123")
    admin.confirm_password("Spider@123")
    time.sleep(5)
    admin.click_save()
    time.sleep(5)

    login.logout()

    login.login("loki12345","Spider@123")

    assert "dashboard" in driver.current_url.lower()

def test_search_user(driver):

    login = LoginPage(driver)
    admin = AdminPage(driver)

    login.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login.login("Admin", "admin123")

    admin.click_admin()
    admin.search_username("loki12345")
    admin.search_button()

    assert admin.is_user_displayed()









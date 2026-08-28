from OrangeHRM_Project.pages.homepage import HomePage
from OrangeHRM_Project.pages.loginpage import LoginPage

def test_verify_url(driver):

    home = HomePage(driver)
    home.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    assert "orangehrmlive.com" in home.get_current_url()

def test_verify_main_menu(driver):

    login=LoginPage(driver)
    home = HomePage(driver)

    login.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin","admin123")

    print("ADMIN")
    assert home.is_admin_visible()
    print("PIM")
    assert home.is_pim_visible()
    print("Leave")
    assert home.is_leave_visible()
    print("Time")
    assert home.is_time_visible()
    print("Recuritment")
    assert home.is_recrutiment_visble()
    print("Myinfo")
    assert home.is_myinfo_visible()
    print("Perfomance")
    assert home.is_performance_visible()
    print("Dashboard")
    assert home.is_dashboard_visible()

def test_verify_myinfo_submenu(driver):

    login = LoginPage(driver)
    home = HomePage(driver)
    login.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")

    home.click_myinfo()

    assert home.is_personal_details_displayed()
    home.click_personal_details()
    assert home.is_contact_details_displayed()
    home.click_contact_details()
    assert home.is_emergency_contacts_displayed()
    home.click_emergency_contacts()
    assert home.is_dependents_displayed()
    home.click_dependents()
    assert home.is_immigration_displayed()
    home.click_immigration()
    assert home.is_job_displayed()
    home.click_job()
    assert home.is_salary_displayed()
    home.click_salary()
    assert home.is_report_displayed()
    home.click_report()
    assert home.is_qualification_displayed()
    home.click_qualifications()
    assert home.is_membership_displayed()
    home.click_memberships()

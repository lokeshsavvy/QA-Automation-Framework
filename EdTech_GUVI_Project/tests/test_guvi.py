from OrangeHRM_Project import HomePage
from OrangeHRM_Project import LoginPage

def test_verify_url(driver):
    home = HomePage(driver)
    home.open_application()
    assert "guvi.in" in home.get_current_url()

def test_verify_title(driver):
    home = HomePage(driver)
    home.open_application()
    actual_title = home.get_page_title()
    assert "GUVI" in actual_title

def test_verify_loginbtn(driver):
    home = HomePage(driver)
    home.open_application()
    assert home.login_button_visible()
    home.click_login()

def test_verify_signupbtn(driver):
    home = HomePage(driver)
    home.open_application()
    assert home.signup_button_visible()
    home.click_signup()

def test_verify_signuppage(driver):
    home = HomePage(driver)
    home.open_application()
    home.click_signup()
    assert "/register/" in home.get_current_url()

def test_login(driver):

    home = HomePage(driver)
    login = LoginPage(driver)

    home.open_application()
    home.click_login()

    login.enter_email("testuser@gmail.com")
    login.enter_password("Test@123")
    login.click_login()

def test_invalid_login(driver):

    home = HomePage(driver)
    login = LoginPage(driver)

    home.open_application()
    home.click_login()

    login.enter_email("lokesh12345@gmail.com")
    login.enter_password("L!9lokii")
    login.click_login()
    assert login.invalid_login_message_displayed()

def test_verify_menu_items(driver):

    home = HomePage(driver)
    home.open_application()

    assert home.Courses_visible(),'Courses menu not visible'
    assert home.Practice_visible(),'Practice menu not visible'
    assert home.Liveclasses_visble(),'Live Classes menu not visible'

def test_verify_chatbox(driver):

    home = HomePage(driver)
    home.open_application()

    assert home.dobby_assistant_visible()

def test_verify_logout(driver):

    home = HomePage(driver)
    login = LoginPage(driver)

    home.open_application()
    home.click_login()

    login.enter_email("testuser@gmail.com")
    login.enter_password("Test@123")
    login.click_login()
    login.click_profile()
    login.click_logout()

    assert home.login_button_visible(),"Logout failed"
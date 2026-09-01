from Ecommerce_Saucedemo_Project.pages.loginpage import LoginPage
import pytest
from Ecommerce_Saucedemo_Project.test_data.login_test_data import (LOGIN_DATA,INVALID_LOGIN_DATA)
from Ecommerce_Saucedemo_Project.pages.homepage import HomePage

@pytest.mark.parametrize("username,password,expected",LOGIN_DATA)

def test_login(driver,username,password,expected):

    login = LoginPage(driver)
    login.open_url("https://www.saucedemo.com/")

    login.login(username,password)

    if expected == "success":
        assert "/inventory" in driver.current_url
    elif expected == "locked":
        assert login.is_error_message_displayed()

@pytest.mark.parametrize("username,password",INVALID_LOGIN_DATA)

def test_invalid_login(driver,username,password):
    login = LoginPage(driver)
    login.open_url("https://www.saucedemo.com/")
    login.login(username,password)
    assert login.is_error_message_displayed()

def test_logout(driver):

    login = LoginPage(driver)
    home = HomePage(driver)

    login.open_url("https://www.saucedemo.com/")

    login.login("standard_user","secret_sauce")

    home.logout()

    assert login.is_login_button_displayed()

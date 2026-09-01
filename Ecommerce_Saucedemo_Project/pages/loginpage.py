from Ecommerce_Saucedemo_Project.pages.basepage import BasePage
from Ecommerce_Saucedemo_Project.locators.login_locators import *

class LoginPage(BasePage):

    def enter_username(self,username):
        self.enter_text(USERNAME,username)

    def enter_password(self,password):
        self.enter_text(PASSWORD,password)

    def click_login(self):
        self.click_element(LOGIN_BTN)

    def is_error_message_displayed(self):
        return self.is_element_displayed(ERROR_MESSAGE)

    def is_login_button_displayed(self):
        return self.is_element_displayed(LOGIN_BTN)

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
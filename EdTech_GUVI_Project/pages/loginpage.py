from OrangeHRM_Project import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    EMAIL = (By.XPATH,"//input[@id='email']")
    PASSWORD = (By.XPATH,"//input[@id='password']")
    LOGIN = (By.XPATH,"//a[@id='login-btn']")
    ERROR_MSG = (By.XPATH,"//div[contains(text(),'Incorrect Email or Password')]")
    Profile_menu = (By.XPATH, "//img[@alt='Profile']")
    LOGOUT = (By.XPATH, "//p[text()='Sign Out']")

    def enter_email(self,email):
        self.enter_text(self.EMAIL,email)

    def enter_password(self,password):
        self.enter_text(self.PASSWORD,password)

    def click_login(self):
        self.click_element(self.LOGIN)

    def invalid_login_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MSG)

    def click_profile(self):
        self.click_element(self.Profile_menu)

    def click_logout(self):
        self.click_element(self.LOGOUT)


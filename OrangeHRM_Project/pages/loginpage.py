from selenium.webdriver.common.by import By
from OrangeHRM_Project.pages.basepage import BasePage

class LoginPage(BasePage):

    username_text = (By.XPATH,"//input[@name='username']")
    passcode = (By.XPATH,"//input[@name='password']")
    login_btn = (By.XPATH,"//button[@type='submit']")
    profile = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    logout_btn = (By.XPATH, "//a[contains(text(),'Logout')]")
    FORGOT_PASSWORD = (By.XPATH,"//p[normalize-space()='Forgot your password?']")
    RESER_USERNAME = (By.XPATH,"//input[@placeholder='Username']")
    RESET_PASSWORD = (By.XPATH,"//button[@type='submit']")
    SUCESS_MESSAGE = (By.XPATH,"//div[@class='orangehrm-card-container']")

    def login(self,username,password):

        self.enter_text(self.username_text,username)
        self.enter_text(self.passcode,password)
        self.click_element(self.login_btn)

    def logout(self):
        self.click_element(self.profile)
        self.click_element(self.logout_btn)

    def is_username_displayed(self):

        return self.is_element_displayed(self.username_text)

    def is_password_displayed(self):

        return self.is_element_displayed(self.passcode)

    def is_login_btn_displayed(self):

        return self.is_element_displayed(self.login_btn)

    def is_username_enabled(self):
        return self.is_element_enabled(self.username_text)

    def is_password_enabled(self):
        return self.is_element_enabled(self.passcode)

    def is_profile_button_displayed(self):
        return self.is_element_displayed(self.profile)

    def is_logout_btn_displayed(self):
        return self.is_element_displayed(self.logout_btn)

    def click_forgot_passwrod(self):
        self.click_element(self.FORGOT_PASSWORD)

    def enter_reset_username(self,username):
        self.enter_text(self.RESER_USERNAME,username)

    def click_reset_password(self):
        self.click_element(self.RESET_PASSWORD)

    def is_reset_sucessful(self):
        return self.is_element_displayed(self.SUCESS_MESSAGE)
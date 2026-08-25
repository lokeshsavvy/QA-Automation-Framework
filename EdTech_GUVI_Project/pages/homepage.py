from selenium.webdriver.common.by import By
from EdTech_GUVI_Project.pages.basepage import BasePage

class HomePage(BasePage):

    LOGIN_BTN = (By.XPATH,"//button[@id='login-btn']")
    SIGN_BTN = (By.XPATH, "//button[contains(text(),'Sign up')]")
    COURSES = (By.XPATH,"//p[text()='Courses']")
    PRACTICE = (By.XPATH,"//p[text()='Practice']")
    LIVECLASSES = (By.XPATH,"//p[text()='LIVE Classes']")
    CHATBOX = (By.XPATH,"//span[@aria-label='Chat Widget']")


    def open_application(self):
        self.driver.get("https://www.guvi.in")

    def get_page_title(self):
        return self.driver.title

    def click_login(self):
        self.click_element(self.LOGIN_BTN)

    def click_signup(self):
        self.click_element(self.SIGN_BTN)

    def login_button_visible(self):
        return self.is_element_displayed(self.LOGIN_BTN)

    def signup_button_visible(self):
        return self.is_element_displayed(self.SIGN_BTN)

    def Courses_visible(self):
        return self.is_element_displayed(self.COURSES)

    def Practice_visible(self):
        return self.is_element_displayed(self.PRACTICE)

    def Liveclasses_visble(self):
        return self.is_element_displayed(self.LIVECLASSES)

    def dobby_assistant_visible(self):
        return self.is_element_displayed(self.CHATBOX)
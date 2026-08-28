from OrangeHRM_Project.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class AdminPage(BasePage):

    ADMIN = (By.XPATH, "//span[normalize-space()='Admin']")
    ADD = (By.XPATH,"//button[normalize-space()='Add']")
    USER_ROLE = (By.XPATH,"(//div[contains(@class,'oxd-select-text')])[1]")
    ESS_OPTION = (By.XPATH,"//div[normalize-space()='ESS']")
    EMPLOYEE_NAME = (By.XPATH,"//input[@placeholder='Type for hints...']")
    EMPLOYEE_NAME_SUGGESTION = (By.XPATH,"//div[@role='listbox']//span")
    STATUS = (By.XPATH,"(//div[contains(@class,'oxd-select-text')])[4]")
    STATUS_OPTION = (By.XPATH,"//div[normalize-space()='Enabled']")
    USERNAME = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    PASSWORD = (By.XPATH,"(//input[@type='password'])[1]")
    CONFIRM_PASS = (By.XPATH,"(//input[@type='password'])[2]")
    SAVE = (By.XPATH,"//button[@type='submit']")
    SEARCH_USER = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    SEARCH_BTN = (By.XPATH,"//button[@type='submit']")
    SEARCH_RESULT = (By.XPATH,"//div[text()='loki12345']")


    def click_admin(self):
        self.click_element(self.ADMIN)

    def click_add(self):
        self.click_element(self.ADD)

    def select_user_role(self):
         self.click_element(self.USER_ROLE)
         self.click_element(self.ESS_OPTION)

    def enter_employee_name(self,employee_name):
        self.enter_text(self.EMPLOYEE_NAME,employee_name)
        self.click_element(self.EMPLOYEE_NAME_SUGGESTION)

    def select_status(self):
        self.click_element(self.STATUS)
        self.click_element(self.STATUS_OPTION)

    def enter_user_name(self,username):
        self.enter_text(self.USERNAME,username)

    def enter_password(self,password):
        self.enter_text(self.PASSWORD,password)

    def confirm_password(self,confrim_password):
        self.enter_text(self.CONFIRM_PASS,confrim_password)

    def click_save(self):
        self.click_element(self.SAVE)

    def search_username(self,username):
        self.enter_text(self.SEARCH_USER,username)

    def search_button(self):
        self.click_element(self.SEARCH_BTN)

    def is_user_displayed(self):
        return self.is_element_displayed(self.SEARCH_RESULT)














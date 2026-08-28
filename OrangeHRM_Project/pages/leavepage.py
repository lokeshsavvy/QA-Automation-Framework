from OrangeHRM_Project.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LeavePage(BasePage):

    LEAVE = (By.XPATH,"(//*[name()='svg'][@role='presentation'])[4]")
    ASSIGN_LEAVE = (By.XPATH,"//a[contains(text(),'Assign Leave')]")
    EMPLOYEE_NAME = (By.XPATH,"//input[@placeholder='Type for hints...']")
    EMPLOYEE_NAME_SUGGESTION = (By.XPATH, "//div[@role='listbox']//span")
    LEAVE_TYPE = (By.XPATH,"(//div[@class='oxd-select-text--after'])[1]")
    LEAVE_OPTION= (By.XPATH,"//div[normalize-space()='CAN - Personal']")
    FROM_DATE = (By.XPATH,"//label[contains(text(),'From Date')]/following::input[1]")
    TO_DATE = (By.XPATH,"//label[contains(text(),'From Date')]/following::input[2]")
    PARTIAL_DAYS = (By.XPATH,"//label[contains(text(),'Partial Days')]/following::div[@class='oxd-select-text-input'][1]")
    PARTIAL_OPTIONS = (By.XPATH,"//span[normalize-space()='All Days']")
    DURATION = (By.XPATH,"(//div[@class='oxd-select-text--after'])[3]")
    DURATION_OPTIONS= (By.XPATH,"//div[normalize-space()='Half Day - Morning']")
    COMMENTS = (By.XPATH,"//textarea[contains(@class,'oxd-textarea')]")
    ASSIGN_BTN = (By.XPATH,"//button[@type='submit']")
    CONFIRM_POPUP = (By.XPATH,"//div[@role='document']")
    CONFIRM_OK = (By.XPATH,"//button[normalize-space()='Ok']")
    # LEAVE_LIST = (By.XPATH,"//a[contains(text(),'Leave List')]")

    def click_leave(self):
        self.click_element(self.LEAVE)

    def click_assign_leave(self):
        self.click_element(self.ASSIGN_LEAVE)

    def enter_employee_name(self,employee_name):
        self.enter_text(self.EMPLOYEE_NAME,employee_name)
        self.click_element(self.EMPLOYEE_NAME_SUGGESTION)

    def select_leave_type(self):
        self.click_element(self.LEAVE_TYPE)
        self.click_element(self.LEAVE_OPTION)

    def enter_from_date(self,from_date):
        element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.FROM_DATE))
        element.click()
        element.send_keys(from_date)

    def enter_to_date(self,to_date):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.TO_DATE))
        element.click()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(to_date)
        element.send_keys(Keys.TAB)

    def select_partial(self):
        self.click_element(self.PARTIAL_DAYS)
        self.click_element(self.PARTIAL_OPTIONS)

    def select_duration(self):
        self.click_element(self.DURATION)
        self.click_element(self.DURATION_OPTIONS)

    def enter_comments(self,comments):
        self.enter_text(self.COMMENTS,comments)

    def click_assign(self):
        self.click_element(self.ASSIGN_BTN)

    def is_confirm_popup_displayed(self):
        return self.is_element_displayed(self.CONFIRM_POPUP)

    def click_ok(self):
        self.click_element(self.CONFIRM_OK)

    # def click_leave_list(self):
    #     self.click_element(self.LEAVE_LIST)
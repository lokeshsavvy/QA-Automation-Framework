from OrangeHRM_Project.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class ClaimPage(BasePage):

    CLAIM = (By.XPATH,"//a[@href='/web/index.php/claim/viewClaimModule']")
    CREATE_CLAIM = (By.XPATH,"//a[normalize-space()='Assign Claim']")
    EMPLOYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EMPLOYEE_NAME_SUGGESTION = (By.XPATH, "//div[@role='listbox']//span")
    EVENT = (By.XPATH,"(//div[@class='oxd-select-text--after'])[1]")
    EVENT_OPTION = (By.XPATH,"//div[normalize-space()='Medical Reimbursement']")
    CURRENCY = (By.XPATH,"(//i[contains(@class,'oxd-select-text--arrow')])[2]")
    CURRENCY_OPTION = (By.XPATH,"//*[normalize-space()='Indian Rupee']")
    REMARKS = (By.XPATH,"//textarea[contains(@class,'oxd-textarea')]")
    CREATE = (By.XPATH,"//button[@type='submit']")
    ADD_EXPENCES = (By.XPATH,"(//button[@type='button'][normalize-space()='Add'])[1]")
    EXPENCE_TYPE = (By.XPATH,"//div[@class='oxd-select-text--after']")
    EXPENCE_OPTION = (By.XPATH,"//*[normalize-space()='Planned Surgery']")
    DATE = (By.XPATH,"//input[@placeholder='yyyy-dd-mm']")
    AMMOUNT = (By.XPATH,"//label[normalize-space()='Amount']/following::input[1]")
    NOTE = (By.XPATH,"//label[contains(text(),'Note')]/following::textarea[1]")
    SAVE = (By.XPATH,"//button[@type='submit']")
    CLAIM_RECORD = (By.XPATH,"//*[contains(text(),'Planned Surgery')]")



    def click_claim(self):
        self.click_element(self.CLAIM)

    def click_create_claim(self):
        self.click_element(self.CREATE_CLAIM)

    def enter_employee_name(self, employee_name):
        self.enter_text(self.EMPLOYEE_NAME, employee_name)
        self.click_element(self.EMPLOYEE_NAME_SUGGESTION)

    def click_event(self):
        self.click_element(self.EVENT)
        self.click_element(self.EVENT_OPTION)

    def click_currency(self):
        self.click_element(self.CURRENCY)
        self.click_element(self.CURRENCY_OPTION)

    def enter_remarks(self,remarks):
        self.enter_text(self.REMARKS,remarks)

    def create_claim(self):
        self.click_element(self.CREATE)

    def add_expenses(self):
        self.click_element(self.ADD_EXPENCES)

    def click_expense_type(self):
        self.click_element(self.EXPENCE_TYPE)
        self.click_element(self.EXPENCE_OPTION)

    def enter_date(self,date):
        element = self.driver.find_element(*self.DATE)
        element.send_keys(date)

    def enter_amount(self,amount):
        self.enter_text(self.AMMOUNT,amount)

    def enter_note(self,note):
        self.enter_text(self.NOTE,note)

    def click_save(self):
        self.click_element(self.SAVE)

    def is_expence_record_displayed(self):
        return self.is_element_displayed(self.CLAIM_RECORD)
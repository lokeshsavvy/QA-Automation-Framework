from Ecommerce_Saucedemo_Project.pages.basepage import BasePage
from Ecommerce_Saucedemo_Project.locators.checkout_locators import *

class CheckoutPage(BasePage):

    def enter_first_name(self,first_name):
        self.enter_text(FIRST_NAME,first_name)

    def enter_last_name(self,last_name):
        self.enter_text(LAST_NAME,last_name)

    def enter_postal_code(self,postal):
        self.driver.find_element(*POSTAL_CODE).send_keys(postal)

    def click_continue_btn(self):
        self.click_element(CONTINUE_BTN)

    def click_finish(self):
        self.click_element(FINISH_BTN)

    def complete_checkout(self,first_name,last_name,postal):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal)
        self.click_continue_btn()

    def get_confirmation_msg(self):
        return self.driver.find_element(*CONFIRMATION_MSG).text
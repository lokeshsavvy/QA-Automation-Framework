from Ecommerce_Saucedemo_Project.pages.basepage import BasePage
from Ecommerce_Saucedemo_Project.locators.homepage_locators import *
from selenium.webdriver.support.ui import Select
import random

class HomePage(BasePage):

    def click_menu(self):
        self.click_element(MENU_BTN)

    def click_logout(self):
        self.click_element(LOGOUT_BTN)

    def logout(self):
        self.click_menu()
        self.click_logout()

    def is_cart_icon_displayed(self):
        return self.is_element_displayed(CART_ICON)

    def get_random_products(self,count=4):

        product_names = self.driver.find_elements(*PRODUCT_NAMES)
        product_prices = self.driver.find_elements(*PRODUCT_PRICES)

        products = []

        for name,price in zip(product_names,product_prices):

            products.append({"name":name.text,"price":price.text})

        return random.sample(products,count)

    def add_random_products(self,count = 4):
        buttons = self.driver.find_elements(*ADD_TO_CART_BTN)
        selected = random.sample(buttons,count)
        for button in selected:
            button.click()

    def get_cart_badge_count(self):
        return self.driver.find_element(*CART_BADGE).text

    def click_cart(self):
        self.click_element(CART_ICON)

    def select_sort_option(self,option_text):
        dropdown = Select(self.driver.find_element(*SORT_DROPDOWN))
        dropdown.select_by_visible_text(option_text)

    def get_product_prices(self):
        prices = self.driver.find_elements(*PRODUCT_PRICES)
        return [float(price.text.replace("$",""))
                for price in prices]

    def click_reset_app_status(self):
        self.click_element(RESET_BTN)

    def is_cart_badge_displayed(self):

        elements = self.driver.find_elements(*CART_BADGE)

        return len(elements) > 0

    def close_menu(self):
        self.click_element(CLOSE_MENU)





from Ecommerce_Saucedemo_Project.pages.basepage import BasePage
from Ecommerce_Saucedemo_Project.locators.cart_locators import *

class CartPage(BasePage):

    def get_cart_items(self):
        return(len(self.driver.find_elements(*CART_ITEMS)))

    def get_cart_product_details(self):

        names = self.driver.find_elements(*CART_PRODUCT_NAMES)
        prices = self.driver.find_elements(*CART_PRODUCT_PRICES)

        cart_products = []

        for name, price in zip(names,prices):
            cart_products.append({"name":name.text,"price":price.text})
        return cart_products

    def click_checkout(self):
        self.click_element(CHECK_OUT)



from selenium.webdriver.common.by import By

MENU_BTN = (By.ID,"react-burger-menu-btn")
LOGOUT_BTN = (By.ID,"logout_sidebar_link")
CART_ICON = (By.CLASS_NAME,"shopping_cart_link")
PRODUCT_NAMES = (By.CLASS_NAME,"inventory_item_name ")
PRODUCT_PRICES = (By.CLASS_NAME,"inventory_item_price")
ADD_TO_CART_BTN = (By.XPATH,"//button[contains(text(),'Add to cart')]")
CART_BADGE = (By.CLASS_NAME,"shopping_cart_badge")
SORT_DROPDOWN = (By.CLASS_NAME,"product_sort_container")
RESET_BTN = (By.ID,"reset_sidebar_link")
CLOSE_MENU = (By.ID,"react-burger-cross-btn")
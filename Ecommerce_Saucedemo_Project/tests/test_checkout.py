from Ecommerce_Saucedemo_Project.pages.loginpage import LoginPage
from Ecommerce_Saucedemo_Project.pages.homepage import HomePage
from Ecommerce_Saucedemo_Project.pages.cartpage import CartPage
from Ecommerce_Saucedemo_Project.pages.checkout_page import CheckoutPage

def test_complete_checkout(driver):

    login = LoginPage(driver)
    home = HomePage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open_url("https://www.saucedemo.com/")

    login.login("standard_user","secret_sauce")

    home.add_random_products(4)

    home.click_cart()

    cart.click_checkout()

    checkout.complete_checkout("loki","lokesh","517644")

    driver.save_screenshot("Ecommerce_Saucedemo_Project/utilities/screenshots/TC8_Order_Summary.png")

    checkout.click_finish()

    driver.save_screenshot("Ecommerce_Saucedemo_Project/utilities/screenshots/TC8_Order_Confirmation.png")

    assert checkout.get_confirmation_msg() == "Thank you for your order!"
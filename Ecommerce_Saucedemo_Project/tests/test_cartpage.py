from Ecommerce_Saucedemo_Project.pages.loginpage import LoginPage
from Ecommerce_Saucedemo_Project.pages.homepage import HomePage
from Ecommerce_Saucedemo_Project.pages.cartpage import CartPage

def test_add_products_to_cart(driver):

    login = LoginPage(driver)
    home = HomePage(driver)
    cart = CartPage(driver)

    login.open_url("https://www.saucedemo.com/")

    login.login("standard_user","secret_sauce")

    home.add_random_products(4)

    assert home.get_cart_badge_count() == "4"

    home.click_cart()

    assert cart.get_cart_items() == 4

def test_validate_cart_product_details(driver):

    login = LoginPage(driver)
    home = HomePage(driver)
    cart = CartPage(driver)

    login.open_url("https://www.saucedemo.com/")

    login.login("standard_user","secret_sauce")

    selected_products = home.get_random_products(4)
    print("\nSelected Products",selected_products)

    home.add_random_products(4)

    home.click_cart()

    cart_products = cart.get_cart_product_details()
    print("\nCart Products:",cart_products)

    assert len(cart_products)==4



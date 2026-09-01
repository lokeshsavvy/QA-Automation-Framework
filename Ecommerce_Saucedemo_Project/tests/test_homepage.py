from Ecommerce_Saucedemo_Project.pages.homepage import HomePage
from Ecommerce_Saucedemo_Project.pages.loginpage import LoginPage

def test_cart_icon_visibility(driver):
    login = LoginPage(driver)
    home = HomePage(driver)

    login.open_url("https://www.saucedemo.com/")

    login.login("standard_user","secret_sauce")

    assert home.is_cart_icon_displayed()

def test_random_product_selection(driver):

    login = LoginPage(driver)
    home = HomePage(driver)

    login.open_url("https://www.saucedemo.com/")

    login.login("standard_user","secret_sauce")

    products = home.get_random_products(4)

    print("\nSelected Products:")

    for product in products:

        print(f"Name:{product['name']} |" f"Price:{product['price']}")

    assert len(products) == 4

def test_sort_products_by_price(driver):

    login = LoginPage(driver)
    home = HomePage(driver)

    login.open_url("https://www.saucedemo.com/")

    login.login("standard_user","secret_sauce")

    home.select_sort_option("Price (low to high)")

    prices = home.get_product_prices()

    assert prices == sorted(prices)

def test_reset_app_state(driver):

    login = LoginPage(driver)
    home = HomePage(driver)

    login.open_url("https://www.saucedemo.com/")

    login.login("standard_user","secret_sauce")

    home.add_random_products(4)

    assert home.get_cart_badge_count() == "4"

    home.click_menu()

    home.click_reset_app_status()

    home.close_menu()

    assert not home.is_cart_badge_displayed()
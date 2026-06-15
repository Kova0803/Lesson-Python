from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Mainshoppage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://saucedemo.com"
        self.wait = WebDriverWait(driver, 10)

        # Локаторы товаров
        self.product_1 = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.product_2 = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.product_3 = (By.ID, "add-to-cart-sauce-labs-onesie")

        # Иконка корзины
        self.total_check = (By.CLASS_NAME, "shopping_cart_link")

    def produkt_in_basket(self):
        self.driver.find_element(*self.product_1).click()
        self.driver.find_element(*self.product_2).click()
        self.driver.find_element(*self.product_3).click()

    def checkout(self):
        self.driver.find_element(*self.total_check).click()

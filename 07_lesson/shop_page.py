from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class OnlineStorePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.wait = WebDriverWait(driver, 10)

        # Локаторы элементов
        self.field_username = By.ID, "user-name"
        self.field_password = By.ID, "password"
        self.button_login = By.ID, "login-button"
        
        # Локаторы нужных товаров
        self.product_1 = By.ID, "add-to-cart-sauce-labs-backpack"
        self.product_2 = By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        self.product_3 = By.ID, "add-to-cart-sauce-labs-onesie"
        
        self.basket = By.CLASS_NAME, "shopping_cart_link"
        self.total_check = By.ID, "checkout"
        self.field_first_name = By.ID, "first-name"
        self.field_last_name = By.ID, "last-name"
        self.field_post = By.ID, "postal-code"
        self.button_cont = By.ID, "continue"
        self.field_total = By.CSS_SELECTOR, "[data-test='total-label']"

    def open(self):
        self.driver.get(self.url)

    def login(self):
        self.driver.find_element(
            *self.field_username).send_keys("standard_user")
        self.driver.find_element(
            *self.field_password).send_keys("secret_sauce")
        self.driver.find_element(
            *self.button_login).click()

    def produkt_in_basket(self):
        self.driver.find_element(*self.product_1).click()
        self.driver.find_element(*self.product_2).click()
        self.driver.find_element(*self.product_3).click()
        self.driver.find_element(*self.basket).click()

    def checkout(self):
        self.driver.find_element(
            *self.total_check).click()

    def placing_an_order(self, first_name="Иван", last_name="Иванов", post_code="123456"):
        self.driver.find_element(*self.field_first_name).send_keys(first_name)
        self.driver.find_element(*self.field_last_name).send_keys(last_name)
        self.driver.find_element(*self.field_post).send_keys(post_code)
        self.driver.find_element(*self.button_cont).click()
        
        return self.driver.find_element(*self.field_total).text

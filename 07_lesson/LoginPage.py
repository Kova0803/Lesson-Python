from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://saucedemo.com"
        self.wait = WebDriverWait(driver, 10)

        self.field_username = (By.ID, "user-name")
        self.field_password = (By.ID, "password")
        self.button_login = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self):
        self.driver.find_element(
            *self.field_username).send_keys("standard_user")
        self.driver.find_element(
            *self.field_password).send_keys("secret_sauce")
        self.driver.find_element(
            *self.button_login).click()

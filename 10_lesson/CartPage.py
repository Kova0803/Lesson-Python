import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.description("""
    Данный тест проверяет переход на страницу оформления заказа
     """)
    def checkout(self) -> None:
        """
        Эта кнопка для перехода на страницу оформления заказа
        """
        with allure.step("Переходим на страницу оформления заказа"):
            self.driver.find_element(*self.checkout_button).click()

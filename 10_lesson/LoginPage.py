import allure
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

    @allure.description("""
        Данный тест проверяет стандартный сценарий авторизации пользователя.
        Предусловия: пользователь зарегистрирован в системе.
        Ожидаемый результат: открывается главная страница магазина, доступна корзина.
        """)
    def open(self) -> None:
        """
        функция для перехода на сайт
        """
        with allure.step("Открыть сайт в браузере Firefox"):
            self.driver.get(self.url)

    @allure.step("Заполняем логин: {username} и пароль: {password}")
    def login(
        self, username: str = "standard_user", password: str = "secret_sauce"
    ) -> None:
        self.driver.find_element(*self.field_username).send_keys(username)
        self.driver.find_element(*self.field_password).send_keys(password)

        with allure.step("Нажимаем войти"):
            self.driver.find_element(*self.button_login).click()

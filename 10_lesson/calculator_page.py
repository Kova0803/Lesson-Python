import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        # Ссылка на сайт калькулятора
        self.url = (
            "https://bonigarcia.dev" "/selenium-webdriver-java/slow-calculator.html"
        )
        self.wait = WebDriverWait(driver, 20)
        # Локаторы элементов
        self.delay_input = By.CSS_SELECTOR, "#delay"
        self.screen = By.CLASS_NAME, "screen"
        # локатор для кнопок
        self.button_xpath = "//span[text()='{}']"

    def open(self) -> None:
        """
        Открыть страницу калькулятора.
        """
        with allure.step("Открыть сайт калькулятора"):
            self.driver.get(self.url)

    def set_delay(self, seconds: int) -> None:
        """
        Ввести значение в поле задержки
        """
        with allure.step(
            "дождаться пока очистится поле ввода задержки и введется указанное значение"
        ):
            delay_field = self.wait.until(EC.element_to_be_clickable(self.delay_input))
            delay_field.clear()
            delay_field.send_keys(str(seconds))

    def click_button(self, text: str) -> None:
        """
        Нажать кнопки: 7, +, 8, =.
        """
        with allure.step("Нажать на кнопки калькулятора"):
            locator = (By.XPATH, self.button_xpath.format(text))
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_result(self, expected_text: str) -> str:
        """
        Проверить, что в окне отобразится результат 15 через 10 секунд
        """
        with allure.step(
            "Проверям , что в окне решения отобразится результат 15 через 10 секунд"
        ):
            self.wait.until(
                EC.text_to_be_present_in_element(self.screen, expected_text)
            )
        return self.driver.find_element(*self.screen).text

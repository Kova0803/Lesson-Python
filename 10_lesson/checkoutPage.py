import allure
from selenium.webdriver.common.by import By


class checkoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.field_first_name = (By.ID, "first-name")
        self.field_last_name = (By.ID, "last-name")
        self.field_post = (By.ID, "postal-code")
        self.button_cont = (By.ID, "continue")
        self.field_total = (By.CSS_SELECTOR, "[data-test='total-label']")

    @allure.description("""
    Данный тест проверяет оформление заказа и сравнивает корркиность итоговой суммы.
    """)
    @allure.step("заполняем форму данными для оформления заказа")
    def placing_an_order(self, first_name: str, last_name: str, post_code: int) -> str:
        """
        Страница оформления заказа,
        которая будет содержать методы для заполнения формы данными
        (имя, фамилия, почтовый индекс) и проверки итоговой стоимости.
        """

        self.driver.find_element(*self.field_first_name).send_keys(first_name)
        self.driver.find_element(*self.field_last_name).send_keys(last_name)
        self.driver.find_element(*self.field_post).send_keys(post_code)
        self.driver.find_element(*self.button_cont).click()
        with allure.step("сравниваем итоговую сумму"):
            return self.driver.find_element(*self.field_total).text

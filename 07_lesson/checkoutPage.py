from selenium.webdriver.common.by import By


class checkoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.field_first_name = (By.ID, "first-name")
        self.field_last_name = (By.ID, "last-name")
        self.field_post = (By.ID, "postal-code")
        self.button_cont = (By.ID, "continue")
        self.field_total = (By.CSS_SELECTOR, "[data-test='total-label']")

    def placing_an_order(
        self, first_name="Иван", last_name="Иванов", post_code="123456"
    ):
        self.driver.find_element(*self.field_first_name).send_keys(first_name)
        self.driver.find_element(*self.field_last_name).send_keys(last_name)
        self.driver.find_element(*self.field_post).send_keys(post_code)
        self.driver.find_element(*self.button_cont).click()
        return self.driver.find_element(*self.field_total).text

import pytest
from selenium import webdriver
from calculator_page import SlowCalculatorPage


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    
    yield chrome_driver
    
    chrome_driver.quit()


def test_slow_calculator(driver):
    page = SlowCalculatorPage(driver)
    
    page.open()

    page.set_delay(45)

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")
    
    actual_result = page.get_result("15")
    assert actual_result == "15", f"Ожидалось 15, но калькулятор показал {
        actual_result}"

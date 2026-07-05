import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    # Инициализация драйвера (например, для Firefox, как в вашем тесте)
    browser = webdriver.Firefox()
    yield browser
    # Закрытие браузера после выполнения теста
    browser.quit()

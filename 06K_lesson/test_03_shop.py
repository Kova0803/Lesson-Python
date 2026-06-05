from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()),
    options=options)

driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://www.saucedemo.com/")

search_input = driver.find_element(By.ID, "user-name")
search_input.send_keys("standard_user")

search_input = driver.find_element(By.ID, "password")
search_input.send_keys("secret_sauce")
input_login = driver.find_element(By.ID, "login-button").click()
product_1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
product_2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
product_3 = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
basket = driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
total_check = driver.find_element(By.ID, "checkout").click()

input_first_name = wait.until(
    EC.visibility_of_element_located((By.ID, "first-name")))
input_first_name.send_keys("Marina")

input_last_name = wait.until(
    EC.visibility_of_element_located((By.ID, "last-name")))
input_last_name.send_keys("Ko")

post = wait.until(
    EC.visibility_of_element_located((By.ID, "postal-code")))
post.send_keys("888888")

cont = driver.find_element(By.ID, "continue").click()

total = driver.find_element(By.CSS_SELECTOR, "[data-test='total-label']").text

is_correct = "58.29" in total
print(is_correct)

driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options)

driver.maximize_window()
waiter = WebDriverWait(driver, 50)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

input_time = waiter.until(
    EC.visibility_of_element_located((By.ID, "delay")))
input_time.clear()
input_time.send_keys("45")

input_first_num = driver.find_element(By.XPATH, "//span[text()='7']").click()
input_sign = driver.find_element(By.XPATH, "//span[text()='+']").click()
input_second_num = driver.find_element(By.XPATH, "//span[text()='8']").click()
input_equals = driver.find_element(By.XPATH, "//span[text()='=']").click()

waiter.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

total_result = driver.find_element(By.CLASS_NAME, "screen").text

assert total_result == "15"

driver.quit()

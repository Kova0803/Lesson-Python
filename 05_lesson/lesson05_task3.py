from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

wait = WebDriverWait(driver, 10)

input_field = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
input_field.send_keys("12345")
sleep(2)

input_field.clear()
sleep(2)

input_field.send_keys("54321")
sleep(3)

driver.quit()

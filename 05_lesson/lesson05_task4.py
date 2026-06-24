from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
username_field.send_keys("tomsmith")
sleep(1)

pass_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
pass_field.send_keys("SuperSecretPassword!")
sleep(1)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
sleep(1)

flash_message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))

print(flash_message.text)

driver.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

wait = WebDriverWait(driver, 10)

button_xpath = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"

blue_button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
blue_button.click()

sleep(5)

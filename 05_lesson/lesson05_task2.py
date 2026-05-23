from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")


wait = WebDriverWait(driver, 10)
button_css = "button.btn-primary"

blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_css)))

blue_button.click()

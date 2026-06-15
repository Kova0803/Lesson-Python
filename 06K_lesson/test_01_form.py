from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(
    service=EdgeService(EdgeChromiumDriverManager().install())
)

wait = WebDriverWait(driver, 10)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.maximize_window()

# Вводим имя
input_first_name = wait.until(
    EC.visibility_of_element_located((By.NAME, "first-name")))
input_first_name.send_keys("Иван")

# вводим фамилию
last_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "last-name")))
last_name_field.send_keys("Петров")

# вводим адрес Ленина, 55-3
address_field = wait.until(EC.visibility_of_element_located((By.NAME, "address")))
address_field.send_keys("Ленина, 55-3")

#емейл test@skypro.com
email_field = wait.until(EC.visibility_of_element_located((By.NAME, "e-mail")))
email_field.send_keys("test@skypro.com")

# телефон +7985899998787
phone_field = wait.until(EC.visibility_of_element_located((By.NAME, "phone")))
phone_field.send_keys("+7985899998787")

# zip code ПУСТО

# Москва
city_field = wait.until(EC.visibility_of_element_located((By.NAME, "city")))
city_field.send_keys("Москва")

# Россия
country_field = wait.until(EC.visibility_of_element_located((By.NAME, "country")))
country_field.send_keys("Россия")

# job QA
job_position_field = wait.until(EC.visibility_of_element_located((By.NAME, "job-position")))
job_position_field.send_keys("QA")

# компания SkyPro
company_field = wait.until(EC.visibility_of_element_located((By.NAME, "company")))
company_field.send_keys("SkyPro")

submit_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)
submit_button.click()

zip_code = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
bg_color = zip_code.value_of_css_property("background-color")
assert "248" in bg_color
print("Поле Zip code красное")

first_name = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
first_name_bg = first_name.value_of_css_property("background-color")
assert "209, 231, 221" in first_name_bg
print("Поле First name зелёное")

last_name = wait.until(
    EC.presence_of_element_located((By.ID, "last-name")))
last_name_bg = last_name.value_of_css_property("background-color")
assert "209, 231, 221" in last_name_bg
print("Поле Last name зелёное")

address = wait.until(
    EC.presence_of_element_located((By.ID, "address")))
address_bg = address.value_of_css_property("background-color")
assert "209, 231, 221" in address_bg
print("Поле Address зелёное")

email = wait.until(EC.presence_of_element_located((By.ID, "e-mail")))
email_bg = email.value_of_css_property("background-color")
assert "209, 231, 221" in email_bg
print("Поле email зелёное")

phone = wait.until(EC.presence_of_element_located((By.ID, "phone")))
phone_bg = phone.value_of_css_property("background-color")
assert "209, 231, 221" in phone_bg
print("Поле Phone зелёное")

city = wait.until(EC.presence_of_element_located((By.ID, "city")))
city_bg = city.value_of_css_property("background-color")
assert "209, 231, 221" in city_bg
print("Поле City зелёное")

country = wait.until(EC.presence_of_element_located((By.ID, "country")))
country_bg = country.value_of_css_property("background-color")
assert "209, 231, 221" in country_bg
print("Поле Country зелёное")

job_position = wait.until(EC.presence_of_element_located((By.ID, "job-position")))
job_position_bg = job_position.value_of_css_property("background-color")
assert "209, 231, 221" in job_position_bg
print("Поле Job Position зелёное")

company = wait.until(EC.presence_of_element_located((By.ID, "company")))
company_bg = company.value_of_css_property("background-color")
assert "209, 231, 221" in company_bg
print("Поле Company зелёное")

driver.quit

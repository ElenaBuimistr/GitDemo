import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, 'autosuggest').send_keys('ind')
time.sleep(3)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

# it will right all the items with the same xpath in the list

print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break

driver.find_element(By.XPATH, '//input[@id="autosuggest"]').get_attribute('value')
value_country = driver.find_element(By.XPATH, '//input[@id="autosuggest"]').get_attribute('value')
print(value_country)

assert value_country == 'India'

time.sleep(2)

# Check-box
driver.find_element(By.XPATH, '//input[@id="ctl00_mainContent_chk_friendsandfamily"]').click()

time.sleep(2)


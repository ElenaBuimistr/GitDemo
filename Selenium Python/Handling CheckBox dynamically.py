import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()
        break

time.sleep(3)

radiobuttons = driver.find_elements(By.XPATH, '//input[@class="radioButton"]')

print(len(radiobuttons))

# for radiobutton in radiobuttons:
#     if radiobutton.get_attribute('value') == 'radio3':
#         radiobutton.click()
#         assert radiobutton.is_selected()
#         break

# time.sleep(3)

radiobuttons[0].click()
assert radiobuttons[0].is_selected

time.sleep(2)


assert driver.find_element(By.XPATH, '//input[@id="displayed-text"]').is_displayed()
driver.find_element(By.XPATH, '//input[@id="hide-textbox"]').click()
assert not driver.find_element(By.XPATH, '//input[@id="displayed-text"]').is_displayed()


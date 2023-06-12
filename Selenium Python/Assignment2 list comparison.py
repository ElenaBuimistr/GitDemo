import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element(By.XPATH, '//input[@type="search"]').send_keys('ber')

time.sleep(2)

results = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
count = len(results)
print(count)

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

for result in results:
    actualList.append(result.find_element(By.XPATH, 'h4').text)

print(actualList)

assert expectedList == actualList
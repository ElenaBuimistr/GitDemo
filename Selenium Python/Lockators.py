from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# CSS -  tagname[attribute='value'] -> //input[@type='submit'],  #id, .classname


driver.find_element(By.NAME, 'email').send_keys('hi@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123')
driver.find_element(By.ID, 'exampleCheck1').click()
# driver.find_element(By.XPATH, '//input[@type="submit"]').click()
driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
message = driver.find_element(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]').text
print(message)
assert 'Success' in message
print()

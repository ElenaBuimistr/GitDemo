import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = 'Rahul'
driver.find_element(By.XPATH, '//input[@id="name"]').send_keys(name)
driver.find_element(By.XPATH, '//input[@id="alertbtn"]').click()

time.sleep(2)

alert = driver.switch_to.alert
alertText = alert.text    # read the text from the alert message
print(alertText)

assert name in alertText

alert.accept()
# alert.dismiss()

time.sleep(2)
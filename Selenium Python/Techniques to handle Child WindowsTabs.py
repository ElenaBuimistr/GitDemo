import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")

# windowsOpened = driver.window_handles
# print(windowsOpened)
driver.find_element(By.XPATH, '//a[@href="/windows/new"]').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH, '//h3').text
print(driver.find_element(By.XPATH, '//h3').text)

driver.close()

driver.switch_to.window(driver.window_handles[0])
print(driver.find_element(By.XPATH, '//h3').text)
import time

from selenium import webdriver

#chrome driver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.minimize_window()
# driver.back()
driver.refresh()
time.sleep(10)
print()
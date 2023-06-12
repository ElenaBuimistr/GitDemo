import time

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Service()

# service_obj = Service('C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# service_obj = Service('C:\\Users\\Elena\\PycharmProjects\\Udemy Testing\\chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj, options=options)
driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/')

# print()

# time.sleep(3)

# driver.close()



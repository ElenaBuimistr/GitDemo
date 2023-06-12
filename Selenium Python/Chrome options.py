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

# https://selenium-python.readthedocs.io/api.html
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-start-maximized')
chromeOptions.add_argument('headless')    # to have the option of running in the headless mode
chromeOptions.add_argument('__ignore-certificate-errors')  # to igtore the certification errors

driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.title
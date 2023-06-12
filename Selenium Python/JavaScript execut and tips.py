import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('headless')    # to have the option of running in the headless mode
chromeOptions.add_argument('__ignore-certificate-errors')  # to igtore the errors


service_obj = Service("C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome(service=service_obj, options=chromeOptions) # to run in the headless mode

driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script('window.scrollBy(0, 700)')
driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')  # scrolls to the bottom of the page
# driver.get_screenshot_as_file('1.png')  # take screenshot


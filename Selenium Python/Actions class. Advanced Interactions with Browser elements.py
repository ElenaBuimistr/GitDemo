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
driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

action = ActionChains(driver)
# action.click_and_hold()
# action.double_click()
# action.move_to_element() different options are allowed for interaction

action.move_to_element(driver.find_element(By.XPATH, '//button[@id="mousehover"]')).perform()
# action.context_click(driver.find_element(By.XPATH, '//a[@href="#top"]')).perform()  # right click
action.move_to_element(driver.find_element(By.XPATH, '//a[@href="#top"]/following-sibling::a')).click().perform()

print()
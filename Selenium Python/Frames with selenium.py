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

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame('mce_0_ifr')
time.sleep(2)
driver.find_element(By.XPATH, '//body[@id="tinymce"]').clear()
driver.find_element(By.XPATH, '//body[@id="tinymce"]').send_keys('I am able to automate frames!')
time.sleep(2)
print(driver.find_element(By.XPATH, '//body[@id="tinymce"]').text)

driver.switch_to.default_content()


print()
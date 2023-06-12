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
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()


driver.find_element(By.XPATH, '//a[@href="/angularpractice/shop"]').click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[@class="nav-link btn btn-primary"]')))

itemsList = []

items = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')

for item in items:
    productName = item.find_element(By.XPATH, 'div/h4/a').text
    if productName == 'Blackberry':
        item.find_element(By.XPATH, 'div/button').click()


driver.find_element(By.XPATH, '//a[@class="nav-link btn btn-primary"]').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-success"]')))

driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//input[@class="btn btn-success btn-lg"]')))

driver.find_element(By.XPATH, '//input[@id="country"]').send_keys('Cy')

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="suggestions"]')))

driver.find_element(By.XPATH, '//div[@class="suggestions"]').click()

driver.find_element(By.XPATH, '//label[@for="checkbox2"]').click()

driver.find_element(By.XPATH, '//input[@class="btn btn-success btn-lg"]').click()

successMessage = driver.find_element(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]').text

print(successMessage)

assert 'Success! Thank you!' in successMessage



import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element(By.XPATH, '//input[@type="search"]').send_keys('ber')

results = driver.find_elements(By.XPATH, '//div[@class="products"]/div')

count = len(results)
print(count)

for result in results:
    result.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.XPATH, '//a[@class="cart-icon"]').click()
driver.find_element(By.XPATH, '//ancestor::div[@class="cart-preview active"]/descendant::button[@type="button"]').click()
driver.find_element(By.XPATH, '//input[@class="promoCode"]').send_keys('rahulshettyacademy')
driver.find_element(By.XPATH, '//button[@class="promoBtn"]').click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//span[@class="promoInfo"]')))

totalAmount = driver.find_element(By.XPATH, '//span[@class="totAmt"]').text
totalAfterDiscount = driver.find_element(By.XPATH, '//span[@class="discountAmt"]').text


assert float(totalAmount) > float(totalAfterDiscount)


print()
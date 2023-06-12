import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\Elena\\PycharmProjects\\Test\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# Open child window and find the email
driver.find_element(By.XPATH, '//a[@class="blinkingText"]').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
element = driver.find_element(By.XPATH, '//p[@class="im-para red"]//descendant::a')
string = element.get_attribute('href')
var = string.split(":")
email = var[1]
driver.close()

# Go back to the main window
# Place the email in the 'email' field
# Place the fake password and click on sign in
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(email)
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('Password')
driver.find_element(By.XPATH, '//input[@id="signInBtn"]').click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-danger col-md-12"]')))

# Grab the error message and print it
errorMessage = driver.find_element(By.XPATH, '//div[@class="alert alert-danger col-md-12"]').text

print(errorMessage)
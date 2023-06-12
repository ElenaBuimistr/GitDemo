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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

sortedVeggis = []
# click on sorting icon
driver.find_element(By.XPATH, '//span[text()="Veg/fruit name"]').click()

# collect all the vegetables names and stpre them to the list > sorted vegNames (a, b, c)

vegNames = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')

for veg in vegNames:
    sortedVeggis.append(veg.text)

originalBrSortedList = sortedVeggis.copy()
print(originalBrSortedList)

# sort this list via phyton
sortedVeggis.sort()


# compare 2 lists

assert sortedVeggis == originalBrSortedList



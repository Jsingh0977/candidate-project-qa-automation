#This automated framework validates the workflow of opening a Chat care session

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('F:\Desktop\chromedriver_win32 (1)./chromedriver')
driver.maximize_window()

#Open URL
driver.get("https://www.zoomcare.com/schedule")

time.sleep(3)

# Select Current location and find a clinic care appointment time slot
element = driver.find_element(By.CSS_SELECTOR, "span.css-901oao.css-16my406")
element.click()
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR, "div.css-901oao.css-vcwn7f")
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/div[1]/button[3]/div")
element.click()
time.sleep(3)

# Check if the registration page for scheduling appears
if driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/form/div[1]/h2"):
    print("Successfully landed at the registration page for scheduling ChatCare appointment")

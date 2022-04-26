#This automated framework validates the workflow of scheduling video care appointments using user's current location

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('F:\Desktop\chromedriver_win32 (1)./chromedriver')
driver.maximize_window()

#Open the URL
driver.get("https://www.zoomcare.com/schedule")

time.sleep(3)

#Select Current location and find a clinic care appointment time slot
element = driver.find_element(By.CSS_SELECTOR, "span.css-901oao.css-16my406")
element.click()
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR, "div.css-901oao.css-vcwn7f")
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/div[1]/button[2]/div/div[1]/i")
element.click()
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR,
                              "div.css-18t94o4.css-1dbjc4n.r-1awozwy.r-1loqt21.r-13awgt0.r-18u37iz.r-1777fci.r-10paoce.r-1otgn73.r-1i6wzkk.r-lrvibr")
element.click()

#Check if the registration page for scheduling appears
if driver.find_element(By.CSS_SELECTOR,"div.css-1dbjc4n.r-1awozwy.r-1loqt21.r-18u37iz.r-1777fci.r-10paoce.r-1otgn73.r-1i6wzkk.r-lrvibr"):
    print("Successfully landed at the registration page for scheduling VideoCare appointment")

#WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.css-18t94o4.css-1dbjc4n.r-1awozwy.r-1loqt21.r-13awgt0.r-18u37iz.r-1777fci.r-10paoce.r-1otgn73.r-1i6wzkk.r-lrvibr"))).click()
#element = driver.find_element(By.CSS_SELECTOR, "div.css-901oao")
#element.click()


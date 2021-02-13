from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

## Provide your username and password inside the quotes
username = ''
password = ''
timeout=5

browser = webdriver.Firefox()
browser.get('https://netaccess.iitm.ac.in/account/login')

userElem = browser.find_element_by_id('username')
userElem.send_keys(username)
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys(password)

try:
    nextButton = browser.find_element_by_name('submit')
    nextButton.click()
except NameError:
    print("Hey!!! You gave me wrong Log in details")

try:
    element_present = EC.presence_of_element_located((By.ID, 'content'))
    WebDriverWait(browser, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")

approveButton = browser.find_element_by_xpath('//a[contains(@href,"/account/approve")]')
approveButton.click()

try:
    element_present = EC.presence_of_element_located((By.ID, 'radios-1'))
    WebDriverWait(browser, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")

durationButton = browser.find_element_by_id("radios-1")
durationButton.click()
approveButton2 = browser.find_element_by_name('approveBtn')
approveButton2.click()

browser.close()
browser.quit()

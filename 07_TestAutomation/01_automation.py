from selenium import webdriver
from selenium.webdriver.common.by import By

# using Chromium driver for chrome
# or we can put driver to c:/Windows folder 
# /user/local/bin in osx
chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

#Selectors
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element(By.ID, "user-message")

#Css Selector
user_button2 = chrome_browser.find_element(By.CSS_SELECTOR, '#get-input > .btn')

user_message.clear()
user_message.send_keys('I am extra cool')

show_message_button.click()
output_message = chrome_browser.find_element(By.ID, 'display')

assert 'I am extra cool' in output_message.text

# quiting the driver
chrome_browser.quit()

# we can put delays with wait
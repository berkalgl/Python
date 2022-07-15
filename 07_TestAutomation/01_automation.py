from selenium import webdriver

# using Chromium driver for chrome
# or we can put driver to c:/Windows folder 
# /user/local/bin in osx
chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
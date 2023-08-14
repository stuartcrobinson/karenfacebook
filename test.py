from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Chrome()

driver.get("https://www.python.org")

print(driver.title)
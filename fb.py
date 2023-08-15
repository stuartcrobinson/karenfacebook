from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

# driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Chrome()

driver.get("https://www.facebook.com")

email = open('secrets/.email').read()
password = open('secrets/.password').read()

print(email)
print(password)


driver.find_element("name", 'email').send_keys('stuart.clifford@gmail.com')
time.sleep(0.25)
driver.find_element("name", 'pass').send_keys(password)
time.sleep(0.25)
driver.find_element("name", 'login').click()


time.sleep(1)

driver.get("https://www.facebook.com/groups/144178824324561")

time.sleep(1)

divs = driver.find_elements(By.XPATH, '//div[@role="feed"]/div')

#driver.find_element(By.XPATH, '//div[@role="feed"]/div[2]//span/a/strong').text


del divs[0] #remove "Most Relevant" link

for div in divs:
    op_name = div.find_element(By.XPATH, './/span/a/strong').get_attribute('innerText')  #works
    # print(div)
    print(op_name)


print(len(divs))
print(driver.title)
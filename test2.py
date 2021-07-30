import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver= 'C:\Project\selenium\chromedriver.exe'
driver= webdriver.Chrome(chromedriver)
driver.implicitly_wait(1)
sample_url = 'http://59.3.93.125:8085/aimir/login'
driver.get(sample_url)
driver.maximize_window()

driver.find_element_by_css_selector('#id').send_keys('admin')
driver.find_element_by_css_selector('#pw').send_keys('nuri1234')
driver.find_element_by_css_selector('#pw').send_keys(Keys.ENTER)

print(driver.title)
print(driver.current_url)

#driver.quit()

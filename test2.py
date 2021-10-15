import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver= 'C:\Project\selenium\chromedriver.exe'
driver= webdriver.Chrome(chromedriver)
driver.implicitly_wait(1)
sample_url = ''
driver.get(sample_url)
driver.maximize_window()

driver.find_element_by_css_selector('#id').send_keys('')
driver.find_element_by_css_selector('#pw').send_keys('')
driver.find_element_by_css_selector('#pw').send_keys(Keys.ENTER)

print(driver.title)
print(driver.current_url)

#driver.quit()

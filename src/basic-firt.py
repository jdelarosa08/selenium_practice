import time
import os
from selenium import webdriver

src_win = os.path.abspath(os.path.join(os.path.dirname(__file__), 'drivers')) + '/chromedriver.exe'
driver = webdriver.Chrome(executable_path=src_win)
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
driver.implicitly_wait(8)
driver.find_element_by_id('at-cv-lightbox-close').click()
driver.find_element_by_id('user-message').send_keys('abc')
driver.find_element_by_xpath('//*[@id="get-input"]/button').click()
if driver.find_element_by_id('display').text == 'abc':
    print('Single input Field Completed')
else:
    print('Single input Field Failed')
driver.close()
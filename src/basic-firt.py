import time
import os
from selenium import webdriver

#Excersice 1
src_win = os.path.abspath(os.path.join(os.path.dirname(__file__), 'drivers')) + '/chromedriver.exe'
driver = webdriver.Chrome(executable_path=src_win)
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
driver.maximize_window()
driver.implicitly_wait(8)
driver.find_element_by_id('at-cv-lightbox-close').click()
driver.find_element_by_id('user-message').send_keys('abc')
driver.find_element_by_xpath('//*[@id="get-input"]/button').click()
display = driver.find_element_by_id('display').text
if display == 'abc':
    print('Single input Field Completed')

else:
    print('Single input Field Failed')


driver.find_element_by_id('sum1').send_keys('10')
driver.find_element_by_id('sum2').send_keys('5')
element=driver.find_element_by_xpath('//*[@id="gettotal"]/button')
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()
if driver.find_element_by_id('displayvalue').text == '15':
    print('Two input Field Completed')
else:
    print('Two input Field Failed')

time.sleep(3)
driver.close()

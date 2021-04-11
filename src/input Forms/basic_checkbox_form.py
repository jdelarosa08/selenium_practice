import time
import os
from selenium import webdriver

#Excersice 2
src_win = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) + '\drivers\chromedriver.exe'
driver = webdriver.Chrome(executable_path=src_win)
driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
driver.maximize_window()
driver.implicitly_wait(8)
driver.find_element_by_id('isAgeSelected').click()
if driver.find_element_by_id('txtAge').text == 'Success - Check box is checked':
    print("Single Checkbox Completed")
else:
    print("Single Checkbox Failed")

button = driver.find_element_by_id('check1')
driver.execute_script("arguments[0].scrollIntoView();", button)
for i in range(2):
    if button.get_attribute('value') == 'Check All':
        button.click()
        print("Check All done")
    else:
        button.click()
        print("unCheck All done")

list_checkbox = driver.find_elements_by_class_name('checkbox')
for checkbox in list_checkbox:
    if checkbox.text == 'Option 3':
        checkbox.find_element_by_tag_name('input').click()
button = driver.find_element_by_id('check1')
if button.get_attribute('value') == 'Check All':
    print("Multi Checkbox Completed")
else: 
    print("Multi Checkbox Failed")
driver.close()
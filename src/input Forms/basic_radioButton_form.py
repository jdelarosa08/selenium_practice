import time
import os
from selenium import webdriver

#Excersice 2
src_win = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) + '\drivers\chromedriver.exe'
driver = webdriver.Chrome(executable_path=src_win)
driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
driver.maximize_window()
driver.implicitly_wait(8)

radio_buttons = driver.find_elements_by_name('optradio')
for radio_button in radio_buttons:
    if radio_button.get_attribute('value') == 'Male':
        radio_button.click()
        print('Male seleted')
        driver.find_element_by_id('buttoncheck').click()
        if driver.find_element_by_class_name('radiobutton').text == "Radio button 'Male' is checked":
            print("Radio Button Completed")
        else:
            print("Radio Button Failed")


driver.close()
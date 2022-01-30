from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# now we can access all the keyboard keys to automate,
# And we can always inspect modules class by pressing ctrl + b

driver = webdriver.Chrome('chromedriver.exe') # make sure driver path exists in both file directory
driver.maximize_window()
url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
driver.get(url = url)

driver.implicitly_wait(5)
# to get rid of pop-ups
try: # for no pop-ups
    close_popup = driver.find_element_by_class_name('at4-close')
    close_popup.click()
except:
    print('no pop-ups')

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

#sum1.send_keys(15) we can pass int without quotes
sum1.send_keys(Keys.NUMPAD1) # using keys
sum2.send_keys(Keys.NUMPAD1, Keys.NUMPAD5) # it sends 15

#not everytime we want to filter elements by class or id
# we can use css selector for different key value pair #tag   #key      #value
result_button = driver.find_element_by_css_selector('button[onclick = "return total()"]')
result_button.click() # refer CSS selectors reference in web   

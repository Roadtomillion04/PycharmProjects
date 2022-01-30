from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
driver.implicitly_wait(3)
driver.maximize_window()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

radio_element = driver.find_elements_by_class_name("radio-inline") # this is top class contains all buttons

for i in radio_element:
    radio_button = i.find_element_by_css_selector('input') # getting inside tag
    if radio_button.get_attribute('value') == 'Female':
        radio_button.click()

checked_button = driver.find_element_by_id('buttoncheck')
checked_button.click()
output_message = driver.find_element_by_class_name('radiobutton')
print(output_message.get_attribute('innerHTML'))

# group radio buttons
for i in radio_element:
    age_button = i.find_element_by_css_selector('input')
    if age_button.get_attribute('value') == '5 - 15':
        age_button.click()

get_values_button = driver.find_element_by_css_selector('button[onclick="getValues();"]')
get_values_button.click()
output = driver.find_element_by_class_name('groupradiobutton')
print(output.get_attribute('innerHTML'))
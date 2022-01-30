from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
#driver.implicitly_wait(5)
driver.maximize_window()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try:
    pop_up_element = driver.find_element_by_class_name("at4-close")
    pop_up_element.click()
except:
    print('no pop up skipping...')

checkbox_element = driver.find_element_by_css_selector('input[type="checkbox"]')
checkbox_element.click()

# group checkbox
check_all_button = driver.find_element_by_css_selector('input[type="button"]')
check_all_button.click()

buttons = driver.find_elements_by_class_name("checkbox") # top class of four buttons

for i in buttons:
    if "Option 2" in i.get_attribute('innerHTML'): # gets text from top class
        i.find_element_by_css_selector('input[type="checkbox"]').click() # finds and clicks inside top class

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
driver.implicitly_wait(3)
driver.maximize_window()

# single select
select_list_button = driver.find_element_by_id("select-demo")
select_list_button.click()
select_option = select_list_button.find_elements_by_css_selector('option')

for day in select_option:
    if day.get_attribute('value') == 'Friday':
        day.click()
output_message = driver.find_element_by_class_name("selected-value")
print(output_message.get_attribute('innerHTML'))


# multi select
from selenium.webdriver.common.keys import Keys
multi_select_list = driver.find_element_by_id("multi-select").find_elements_by_tag_name('option')

for city in multi_select_list:
    city.click()

get_all_selected_button = driver.find_element_by_id('printAll')
get_all_selected_button.click()

output_msg = driver.find_element_by_class_name('getall-selected')
print(output_msg.get_attribute('innerHTML'))
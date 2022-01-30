from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.seleniumeasy.com/test/input-form-demo.html')
driver.implicitly_wait(3)
driver.maximize_window()

form_container = driver.find_element_by_tag_name('fieldset')
title = form_container.find_element_by_tag_name('legend').get_attribute('innerHTML')
print(title)

forms = form_container.find_elements_by_class_name('has-feedback')#if keys have two values separated by spaces
print(len(forms))                                                    # we can pick either one of them


for form_name in forms:
    form_input = input(f" Enter {form_name.find_element_by_class_name('control-label').text}")
    form_name.find_element_by_css_selector('input[class="form-control"]').send_keys(form_input)




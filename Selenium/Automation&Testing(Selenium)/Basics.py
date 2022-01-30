from selenium import webdriver
#this allows to drive the web through code
#make sure to install mse driver here

edge_browser = webdriver.Edge('./msedgedriver.exe')

#Everytime we run it creates new instance of Microsoft Edge
edge_browser.maximize_window() # full screen
edge_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html') # opens the page for us
assert 'Selenium Easy Demo' in edge_browser.title, 'Wrong Title' # its title tag of html

#to capture elements of html
show_message_button = edge_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML')) # it grabs text inside <button> tag
assert 'Show Message' in edge_browser.page_source # page_source returns html version of webpage
#another way
user_button = edge_browser.find_element_by_css_selector('#get-input > .btn') # #refers id, >refers grab all child
print(user_button)

# to fill the prompt
user_message = edge_browser.find_element_by_id('user-message')
user_message.clear() # just to make sure nothing in input
inputs = 'I AM SUPER COOL'
user_message.send_keys(inputs) # sends inputs as user typing there

show_message_button.click() # clicks for us
output_message = edge_browser.find_element_by_id('display')
assert inputs in output_message.text

#edge_browser.close()

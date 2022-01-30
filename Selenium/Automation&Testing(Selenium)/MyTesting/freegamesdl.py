from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://www.freegamesdl.net/")
driver.implicitly_wait(5)
driver.maximize_window()

game_name = input('Enter game name: ')
search_box = driver.find_element_by_class_name('geekmag-searchtext')
search_box.send_keys(game_name)
submit_button = driver.find_element_by_css_selector('input[type="submit"]')
submit_button.click()
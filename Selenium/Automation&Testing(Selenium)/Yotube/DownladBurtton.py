from selenium import webdriver
# we need these 3 to use explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver.exe') # make sure driver path exists in both file directory
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html')
download_button = driver.find_element_by_id('downloadButton')
assert 'Start Download' in download_button.text

download_button.click()

#progress_label = driver.find_element_by_class_name('progress-label')
#print('Complete!' in progress_label.text) # it gives only start download..

#we need to use explicit wait
                               # waits this time to get True or False
WebDriverWait(driver = driver, timeout = 30).until(
    method = EC.text_to_be_present_in_element( # as name suggests looks for the expected text we gave below
            # BY. is another way of finding tags
            (By.CLASS_NAME, 'progress-bar'), # Element filtration
            'Complete!' # the expected text
    )
)



from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://admin-dev.goopter.com/')

# login
username_text = driver.find_element(By.NAME, 'username').send_keys('tomdev')
password_text = driver.find_element(By.NAME, 'password').send_keys('20230130')
driver.find_element(By.XPATH, "//button[text()='Login']").click()

time.sleep(3)

# From the left panel of Admin main page, click Settings
driver.find_element(By.XPATH, '//li[@class="ant-menu-item"][.//span/text()="Settings"]').click()
# title_line = driver.find_element(By.CLASS_NAME, 'wrapper-title-line').text
# assert 'Settings Overview' in title_line, '"Settings" page is not displayed.'

time.sleep(3)

# Go to Discount Settings and click Edit button
driver.find_element(By.XPATH, '//div[@class="setting-card"][./div[@class="setting-card-title"]/text()="Discount Settings"]').click()

driver.find_element(By.XPATH, "//button[contains(text(),'Create Discount Code')]").click()

driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[@class="payment-subtitle"][contains(text(), "Discount Name")]/../input').send_keys('Clearance Sale')

driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[@class="payment-subtitle"][contains(text(), "Discount Code")]/../input').send_keys('20230309')

#delete_icon = driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[@class="payment-subtitle"][contains(text(), "Start Date")]/..//span[@role="img"]')
#driver.execute_script('arguments[0].click();', delete_icon)
start_date = driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[@class="payment-subtitle"][contains(text(), "Start Date")]/..//input')
#start_date.clear()
time.sleep(3)
#start_date.send_keys('2023-01-23')

driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div/input').send_keys('2023-03-09')

button1 = driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[contains(@class, "payment-subtitle")][contains(text(), "Publicly Available")]/../button')
if button1.get_attribute('aria-checked') == 'false':
    button1.click()

button2 = driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[contains(@class, "payment-subtitle")][contains(text(), "Enable")]/../button')
if button2.get_attribute('aria-checked') == 'false':
    button2.click()

driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[contains(@class, "payment-subtitle")][contains(text(), "Uses Per Coupon")]/../input').send_keys('5')
driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[contains(@class, "payment-subtitle")][contains(text(), "Uses Per Customer")]/../input').send_keys('2')

driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[contains(@class, "payment-subtitle")][contains(text(), "Discount Type")]/../div[contains(@class, "ant-select-single")]').click()
time.sleep(1)   # This wait is required
options = driver.find_elements(By.XPATH, '//div[@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]')
for option in options:
    if option.text == 'Fixed amount discount for whole cart':
        option.click()
        break

driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[contains(@class, "payment-subtitle")][contains(text(), "Discount Value")]/../input').send_keys('9')
driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[contains(@class, "payment-subtitle")][contains(text(), "Minimum Order Amount Limit")]/../input').send_keys('4')

driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[contains(@class, "payment-subtitle")][contains(text(), "Discount Rule")]/../div[contains(@class, "ant-select-single")]').click()
time.sleep(1)   # This wait is required
options = driver.find_elements(By.XPATH, '//div[@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]')
for option in options:
    if option.text == 'Apply to all':
        option.click()
        break


time.sleep(5)

driver.find_element(By.XPATH, '//button[text()="Save Discount Code"]').click()

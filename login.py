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
driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

time.sleep(3)

# From the left panel of Admin main page, click Settings
driver.find_element(By.XPATH, '//li[@class="ant-menu-item"][.//span/text() = "Settings"]').click()
title_line = driver.find_element(By.CLASS_NAME, 'wrapper-title-line').text
assert 'Settings Overview' in title_line, '"Settings" page is not displayed.'

time.sleep(3)

# Choose General and click Edit button
driver.find_element(By.XPATH, '//div[@class="setting-card"][./div[@class="setting-card-title"]/text() = "General"]').click()


time.sleep(3)

# Click the forth section 'Business Features'
tab = driver.find_element(By.XPATH, '//div[@class="ant-tabs-tab"][./div[@class="ant-tabs-tab-btn"]/text() = "Business Features"]')
actions = ActionChains(driver)
actions.move_to_element(tab)
actions.move_to_element_with_offset(tab, 1, 10)
actions.click()
actions.perform()

time.sleep(3)
#driver.find_element(By.XPATH, '//div[@class="ant-tabs-tab"][./div[@class="ant-tabs-tab-btn"]/text() = "Business Features"]').click()

# Parking - Paid
parking = driver.find_element(By.XPATH,
                              '//*[@id="general-settings has-floating-submit_parking"]/label[3]/span[1]/input').click()

time.sleep(3)

# Restaurant Extras - Alcohol
alcohol = driver.find_element(By.XPATH,
                              '//*[@id="general-settings has-floating-submit"]/div[2]/div[2]/table/tbody/tr[1]/td/span/div/div/div/div/div/div/div/span[2]')
alcohol.select_by_visible_text('Beer & Wine Only')

# Restaurant Extras - Noise Level
noise_level = driver.find_element(By.XPATH,
                                  '//*[@id="general-settings has-floating-submit"]/div[2]/div[2]/table/tbody/tr[2]/td/span/div/div/div/div/div/div/div/span[2]')
noise_level.select_by_visible_text('Average')

# Restaurant Extras - Environment
environment = driver.find_element(By.XPATH,
                                  '//*[@id="general-settings has-floating-submit"]/div[2]/div[2]/table/tbody/tr[3]/td/span/div/div/div/div/div/div/div/span[2]')
environment.select_by_visible_text('Classy')

# Attire
environment = driver.find_element(By.XPATH,
                                  '//*[@id="general-settings has-floating-submit"]/div[2]/div[2]/table/tbody/tr[12]/td/span/div/div/div/div/div/div/div/span[2]')
environment.select_by_visible_text('Casual')

# save button
save_btn = driver.find_element(By.XPATH, '//*[@id="general-settings"]/div[2]/button[2]').click()

# cancel button
cancel = driver.find_element(By.XPATH, '//*[@id="general-settings"]/div[2]/button[1]').click()

driver.quit()

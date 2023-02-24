from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://admin-dev.goopter.com/')

# login

username_text = driver.find_element(By.NAME, 'username')
username_text.send_keys('tomdev')

password_text = driver.find_element(By.NAME, 'password')
password_text.send_keys('20230130')

login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/form/div/div[3]/div/div/div/button').click()

time.sleep(3)

# sidebar element

element = driver.find_element(By.XPATH,
                              '/html/body/div[1]/div/section/section/aside[2]/div/div/div[2]/ul/li[16]/span[2]').click()

time.sleep(7)

# edit - General
edit_btn = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div/section/section/main/div[2]/div[2]/div[1]/div[3]/div[2]').click()

time.sleep(3)

# Business Features
basic_btn = driver.find_element(By.XPATH, '//*[@id="rc-tabs-0-tab-business_features"]').click()

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

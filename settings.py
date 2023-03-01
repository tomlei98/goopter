from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
a_tag = driver.find_element(By.CSS_SELECTOR, 'a[href="/settings"]')
a_tag.find_element(By.XPATH, '../..').click()

time.sleep(7)

# Choose Public Notice click Edit button
driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div[2]/div[2]/div[3]/div[3]/div[2]').click()

time.sleep(3)

# In text box, do edit operation to update notice
input_field = driver.find_element(By.CLASS_NAME, 'ant-input')
input_field.clear()
input_field.send_keys('Order is delivered')

time.sleep(3)

# Click Add button to add new order type and notice
driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div[2]/div/div[5]/button').click()

dropdown_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div[2]/div/div[6]/div/div')
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text('Pick Up')
driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div[2]/div/div[7]/span/textarea').send_keys('Pick up Order')
time.sleep(3)

# Click delete button to directly delete notice
driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div[2]/div/div[8]/button[1]').click()

# Save changes button
driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div[2]/div/div[9]/button').click()

time.sleep(3)
# Cancel button
driver.find_element(By.CLASS_NAME, 'anticon anticon-arrow-left').click()

driver.quit()

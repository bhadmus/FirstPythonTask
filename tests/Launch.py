from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from values import strings

driver = webdriver.Chrome()
driver.get(strings.url)
driver.maximize_window()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="nav-link-accountList"]/span[1]')))
time.sleep(3)
driver.find_element_by_xpath(strings.open_sign_in).click()
time.sleep(5)
driver.find_element_by_id(strings.username).send_keys(strings.email)
time.sleep(5)
check_button = driver.find_element_by_id(strings.proceed)
if check_button:
    check_button.click()
    time.sleep(3)
driver.find_element_by_id(strings.password).send_keys(strings.pwd)
time.sleep(5)
driver.find_element_by_id().click()
time.sleep(5)
driver.find_element_by_id(strings.proceed).click()
otp_request = driver.find_element_by_xpath(strings.otp)
assert otp_request.text == 'Enter OTP'

driver.close()

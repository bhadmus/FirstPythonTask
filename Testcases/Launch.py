from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(r"C:\Users\Ademola Bhadmus\Documents\PyCharm Projects\Sample\drivers\chromedriver.exe")
driver.get("https://www.amazon.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[1]').click()
driver.find_element_by_id("ap_email").send_keys("ademolabhadmus@hotmail.com")
time.sleep(2)
driver.find_element_by_id("ap_password").send_keys("********")
time.sleep(1)
driver.find_element_by_id("signInSubmit").click()
time.sleep(5)
driver.execute_script("window.scrollTo(0,120)")
posToHover = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[1]')
hover = ActionChains(driver).move_to_element(posToHover).perform()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="nav-item-signout-sa"]/span').click()
time.sleep(4)
driver.close()

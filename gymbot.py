
import selenium
from selenium import webdriver
import time


#change the path below
#possibly may have to configure version of chrome or driver version
driver = webdriver.Chrome("C:/Users/PC/Desktop/chromedriver_win32/chromedriver.exe")

driver.get('https://shop.westernmustangs.ca/Program/GetProgramDetails?courseId=12a6983e-7702-417e-8710-9181df03dea0&semesterId=81dac0e7-2456-44c9-bfe4-6ed494cc6824')

driver.find_element_by_id('loginLink').click()

time.sleep(0.75)

local_button = driver.find_element_by_class_name('loginOption.btn.btn-lg.btn-block.btn-social.btn-primary')


local_button.click()

id_box = driver.find_element_by_name('Username')
pass_box = driver.find_element_by_name('Password')

id_box.send_keys('Enter Username Here')
pass_box.send_keys("Enter Password Here")


driver.find_element_by_id('btnLogin').click()

time.sleep(0.75)

driver.find_element_by_id('gdpr-cookie-accept').click()

driver.switch_to_window(driver.window_handles[0])

driver.find_element_by_class_name('btn.btn-primary').click()

driver.switch_to_window(driver.window_handles[0])

time.sleep(0.75)

driver.find_element_by_xpath("//a[text()='Continue']").click()
driver.find_element_by_xpath("//button[text()='Add to Cart']").click()


driver.find_element_by_name('CustomPrompts[0].CommonInput').click()
driver.find_element_by_name('CustomPrompts[1].CommonInput').click()

driver.find_element_by_name('CustomPrompts[2].CommonInput').click()

driver.find_element_by_name('CustomPrompts[4].CommonInput').click()


driver.find_element_by_xpath("//button[text()='Add to Cart']").click()

driver.find_element_by_id("checkoutButton").click()

driver.switch_to_window(driver.window_handles[0])

time.sleep(0.75)

driver.find_element_by_xpath('//*[@id="CheckoutModal"]/div/div[2]/button[2]').click()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

dpath = "D:\\frigdrivers\\chrome80driver\\chromedriver.exe"
pwd = open("D:\\frigdrivers\\pass\\notthepassword.txt", "r").readline()
driver = webdriver.Chrome(dpath)

driver.get("https://discord.com/login")
#driver.get("https://discord.com/channels/@me/551246526924455937")

time.sleep(1)
driver.find_element_by_name("email").send_keys("21438709a@gmail.com")
driver.find_element_by_name("password").send_keys(pwd)
driver.find_element_by_css_selector('[type=submit]').click()

time.sleep(5)
driver.find_element_by_css_selector('[data-list-item-id="private-channels-uid_372___551246526924455937]').click()

time.sleep(5)
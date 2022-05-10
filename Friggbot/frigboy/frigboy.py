from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, bot



dpath = "D:\\frigdrivers\\chrome80driver\\chromedriver.exe"
pwd = open("D:\\frigdrivers\\pass\\notthepassword.txt", "r").readline()
driver = webdriver.Chrome(dpath)

driver.get("https://discord.com/login")

time.sleep(.5)
driver.find_element_by_name("email").send_keys("21438709a@gmail.com")
driver.find_element_by_name("password").send_keys(pwd)
driver.find_element_by_css_selector('[type=submit]').click()

time.sleep(3)
driver.find_element_by_css_selector('.subtext-14b69p').click()
time.sleep(.3)


frig = bot.bot(driver)

while 1:
    frig.readLast()
    #print(f"{frig.lastSeen.content}, sent by {frig.lastSeen.sender} at {frig.lastSeen.time}")
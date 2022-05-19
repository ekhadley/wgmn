from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, bot, os

if "ekhad" in os.listdir("C:\\Users"):
    dpath = "C:\\Users\\ekhad\\Desktop\\frig\\chrome101\\chromedriver.exe"
    pwd = open("C:\\Users\\ekhad\\Desktop\\frig\\notthepassword.txt", "r").readline()
else:
    dpath = "D:\\frigdrivers\\chrome80driver\\chromedriver.exe"
    pwd = open("D:\\frigdrivers\\pass\\notthepassword.txt", "r").readline()

driver = webdriver.Chrome(dpath)
driver.get("https://discord.com/login")

time.sleep(.5)
driver.find_element_by_name("email").send_keys("21438709a@gmail.com")
driver.find_element_by_name("password").send_keys(pwd)
driver.find_element_by_css_selector('[type=submit]').click()

time.sleep(3)
while 1:
    try:
        driver.find_element_by_css_selector('.overflow-1wOqNV').click()
        break
    except:
        time.sleep(.5)

time.sleep(.3)


frig = bot.bot(driver)
print("friggbot initiated . . .")
while 1:
    frig.readLast()
    frig.intro()
    print(frig.online)
    #print(f"{frig.lastSeen.content}, sent by {frig.lastSeen.sender} at {frig.lastSeen.time}")
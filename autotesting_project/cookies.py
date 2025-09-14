import  json
import time
import os.path
from cookies_manager import CookieManager
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
BUTTON_FIELD = ("xpath", "//button[@id='loginformsubmit']")

cookie_manager = CookieManager(driver)

if os.path.exists("cookies.json"):
    cookie_manager.load()
else:
    driver.find_element(*LOGIN_FIELD).send_keys("hotdogg90@mail.ru")
    driver.find_element(*PASSWORD_FIELD).send_keys("qwerty123")
    driver.find_element(*BUTTON_FIELD).click()
    cookie_manager.save()

time.sleep(5)









# # driver.delete_all_cookies()
#
# LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# BUTTON_FIELD = ("xpath", "//button[@id='loginformsubmit']")
#
# driver.find_element(*LOGIN_FIELD).send_keys("hotdogg90@mail.ru")
# driver.find_element(*PASSWORD_FIELD).send_keys("qwerty123")
# driver.find_element(*BUTTON_FIELD).click()
#
# cookies = driver.get_cookies()
# driver.delete_all_cookies()
#
# with open("cookies.json", "w") as file:
#     json.dump(cookies, file, indent=4)
#
#
#
# with open("cookies.json", "r") as file:
#     cookies = json.load(file)
# for cookie in cookies:
#     driver.add_cookie(cookie)
#
# driver.refresh()
#
#
# time.sleep(3)
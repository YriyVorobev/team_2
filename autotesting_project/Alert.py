import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
wait = WebDriverWait(driver,7,poll_frequency=1)

driver.find_element("xpath","//button[@id='promtButton']").click()
alert = wait.until(EC.alert_is_present())
time.sleep(3)
alert.send_keys("Yriy")
time.sleep(3)
alert.accept()
time.sleep(3)

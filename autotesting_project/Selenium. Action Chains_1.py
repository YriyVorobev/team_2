import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://demoqa.com/menu")
wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)

MAIN_2_ITEM = ("xpath", "//a[text()='Main Item 2']")
SUB_LIST = ("xpath", "//a[text()='SUB SUB LIST »']")
SUB_ITEM_2 = ("xpath", "//a[text()='Sub Sub Item 2']")

STEP_1 = driver.find_element(*MAIN_2_ITEM)
STEP_2 = driver.find_element(*SUB_LIST)
STEP_3 = driver.find_element(*SUB_ITEM_2)

action.move_to_element(STEP_1).move_to_element(STEP_2).move_to_element(STEP_3).perform()


time.sleep(3)
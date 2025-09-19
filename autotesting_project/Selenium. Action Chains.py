import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)

DOUBLE_BUTTON_CLICK = ("xpath", "//button[@id = 'doubleClickBtn']")
RIGHT_BUTTON_CLICK = ("xpath", "//button[@id = 'rightClickBtn']")
CLICK_ME_BUTTON = ("xpath", "//button[text()= 'Click Me']")

double_click = driver.find_element(*DOUBLE_BUTTON_CLICK)
action.double_click(double_click).perform()

time.sleep(2)

right_click = driver.find_element(*RIGHT_BUTTON_CLICK)
action.context_click(right_click).perform()

time.sleep(2)

click_me = driver.find_element(*CLICK_ME_BUTTON)
action.click(click_me).perform()

time.sleep(2)


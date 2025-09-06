

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")
wait = WebDriverWait(driver,10, poll_frequency=1)
VISIBLE_5_SECOND_AFTER = ("xpath", "//button[@id = 'visibleAfter']")
ENABLE_AFTER = ("xpath","//button[@id = 'enableAfter']")
#Ожидаем, что элемент присутствует в DOM и виден визуально так же имеет высоту ширину больше 0.
wait.until(EC.visibility_of_element_located(VISIBLE_5_SECOND_AFTER))
#Ожидаем что элемент становиться кликабельным и кликаем по нему.
wait.until(EC.element_to_be_clickable(ENABLE_AFTER)).click()


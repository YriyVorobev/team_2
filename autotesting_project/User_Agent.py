import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = webdriver.ChromeOptions()
# Сменили юзер агента(устройство с которого мы заходим)
options.add_argument("--user-agent=Mozilla/5.0 (Android 10; Mobile; rv:141.0) Gecko/141.0 Firefox/141.0")
# Подкинули опции, для отключения автоматических функций, которые могут выдавать как бота.
options.add_argument("--disable-blink-features=AutomationControlled")
# Подкинули параметр, который исключает автоматизацию расширений, отключает уведомления об использовании автоматизации.
options.add_experimental_option("excludeSwitches",["enable-automation"])
# Опция больше идет как доп к предыдущей.
options.add_experimental_option("useAutomationExtension",False)
# Опция с портом если вдруг что не будет открывать страницу
options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(options=options)
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")

time.sleep(5)
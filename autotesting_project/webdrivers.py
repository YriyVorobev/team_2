import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://hyperskill.org/")

page_url = driver.current_url
print(page_url)



# driver.get("https://www.saucedemo.com")


# //a[@class='button-outline w-inline-block']




import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
action = ActionChains(driver)

USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")

CLICK_BUTTON = ("xpath","//input[@id='login-button']")
ADD_BUTTON = ("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
ADD_BUTTON_TSHIRT = ("xpath", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
ADD_BUTTON_JACKET = ("xpath", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
BASKET_BUTTON = ("xpath", "//div[@id='shopping_cart_container']")
CHECKOUT = ("xpath", "//button[@id='checkout']")
CONTINUE_BUTTON = ("xpath", "//input[@id='continue']")
FINISH_BUTTON = ("xpath", "//button[@id = 'finish']")

FIRST_NAME_FIELD = ("xpath", "//input[@id='first-name']")
LAST_NAME_FIELD = ("xpath", "//input[@id='last-name']")
POSTAL_CODE = ("xpath", "//input[@id='postal-code']")

assert "https://www.saucedemo.com/" in driver.current_url

user_name = driver.find_element(*USERNAME_FIELD)
user_name.send_keys("standard_user")

password_key = driver.find_element(*PASSWORD_FIELD)
password_key.send_keys("secret_sauce")

click_button = driver.find_element(*CLICK_BUTTON)
action.click(click_button).perform()

assert "https://www.saucedemo.com/inventory.html" in driver.current_url

add_button = driver.find_element(*ADD_BUTTON)
action.click(add_button).perform()
time.sleep(3)
add_button_tshirt = driver.find_element(*ADD_BUTTON_TSHIRT)
action.click(add_button_tshirt).perform()
time.sleep(3)
add_button_jacket = driver.find_element(*ADD_BUTTON_JACKET)
action.click(add_button_jacket).perform()

basket_button = driver.find_element(*BASKET_BUTTON)
action.click(basket_button).perform()

assert "https://www.saucedemo.com/cart.html" in driver.current_url

checkout_button = driver.find_element(*CHECKOUT)
action.click(checkout_button).perform()

assert "https://www.saucedemo.com/checkout-step-one.html" in driver.current_url

first_name = driver.find_element(*FIRST_NAME_FIELD)
first_name.send_keys(Keys.COMMAND + "A")
first_name.send_keys(Keys.BACKSPACE)

assert first_name.get_attribute("value") == ""

first_name.send_keys("NameSpace")
first_name_field = first_name.get_attribute("value")
time.sleep(3)
assert "NameSpace" in first_name_field

last_name = driver.find_element(*LAST_NAME_FIELD)
last_name.send_keys(Keys.COMMAND + "A")
last_name.send_keys(Keys.BACKSPACE)

assert last_name.get_attribute("value") == ""

last_name.send_keys("Universe")
last_name_field = last_name.get_attribute("value")
time.sleep(3)
assert "Universe" in last_name_field

postal_code = driver.find_element(*POSTAL_CODE)
postal_code.send_keys(Keys.COMMAND + "A")
postal_code.send_keys(Keys.BACKSPACE)

assert postal_code.get_attribute("value") == ""

postal_code.send_keys("323455")
postal_code_field = postal_code.get_attribute("value")
time.sleep(3)
assert "323455" in postal_code_field

continue_button = driver.find_element(*CONTINUE_BUTTON)
action.click(continue_button).perform()

assert "https://www.saucedemo.com/checkout-step-two.html" in driver.current_url

finish_button = driver.find_element(*FINISH_BUTTON)
action.click(finish_button).perform()

assert "https://www.saucedemo.com/checkout-complete.html" in driver.current_url




time.sleep(5)
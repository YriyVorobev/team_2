import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
# check_box
driver = webdriver.Chrome()
# driver.get("https://demoqa.com/checkbox")
#
# CHECK_BOX_BUTTON = ("xpath", "//label[@for='tree-node-home']")
#
# driver.find_element(*CHECK_BOX_BUTTON).click()


# RADIO_BUTTON
# driver.get("https://demoqa.com/radio-button")

# # RADIO_BUTTON_YES = ("xpath", "//input[@id='yesRadio']")
# RADIO_YES_LABEL = ("xpath", "//label[@for='yesRadio']")
#
# RADIO_BUTTON_IMPRESSIVE = ("xpath", "//input[@id='impressiveRadio']")
# RADIO_BUTTON_NO = ("xpath", "//input[@id='noRadio']")
#
# # print(driver.find_element(*RADIO_BUTTON_NO).is_enabled())
#
# driver.find_element(*RADIO_YES_LABEL).click()

driver.get("https://demoqa.com/select-menu")

DROPDOWN_ELEMENT = ("xpath", "//select[@id='oldSelectMenu']")
SELECT_CARS = ("xpath", "//select[@id='cars']")
MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")

dropdown = Select(driver.find_element(*DROPDOWN_ELEMENT))
dropdown.select_by_value("red")

select_cars = Select(driver.find_element(*SELECT_CARS))
select_cars.select_by_value("saab")

multiselect = driver.find_element(*MULTISELECT)
multiselect.send_keys("Green")
assert multiselect.get_attribute("value") == "Green", "Error in value Green"

multiselect.send_keys(Keys.ENTER)

multiselect = driver.find_element(*MULTISELECT)
multiselect.send_keys("Blue")
assert multiselect.get_attribute("value") == "Blue", "Error in value Blue"

multiselect.send_keys(Keys.ENTER)

multiselect = driver.find_element(*MULTISELECT)
multiselect.send_keys("Black")
assert multiselect.get_attribute("value") == "Black", "Error in value Black"

multiselect.send_keys(Keys.ENTER)

multiselect = driver.find_element(*MULTISELECT)
multiselect.send_keys("Red")
assert multiselect.get_attribute("value") == "Red", "Error in value Red"

multiselect.send_keys(Keys.ENTER)
multiselect.send_keys(Keys.BACKSPACE)

multiselect.send_keys(Keys.ESCAPE)

time.sleep(3)



from selenium import webdriver
from selenium.webdriver import Keys
import time
#Открываем браузер с сайтом "https://demoqa.com/text-box"
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

# находим поле ввода userName сохраняем в переменную
input_name = driver.find_element("xpath","//input[@id='userName']")

# чистим поле, с помощью команд, выделяем и очищаем
input_name.send_keys(Keys.COMMAND + "A")
input_name.send_keys(Keys.BACKSPACE)

# проверяем что поля пустые
assert input_name.get_attribute("value") == ""

# заполняем поле userName "Rick"
input_name.send_keys("Rick")

# Проверяем что внутри теперь "Rick"
input_name_field = input_name.get_attribute("value")
assert "Rick" in input_name_field

# находим поле ввода userEmail сохраняем в переменную
input_email = driver.find_element("xpath","//input[@id='userEmail']")

# чистим поле с помощью команд, выделяем и очищаем
input_email.send_keys(Keys.COMMAND + "A")
input_email.send_keys(Keys.BACKSPACE)

# проверяем что поле пустое
assert input_email.get_attribute("value") == ""

# заполняем поле userEmail
input_email.send_keys("hotdogg@mail.com")
email_field = input_email.get_attribute("value")

#проверяем что внутри поля теперь hotdogg@mail.com
assert "hotdogg@mail.com" in email_field

current_address = driver.find_element("xpath","//textarea[@id='currentAddress']")

current_address.send_keys(Keys.COMMAND + "A")
current_address.send_keys(Keys.BACKSPACE)

assert current_address.get_attribute("value") == ""

current_address.send_keys("g.Krasnodar st.Kirov 23")
current_address_field= current_address.get_attribute("value")

assert "g.Krasnodar st.Kirov 23" in current_address_field

permanent_address = driver.find_element("xpath","//textarea[@id='permanentAddress']")

permanent_address.send_keys(Keys.COMMAND +"A")
permanent_address.send_keys(Keys.BACKSPACE)

assert permanent_address.get_attribute("value") == ""

permanent_address.send_keys("g.Krasnodar st.Lenina 13")
permanent_address_field = permanent_address.get_attribute("value")

assert "g.Krasnodar st.Lenina 13" in permanent_address_field


time.sleep(5)




# //input[@id='userName']
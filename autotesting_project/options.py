import time

from selenium import webdriver

options = webdriver.ChromeOptions()
"""
 Создали объект для опции и объявили первую опцию внутри кавычек содержится наша опция
 Безголовый режим (--headless и --headless=new) - Работает в фоне без GUI
 Режим инкогнито (--incognito) - Не использует кэш и cookies
 Игнорирование SSL-ошибок (--ignore-certificate-errors) - Тестирование на тестовых/staging окружениях
 Установка размера окна (--window-size=X,Y) - Важно для тестирования адаптивности
 (--disable-cache) - Отключение кэширования.Тестирование свежего контента,
 Проверка обновлений ресурсов,Отладка проблем с кэшированием
"""
# options.add_argument("--headless")
# options.add_argument("--incognito")
# options.add_argument("--ignor-certificate-errors")
options.add_argument("--window-size=1920,1080")
# options.add_argument("--disable-cache")
driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/upload-download")

upload_file_field = driver.find_element("xpath","//input[@id='uploadFile']")
upload_file_field.send_keys(r"/Users/vorobev-yua/PycharmProjects/team2/autotesting_project/get_file.png")

time.sleep(3)



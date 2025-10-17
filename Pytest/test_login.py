from selenium import webdriver
import pytest

class TestLogin:

    def test_open_login_page(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        # assert driver.current_url == "https://www.google.com/", "Открыта некорректная страница"



class TestDemoqa:

    def setup_method(self):
        print("Открытие браузера")
        self.driver = webdriver.Chrome()

    def test_login_page(self):
        self.driver.get("https://demoqa.com/login")
        # assert driver.current_url == "https://demoqa.com/login", "Открыта некорректная страница"

    def teardown_method(self):
        self.driver.close()
        print("Выход из браузера")

class TestTextbox:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        print("Open URL")

    def test_text_box(self):
        self.driver.get("https://demoqa.com/text-box")
        # assert driver.current_url == "https://demoqa.com/text-box", "Открыта некорректная страница"

    def teardown_method(self):
        self.driver.close()
        print("Quit url")



import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os


USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
CLICK_BUTTON = ("xpath","//input[@id='login-button']")



@pytest.fixture(scope="class",autouse=True)

def driver(request):

    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option(
    "prefs",
    {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
    )

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class",autouse=True)
def credentials(request):
    request.cls.username = "standard_user"
    request.cls.password = "secret_sauce"

@pytest.fixture(scope="class",autouse=True)
def login_in(request,driver,credentials):
    driver = request.cls.driver
    driver.get("https://www.saucedemo.com/")



@pytest.fixture(scope="session",autouse=True)
def setup_environment_properties():
    properties = {
        "STAGE": os.environ["AQA"],
        "BROWSER": os.environ["BROWSER"],
        "MR": os.environ["MR"]
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")


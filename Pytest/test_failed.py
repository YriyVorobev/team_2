import pytest
import allure
from allure_commons.types import Severity


@allure.epic("Accounts")
@allure.feature("Login")
@allure.story("Profile")
@pytest.mark.usefixtures("driver")

class TestLogin:

    @pytest.mark.regression
    @allure.title("open_login_page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com",name="Documentation_1")
    def test_open_login_page(self,driver):

        with allure.step("Open page. step 1"):
            self.driver.get("https://demoqa.com/login")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Login page",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Open page. step 2"):
            assert self.driver.current_url == "https://demoqa.com/login", "ошибка в открытие сайта логина"

    @pytest.mark.sanity
    @allure.title("open_books_page")
    @allure.severity(Severity.BLOCKER)
    @allure.link(url="https://confluence.org",name="Documentation_2")
    def test_open_books_page(self,driver):

        with allure.step("Open books page. step 1"):
            self.driver.get("https://demoqa.com/books")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Books page",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Open books page. step 2"):
            assert self.driver.current_url == "https://demoqa.com/books", "Ошибка открытия сайта книги"

    @pytest.mark.smoke
    @pytest.mark.sanity
    @allure.title("open_profile_page")
    @allure.severity(Severity.MINOR)
    @allure.link(url="https://confluence.org",name="Documentation_3")
    def test_open_profile_page(self,driver):

        with allure.step("Open profile page. Step 1"):
            self.driver.get("https://demoqa.com/profile")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Profile page",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Open profile page. Step 2"):
            assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка открытия сайта профиль"





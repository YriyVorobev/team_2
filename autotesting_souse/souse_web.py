import pytest
import allure
from allure_commons.types import Severity
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")

CLICK_BUTTON = ("xpath","//input[@id='login-button']")
ADD_BUTTON = ("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
ADD_BUTTON_TSHIRT = ("xpath", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
ADD_BUTTON_JACKET = ("xpath", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
BASKET_BUTTON = ("xpath", "//div[@id='shopping_cart_container']")
CHECKOUT = ("xpath", "//button[@data-test='checkout']")
CONTINUE_BUTTON = ("xpath", "//input[@id='continue']")
FINISH_BUTTON = ("xpath", "//button[@id = 'finish']")

FIRST_NAME_FIELD = ("xpath", "//input[@id='first-name']")
LAST_NAME_FIELD = ("xpath", "//input[@id='last-name']")
POSTAL_CODE = ("xpath", "//input[@id='postal-code']")



@allure.epic("Accounts")
@allure.feature("Login")
@allure.story("Profile")
@pytest.mark.usefixtures("driver","credentials")
class TestLogin:

    @pytest.mark.regression
    @allure.title("Login in sauce")
    @allure.severity(Severity.BLOCKER)
    @allure.link(url="https://www.confluence.com",name="Documentation_1")
    def test_login(self):

        with allure.step("Login in saucedemo,step_1"):
            self.driver.get("https://www.saucedemo.com/")
            user_name = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(USERNAME_FIELD))
            password_key = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(PASSWORD_FIELD))

        with allure.step("Login in saucedemo,step_2"):
            user_name.send_keys(self.username)
            password_key.send_keys(self.password)

        with allure.step("correct URL, step_3"):
            assert self.driver.current_url == "https://www.saucedemo.com/"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="userpass screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Login in user,step_4"):
            assert user_name.get_attribute("value") == self.username
            assert password_key.get_attribute("value") == self.password

        with allure.step("login in password,step_5"):
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="password screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Login in saucedemo,step_6"):
            button_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(CLICK_BUTTON))
            button_click.click()


    @pytest.mark.usefixtures("login_in")
    @pytest.mark.regression
    @allure.title("Inventory")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://www.confluence.com", name="Documentation_1")
    def test_product_add(self):

        with allure.step("product_selection,step_1"):
            WebDriverWait(self.driver, 10).until(EC.url_contains("/inventory.html"))
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(ADD_BUTTON)).click()
            self.driver.find_element(*ADD_BUTTON_JACKET).click()
            self.driver.find_element(*ADD_BUTTON_TSHIRT).click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="product selection screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("product selection,step_2"):
            assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.usefixtures("login_in")
    @pytest.mark.regression
    @allure.title("In Basket")
    @allure.severity(Severity.NORMAL)
    def test_basket(self):
        with allure.step("Basket selection,step_1"):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BASKET_BUTTON)).click()
            WebDriverWait(self.driver, 10).until(EC.url_contains("/cart.html"))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Cart_art",
                attachment_type=allure.attachment_type.PNG)

        with allure.step("Cart selection,step_2"):
            assert self.driver.current_url == "https://www.saucedemo.com/cart.html"

    @pytest.mark.usefixtures("login_in")
    @pytest.mark.regression
    @allure.title("In Basket")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://www.confluence.com", name="Documentation_1")
    def test_checkout(self):

        with allure.step("checkout, step_1"):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CHECKOUT)).click()
            WebDriverWait(self.driver, 10).until(EC.url_contains("/checkout-step-one.html"))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="checkout step2",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("checkout_assert, step_2"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

        with allure.step("checkout_field_first, step_3"):
            first_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(FIRST_NAME_FIELD))
            first_name.send_keys(Keys.COMMAND + "A")
            first_name.send_keys(Keys.BACKSPACE)

        with allure.step("checkout_field_first, step_4"):
            assert first_name.get_attribute("value") == ""

        with allure.step("checkout_field_first, step_5"):
            first_name.send_keys("Hookah")

        with allure.step("checkout_field_first, step_6"):
            assert first_name.get_attribute("value") == "Hookah"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="checkout_field_first_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("checkout_field_last, step_3"):
            last_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LAST_NAME_FIELD))
            last_name.send_keys(Keys.COMMAND + "A")
            last_name.send_keys(Keys.BACKSPACE)

        with allure.step("checkout_field_last, step_4"):
            assert last_name.get_attribute("value") == ""

        with allure.step("checkout_field_last, step_5"):
            last_name.send_keys("Universe")

        with allure.step("checkout_field_last, step_6"):
            assert last_name.get_attribute("value") == "Universe"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="checkout_field_last_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("checkout_field_zip, step_7"):
            zip_code = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(POSTAL_CODE))
            zip_code .send_keys(Keys.COMMAND + "A")
            zip_code .send_keys(Keys.BACKSPACE)

        with allure.step("checkout_field_zip, step_8"):
            assert zip_code.get_attribute("value") == ""

        with allure.step("checkout_field_zip, step_9"):
            zip_code.send_keys("324590")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="checkout_zip_field_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("checkout_field_zip, step_10"):
            assert zip_code.get_attribute("value") == "324590"

    @pytest.mark.usefixtures("login_in")
    @pytest.mark.regression
    @allure.title("continue")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://www.confluence.com", name="Documentation_1")
    def test_continue(self):

        with allure.step("continue, step_1"):
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(CONTINUE_BUTTON)).click()
            WebDriverWait(self.driver,10).until(EC.url_contains("/checkout-step-two.html"))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="continue step_1",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("continue, step_2"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

        with allure.step("continue, step_3"):
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(FINISH_BUTTON)).click()
            WebDriverWait(self.driver,10).until(EC.url_contains("/checkout-complete.html"))
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="continue step_4",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("continue, step_5"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"















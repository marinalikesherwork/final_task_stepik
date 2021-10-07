from .base_page import BasePage
from .locators import LoginPageLocators
import math
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
        
    def register_new_user(self, email, password):
        #email = str(time.time()) + "@fakemail.org"
        #password = "123456789"
        email_field = self.browser.find_element(*LoginPageLocators.USER_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.USER_PASSWORD)
        password2_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password2_field.send_keys(password)
        button.click()        
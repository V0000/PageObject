from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Incorrect login url '

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Registration form is not present'

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.input_text_to_field(*LoginPageLocators.EMAIL_REGISTRATION_FIELD, email)
        self.input_text_to_field(*LoginPageLocators.PASSWORD_REGISTRATION_FIELD, password)
        self.input_text_to_field(*LoginPageLocators.REPEAT_PASSWORD_REGISTRATION_FIELD, password)
        self.click_on_element(*LoginPageLocators.SUBMIT_REGISTRATION_BUTTON)

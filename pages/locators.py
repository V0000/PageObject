from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_REGISTRATION_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTRATION_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_PASSWORD_REGISTRATION_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    SUBMIT_REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p.price_color')
    MASSAGE_ABOUT_SUCCESS_ADD_TO_BUSKED = (By.CSS_SELECTOR, '#messages>.alert:nth-child(1)>.alertinner>strong')
    MASSAGE_ABOUT_BUSKED_PRICE = (By.CSS_SELECTOR, '.alert-info>.alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages>.alert:nth-child(1)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini>span>a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_TEXT = (By.XPATH, '"//*[contains(text(),"Your basket is empty.")]"')

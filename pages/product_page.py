from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.click_on_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def get_product_name(self):
        name = self.get_text_from_element(*ProductPageLocators.PRODUCT_NAME)
        return name

    def get_product_price(self):
        price = self.get_text_from_element(*ProductPageLocators.PRODUCT_PRICE)
        return price

    def should_be_massage_about_success_adding_to_busked(self, product_name):
        assert product_name == self.get_text_from_element(*ProductPageLocators.MASSAGE_ABOUT_SUCCESS_ADD_TO_BUSKED), \
            'Massage about added to busked not found'

    def should_be_correct_price_after_adding_to_busked(self, product_price):
        assert product_price == self.get_text_from_element(*ProductPageLocators.MASSAGE_ABOUT_BUSKED_PRICE), \
            'Incorrect price in busked massage'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented, but should not be'

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is not disappeared, but should be'

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_items_should_not_be_present(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Basket items are present, but should not be'

    def text_about_empty_basket_should_be_present(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT)
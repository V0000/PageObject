from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators

class PageObject(BasePage):
        
    def add_into_basket(self):
        link = self.browser.find_element_by_css_selector(".btn-add-to-basket")
        link.click()
        
    def compare_name_of_product(self):
        name = self.browser.find_element_by_css_selector('.product_main h1').text
        name_in_message = self.browser.find_element_by_css_selector('.alertinner').text
        #print(name)
        #print(name_in_message)

        assert name_in_message.find(name) != -1, f"Name is not compare: {name} and {name_in_message}"  
        
    def compare_price_of_product(self):
        price = float(self.browser.find_element_by_css_selector('.product_main .price_color').text.strip()[1:])
        price_in_basket = self.browser.find_element_by_css_selector('.alertinner p strong').text
        price_in_basket = float(price_in_basket[1:])
        #print(price)
        #print(price_in_basket)

        assert price == price_in_basket, f"Price is not compare: {price} and {price_in_basket}"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
           
    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
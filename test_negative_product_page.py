from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import PageObject
import time
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
  
    page = PageObject(browser, link)
    page.open()
    page.add_into_basket()
    time.sleep(2)
    page.should_not_be_success_message()
    
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])      
def test_guest_cant_see_success_message(browser, link):
  
    page = PageObject(browser, link)
    page.open()
    #page.add_into_basket()
    time.sleep(2)
    page.should_not_be_success_message()
    
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])  
def test_message_disappeared_after_adding_product_to_basket(browser, link):

    page = PageObject(browser, link)
    page.open()
    page.add_into_basket()
    time.sleep(2)
    page.should_disappeared_message()
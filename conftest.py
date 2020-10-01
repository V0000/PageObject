import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption('--language', default='en')


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def language(request):
    yield request.config.getoption('--language')

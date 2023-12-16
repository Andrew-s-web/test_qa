from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Edge()
    browser.implicitly_wait(10)
    return browser

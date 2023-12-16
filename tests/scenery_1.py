import time
from conf import browser
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage


def test_main(browser):
    browser_page = SbisPage(browser)
    browser_page_tens = TensorPage(browser)
    browser_page.open_browser()
    browser_page.redirect_cont()
    browser_page.click_banner()
    time.sleep(5)
    browser.switch_to.window(browser.window_handles[-1])
    browser_page_tens.scroll_to_block_sila()
    time.sleep(2)
    assert browser_page_tens.find_block_sila()
    browser_page_tens.redir_about_page()
    assert browser_page_tens.current_url() == "https://tensor.ru/about"
    time.sleep(5)
    browser_page_tens.scroll_to_block_rabotaem()
    time.sleep(2)
    assert browser_page_tens.pictures_width()
    assert browser_page_tens.pictures_height()


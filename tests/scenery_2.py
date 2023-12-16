import time
from conf import browser
from pages.sbis_page import SbisPage


def test_sbis_page_cont(browser):
    simple_page = SbisPage(browser)
    simple_page.open_browser()
    time.sleep(2)
    simple_page.redirect_cont()
    assert simple_page.find_reg()
    simple_page.click_reg()
    time.sleep(2)
    simple_page.click_change_reg()
    time.sleep(5)
    assert simple_page.find_reg().text == 'Камчатский край'
    assert simple_page.changed_contack_text() == 'Петропавловск-Камчатский'
    assert 'Камчатский край' in simple_page.title_handling()
    assert '41-kamchatskij-kraj' in simple_page.current_url()

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SbisPageElements:
    button_selector = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    redir = (By.LINK_TEXT, "Контакты")
    change_reg_text = (By.XPATH, "//*[@id='popup']/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span")
    title = (By.TAG_NAME, "title")
    banner = (By.XPATH, '//img[@alt="Разработчик системы СБИС — компания «Тензор»"]')
    contact_text = (By.CLASS_NAME, 'sbisru-Contacts-List__city')


class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_browser(self):
        self.browser.get('https://sbis.ru/')

    def redirect_cont(self):
        self.browser.find_element(*SbisPageElements.redir).click()

    def click_banner(self):
        self.browser.find_element(*SbisPageElements.banner).click()

    def find_reg(self):
        return self.browser.find_element(*SbisPageElements.button_selector)

    def click_reg(self):
        self.browser.find_element(*SbisPageElements.button_selector).click()

    def click_change_reg(self):
        self.browser.find_element(*SbisPageElements.change_reg_text).click()

    def changed_contack_text(self):
        return self.browser.find_element(*SbisPageElements.contact_text).text

    def title_handling(self):
        return self.browser.title

    def current_url(self):
        return self.browser.current_url

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ElementsPage:
    block_sila = (By.CLASS_NAME, 'tensor_ru-Index__block4-content')
    redirect_sila = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    block_rabotaem = (By.CLASS_NAME, 'tensor_ru-About__block3')
    picture_1 = (By.XPATH, "//img[@alt='Разрабатываем систему СБИС']")
    picture_2 = (By.XPATH, "//img[@alt='Продвигаем сервисы']")
    picture_3 = (By.XPATH, "//img[@alt='Создаем инфраструктуру']")
    picture_4 = (By.XPATH, "//img[@alt='Сопровождаем клиентов']")


class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_browser(self):
        self.browser.get('https://sbis.ru/')

    def find_block_sila(self):
        return self.browser.find_element(*ElementsPage.block_sila).is_displayed()

    def current_url(self):
        return self.browser.current_url

    def scroll_to_block_sila(self):
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(*ElementsPage.block_sila))

    def scroll_to_block_rabotaem(self):
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(*ElementsPage.block_rabotaem))

    def redir_about_page(self):
        self.browser.find_element(*ElementsPage.redirect_sila).click()

    def pictures_width(self):
        return (self.browser.find_element(*ElementsPage.picture_1).get_attribute('width') ==
                self.browser.find_element(*ElementsPage.picture_2).get_attribute('width') ==
                self.browser.find_element(*ElementsPage.picture_3).get_attribute('width') ==
                self.browser.find_element(*ElementsPage.picture_4).get_attribute('width'))

    def pictures_height(self):
        return (self.browser.find_element(*ElementsPage.picture_1).get_attribute('height') ==
                self.browser.find_element(*ElementsPage.picture_2).get_attribute('height') ==
                self.browser.find_element(*ElementsPage.picture_3).get_attribute('height') ==
                self.browser.find_element(*ElementsPage.picture_4).get_attribute('height'))

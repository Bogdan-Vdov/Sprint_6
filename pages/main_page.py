from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config import BASE_URL


class MainPage(BasePage):
    """Page Object для главной страницы Яндекс.Самокат"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL
    
    def open(self):
        """Открыть главную страницу"""
        self.open_url(self.url)
    
    def accept_cookies(self):
        """Принять cookies, если появились"""
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except:
            pass  # Если cookies уже приняты или не появились
    
    def click_order_button_top(self):
        """Нажать на верхнюю кнопку 'Заказать'"""
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
    
    def click_order_button_bottom(self):
        """Нажать на нижнюю кнопку 'Заказать'"""
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    def click_scooter_logo(self):
        """Кликнуть на логотип Самоката"""
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        """Кликнуть на логотип Яндекса"""
        self.click_element(MainPageLocators.YANDEX_LOGO)
    
    def scroll_to_faq(self):
        """Прокрутить страницу до раздела 'Вопросы о важном'"""
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)
    
    def click_faq_question(self, question_number):
        """
        Нажать на вопрос в FAQ
        :param question_number: номер вопроса (1-8)
        """
        locator = getattr(MainPageLocators, f"FAQ_QUESTION_{question_number}")
        self.scroll_to_element(locator)
        self.click_element(locator)
    
    def get_faq_answer_text(self, answer_number):
        """
        Получить текст ответа в FAQ
        :param answer_number: номер ответа (1-8)
        :return: текст ответа
        """
        locator = getattr(MainPageLocators, f"FAQ_ANSWER_{answer_number}")
        return self.get_text(locator)
    
    def is_faq_answer_visible(self, answer_number):
        """
        Проверить, виден ли ответ в FAQ
        :param answer_number: номер ответа (1-8)
        :return: True если виден, False если нет
        """
        locator = getattr(MainPageLocators, f"FAQ_ANSWER_{answer_number}")
        return self.is_element_visible(locator)
    
    def is_on_main_page(self):
        """Проверить, что находимся на главной странице"""
        return self.driver.current_url == BASE_URL

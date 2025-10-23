import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import MAIN_PAGE_URL


class MainPage(BasePage):
    """Page Object для главной страницы Яндекс.Самокат"""
    
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url = MAIN_PAGE_URL
    
    @allure.step('Открыть главную страницу')  # type: ignore[misc]
    def open(self) -> None:
        """Открыть главную страницу"""
        self.open_url(self.url)
    
    @allure.step('Принять cookies')  # type: ignore[misc]
    def accept_cookies(self) -> None:
        """Принять cookies, если появились"""
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except:
            pass  # Если cookies уже приняты или не появились
    
    @allure.step('Нажать на верхнюю кнопку "Заказать"')  # type: ignore[misc]
    def click_order_button_top(self) -> None:
        """Нажать на верхнюю кнопку 'Заказать'"""
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
    
    @allure.step('Нажать на нижнюю кнопку "Заказать"')  # type: ignore[misc]
    def click_order_button_bottom(self) -> None:
        """Нажать на нижнюю кнопку 'Заказать'"""
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step('Нажать на кнопку "Заказать" ({button_type})')  # type: ignore[misc]
    def click_order_button(self, button_type: str) -> None:
        """
        Нажать на кнопку 'Заказать' (верхнюю или нижнюю)
        :param button_type: 'топ' или 'bottom'
        """
        if button_type == 'top':
            self.click_order_button_top()
        else:
            self.click_order_button_bottom()
    
    @allure.step('Кликнуть на логотип Самоката')  # type: ignore[misc]
    def click_scooter_logo(self) -> None:
        """Кликнуть на логотип Самоката"""
        # Используем JavaScript для надежности
        self.click_element_js(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step('Кликнуть на логотип Яндекса')  # type: ignore[misc]
    def click_yandex_logo(self) -> None:
        """Кликнуть на логотип Яндекса"""
        self.click_element(MainPageLocators.YANDEX_LOGO)
    
    @allure.step('Прокрутить до раздела FAQ')  # type: ignore[misc]
    def scroll_to_faq(self) -> None:
        """Прокрутить страницу до раздела 'Вопросы о важном'"""
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)
    
    @allure.step('Нажать на вопрос №{question_number} в FAQ')  # type: ignore[misc]
    def click_faq_question(self, question_number: int) -> None:
        """
        Нажать на вопрос в FAQ
        :param question_number: номер вопроса (1-8)
        """
        locator = getattr(MainPageLocators, f"FAQ_QUESTION_{question_number}")
        self.scroll_to_element(locator)
        self.click_element(locator)
    
    @allure.step('Получить текст ответа №{answer_number} в FAQ')  # type: ignore[misc]
    def get_faq_answer_text(self, answer_number: int) -> str:
        """
        Получить текст ответа в FAQ
        :param answer_number: номер ответа (1-8)
        :return: текст ответа
        """
        locator = getattr(MainPageLocators, f"FAQ_ANSWER_{answer_number}")
        return self.get_text(locator)
    
    @allure.step('Проверить видимость ответа №{answer_number} в FAQ')  # type: ignore[misc]
    def is_faq_answer_visible(self, answer_number: int) -> bool:
        """
        Проверить, виден ли ответ в FAQ
        :param answer_number: номер ответа (1-8)
        :return: True если виден, False если нет
        """
        locator = getattr(MainPageLocators, f"FAQ_ANSWER_{answer_number}")
        return self.is_element_visible(locator)
    
    @allure.step('Проверить, что находимся на главной странице')  # type: ignore[misc]
    def is_on_main_page(self) -> bool:
        """Проверить, что находимся на главной странице"""
        return self.get_current_url() == MAIN_PAGE_URL

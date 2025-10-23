import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    """Page Object для страницы заказа"""
    
    @allure.step('Заполнить форму "Для кого самокат"')  # type: ignore[misc]
    def fill_customer_form(self, first_name: str, last_name: str, address: str, metro_station: str, phone: str) -> None:
        """
        Заполнить форму 'Для кого самокат'
        :param first_name: Имя
        :param last_name: Фамилия
        :param address: Адрес доставки
        :param metro_station: Станция метро
        :param phone: Телефон
        """
        self.input_text(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.input_text(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)
        
        # Выбор станции метро
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        self.input_text(OrderPageLocators.METRO_STATION_INPUT, metro_station)
        # Нажимаем Enter или ждем появления нужной станции и кликаем
        metro_option = (By.XPATH, f"//div[@class='Order_Text__2broi' and contains(text(), '{metro_station}')]")
        self.click_element(metro_option)
        
        self.input_text(OrderPageLocators.PHONE_INPUT, phone)
    
    @allure.step('Нажать кнопку "Далее"')  # type: ignore[misc]
    def click_next_button(self) -> None:
        """Нажать кнопку 'Далее'"""
        self.click_element(OrderPageLocators.NEXT_BUTTON)
    
    @allure.step('Заполнить форму "Про аренду"')  # type: ignore[misc]
    def fill_rental_form(self, delivery_date: str, rental_period: str, color: str, comment: str = "") -> None:
        """
        Заполнить форму 'Про аренду'
        :param delivery_date: Дата доставки (формат: дд.мм.гггг)
        :param rental_period: Срок аренды
        :param color: Цвет самоката ('black' или 'grey')
        :param comment: Комментарий для курьера (опционально)
        """
        # Ввод даты доставки
        self.input_text(OrderPageLocators.DELIVERY_DATE_INPUT, delivery_date)
        self.find_element(OrderPageLocators.DELIVERY_DATE_INPUT).send_keys(Keys.ENTER)
        
        # Выбор срока аренды
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_option = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{rental_period}']")
        self.click_element(rental_option)
        
        # Выбор цвета
        if color == 'black':
            self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        elif color == 'grey':
            self.click_element(OrderPageLocators.GREY_COLOR_CHECKBOX)
        
        # Комментарий (опционально)
        if comment:
            self.input_text(OrderPageLocators.COMMENT_INPUT, comment)
    
    @allure.step('Нажать кнопку "Заказать" на второй форме')  # type: ignore[misc]
    def click_order_button(self) -> None:
        """Нажать кнопку 'Заказать' на второй форме"""
        self.click_element(OrderPageLocators.ORDER_BUTTON_FINAL)
    
    @allure.step('Подтвердить заказ')  # type: ignore[misc]
    def click_confirm_order(self) -> None:
        """Подтвердить заказ в модальном окне"""
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
    
    @allure.step('Проверить отображение сообщения об успешном заказе')  # type: ignore[misc]
    def is_success_message_displayed(self) -> bool:
        """Проверить, отображается ли сообщение об успешном создании заказа"""
        return self.is_element_visible(OrderPageLocators.SUCCESS_MESSAGE)
    
    @allure.step('Получить текст сообщения об успешном заказе')  # type: ignore[misc]
    def get_success_message_text(self) -> str:
        """Получить текст сообщения об успешном заказе"""
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)

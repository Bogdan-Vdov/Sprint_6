from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    """Page Object для страницы заказа"""
    
    def fill_customer_form(self, first_name, last_name, address, metro_station, phone):
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
    
    def click_next_button(self):
        """Нажать кнопку 'Далее'"""
        self.click_element(OrderPageLocators.NEXT_BUTTON)
    
    def fill_rental_form(self, delivery_date, rental_period, color, comment=""):
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
    
    def click_order_button(self):
        """Нажать кнопку 'Заказать' на второй форме"""
        self.click_element(OrderPageLocators.ORDER_BUTTON_FINAL)
    
    def click_confirm_order(self):
        """Подтвердить заказ в модальном окне"""
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
    
    def is_success_message_displayed(self):
        """Проверить, отображается ли сообщение об успешном создании заказа"""
        return self.is_element_visible(OrderPageLocators.SUCCESS_MESSAGE)
    
    def get_success_message_text(self):
        """Получить текст сообщения об успешном заказе"""
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)

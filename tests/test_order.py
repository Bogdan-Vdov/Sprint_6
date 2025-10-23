import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Dict, Any
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import TestData


@allure.feature('Заказ самоката')
class TestOrder:
    """Тесты для оформления заказа самоката"""
    
    @pytest.mark.parametrize(
        'button_type, order_data',
        [
            ('top', TestData.ORDER_DATA_1),
            ('bottom', TestData.ORDER_DATA_2),
        ],
        ids=[
            'Верхняя кнопка - набор данных 1',
            'Нижняя кнопка - набор данных 2',
        ]
    )
    @allure.title('Заказ самоката через {button_type} кнопку')
    @allure.description('Проверка полного флоу заказа: заполнение форм + подтверждение + проверка успешного создания')
    def test_order_scooter(self, driver: WebDriver, button_type: str, order_data: Dict[str, Any]) -> None:
        """
        Параметризованный тест заказа самоката
        :param button_type: Тип кнопки ('top' или 'bottom')
        :param order_data: Словарь с данными для заказа
        """
        # Открыть главную страницу
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        # Нажать на кнопку "Заказать" (верхнюю или нижнюю)
        main_page.click_order_button(button_type)
        
        # Заполнить форму "Для кого самокат"
        order_page = OrderPage(driver)
        order_page.fill_customer_form(
            order_data["first_name"],
            order_data["last_name"],
            order_data["address"],
            order_data["metro_station"],
            order_data["phone"]
        )
        order_page.click_next_button()
        
        # Заполнить форму "Про аренду"
        order_page.fill_rental_form(
            order_data["delivery_date"],
            order_data["rental_period"],
            order_data["color"],
            order_data["comment"]
        )
        order_page.click_order_button()
        
        # Подтвердить заказ
        order_page.click_confirm_order()
        
        # Проверить появление сообщения об успешном создании заказа
        assert order_page.is_success_message_displayed(), \
            "Сообщение об успешном заказе не отображается"
        
        success_text = order_page.get_success_message_text()
        assert "Заказ оформлен" in success_text, \
            f"Текст сообщения не соответствует ожидаемому.\nОжидается: 'Заказ оформлен'\nПолучен: {success_text}"

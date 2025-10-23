import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.main_page import MainPage
from urls import MAIN_PAGE_URL


@allure.feature('Навигация по логотипам')
class TestLogos:
    """Тесты для проверки работы логотипов"""
    
    @allure.title('Переход на главную страницу по клику на логотип Самоката')
    @allure.description('При клике на логотип Самоката происходит переход на главную страницу')
    def test_scooter_logo_redirect_to_main(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        # Прокрутить страницу вниз (чтобы убедиться, что не на главной)
        main_page.scroll_to_faq()
        
        # Кликнуть на логотип Самоката
        main_page.click_scooter_logo()
        
        # Проверить, что перешли на главную страницу
        current_url = main_page.get_current_url()
        assert main_page.is_on_main_page(), f"После клика на логотип Самоката не произошел переход на главную страницу. Текущий URL: {current_url}"
    
    @allure.title('Переход на страницу Дзена по клику на логотип Яндекса')
    @allure.description('При клике на логотип Яндекса открывается новое окно с главной страницей Дзена')
    def test_yandex_logo_redirect_to_dzen(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        # Запомнить текущее окно
        original_window = main_page.get_current_window_handle()
        
        # Кликнуть на логотип Яндекса
        main_page.click_yandex_logo()
        
        # Подождать появления нового окна
        main_page.wait_for_number_of_windows(2)
        
        # Переключиться на новое окно
        main_page.switch_to_new_window(original_window)
        
        # Подождать загрузки страницы Дзена
        try:
            main_page.wait_for_url_contains("dzen.ru")
        except:
            main_page.wait_for_url_contains("yandex")
        
        # Проверить, что URL содержит домен Яндекса/Дзена
        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url or "yandex" in current_url, \
            f"После клика на логотип Яндекса не произошел переход на страницу Дзена. Текущий URL: {current_url}"

import pytest
import allure
from pages.main_page import MainPage
from config import BASE_URL


@allure.feature('Навигация по логотипам')
class TestLogos:
    """Тесты для проверки работы логотипов"""
    
    @allure.title('Переход на главную страницу по клику на логотип Самоката')
    @allure.description('При клике на логотип Самоката происходит переход на главную страницу')
    def test_scooter_logo_redirect_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        # Прокрутить страницу вниз (чтобы убедиться, что не на главной)
        main_page.scroll_to_faq()
        
        # Кликнуть на логотип Самоката
        main_page.click_scooter_logo()
        
        # Проверить, что перешли на главную страницу
        assert main_page.is_on_main_page(), f"После клика на логотип Самоката не произошел переход на главную страницу. Текущий URL: {driver.current_url}"
    
    @allure.title('Переход на страницу Дзена по клику на логотип Яндекса')
    @allure.description('При клике на логотип Яндекса открывается новое окно с главной страницей Дзена')
    def test_yandex_logo_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        # Запомнить текущее окно
        original_window = driver.current_window_handle
        
        # Кликнуть на логотип Яндекса
        main_page.click_yandex_logo()
        
        # Подождать появления нового окна
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        
        # Переключиться на новое окно
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        
        # Подождать загрузки страницы Дзена
        WebDriverWait(driver, 10).until(
            lambda d: "dzen.ru" in d.current_url or "yandex.ru/showcase" in d.current_url
        )
        
        # Проверить, что URL содержит домен Яндекса/Дзена
        current_url = driver.current_url
        assert "dzen.ru" in current_url or "yandex" in current_url, \
            f"После клика на логотип Яндекса не произошел переход на страницу Дзена. Текущий URL: {current_url}"

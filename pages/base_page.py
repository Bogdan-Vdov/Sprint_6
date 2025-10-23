import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple, List
from config import EXPLICIT_WAIT


class BasePage:
    """Базовый класс для всех Page Object классов"""
    
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
    
    @allure.step('Открыть URL: {url}')  # type: ignore[misc]
    def open_url(self, url: str) -> None:
        """Открыть URL"""
        self.driver.get(url)
    
    @allure.step('Найти элемент')  # type: ignore[misc]
    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """Найти элемент"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step('Найти несколько элементов')  # type: ignore[misc]
    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        """Найти несколько элементов"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    @allure.step('Кликнуть по элементу')  # type: ignore[misc]
    def click_element(self, locator: Tuple[str, str]) -> None:
        """Кликнуть по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except:
            # Если обычный клик не работает, используем JavaScript
            self.click_element_js(locator)
    
    @allure.step('Ввести текст: {text}')  # type: ignore[misc]
    def input_text(self, locator: Tuple[str, str], text: str) -> None:
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step('Получить текст элемента')  # type: ignore[misc]
    def get_text(self, locator: Tuple[str, str]) -> str:
        """Получить текст элемента"""
        return self.find_element(locator).text
    
    @allure.step('Проверить видимость элемента')  # type: ignore[misc]
    def is_element_visible(self, locator: Tuple[str, str]) -> bool:
        """Проверить, виден ли элемент"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    @allure.step('Прокрутить страницу до элемента')  # type: ignore[misc]
    def scroll_to_element(self, locator: Tuple[str, str]) -> None:
        """Прокрутить страницу до элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Небольшая задержка после прокрутки
        import time
        time.sleep(0.3)
    
    @allure.step('Кликнуть по элементу через JavaScript')  # type: ignore[misc]
    def click_element_js(self, locator: Tuple[str, str]) -> None:
        """Кликнуть по элементу через JavaScript (для перекрытых элементов)"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step('Получить текущий URL')  # type: ignore[misc]
    def get_current_url(self) -> str:
        """Получить текущий URL страницы"""
        return self.driver.current_url
    
    @allure.step('Получить текущее окно браузера')  # type: ignore[misc]
    def get_current_window_handle(self) -> str:
        """Получить идентификатор текущего окна"""
        return self.driver.current_window_handle
    
    @allure.step('Получить все окна браузера')  # type: ignore[misc]
    def get_window_handles(self) -> List[str]:
        """Получить список всех окон"""
        return self.driver.window_handles
    
    @allure.step('Переключиться на окно')  # type: ignore[misc]
    def switch_to_window(self, window_handle: str) -> None:
        """Переключиться на указанное окно"""
        self.driver.switch_to.window(window_handle)
    
    @allure.step('Ожидать появления {expected_count} окон')  # type: ignore[misc]
    def wait_for_number_of_windows(self, expected_count: int, timeout: int = 10) -> None:
        """Ожидать появления определённого количества окон"""
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(expected_count)
        )
    
    @allure.step('Ожидать URL содержит: {text}')  # type: ignore[misc]
    def wait_for_url_contains(self, text: str, timeout: int = 10) -> None:
        """Ожидать, пока URL не будет содержать указанный текст"""
        WebDriverWait(self.driver, timeout).until(
            lambda d: text in d.current_url
        )
    
    @allure.step('Переключиться на новое окно')  # type: ignore[misc]
    def switch_to_new_window(self, original_window: str) -> None:
        """Переключиться на новое окно (отличное от original_window)"""
        for window_handle in self.get_window_handles():
            if window_handle != original_window:
                self.switch_to_window(window_handle)
                break

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import EXPLICIT_WAIT


class BasePage:
    """Базовый класс для всех Page Object классов"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
    
    def open_url(self, url):
        """Открыть URL"""
        self.driver.get(url)
    
    def find_element(self, locator):
        """Найти элемент"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Найти несколько элементов"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click_element(self, locator):
        """Кликнуть по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def input_text(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text
    
    def is_element_visible(self, locator):
        """Проверить, виден ли элемент"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def scroll_to_element(self, locator):
        """Прокрутить страницу до элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

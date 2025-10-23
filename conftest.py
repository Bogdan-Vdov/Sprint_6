import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from typing import Generator


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    """Фикстура для инициализации и завершения работы WebDriver"""
    options = webdriver.FirefoxOptions()
    # Раскомментируйте следующую строку для запуска в headless режиме
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

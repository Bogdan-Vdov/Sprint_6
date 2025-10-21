from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы заказа"""
    
    # Форма "Для кого самокат"
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
    # Выпадающий список станций метро
    METRO_DROPDOWN = (By.CLASS_NAME, "select-search__select")
    
    # Кнопка "Далее" на первой форме
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Форма "Про аренду"
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    
    # Цвет самоката
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    
    # Комментарий для курьера
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    # Кнопка "Заказать" на второй форме
    ORDER_BUTTON_FINAL = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    
    # Модальное окно подтверждения
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    # Модальное окно успешного заказа
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    
    # Кнопка "Посмотреть статус"
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

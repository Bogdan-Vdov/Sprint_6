from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы Яндекс.Самокат"""
    
    # Кнопки "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    
    # Раздел "Вопросы о важном"
    FAQ_SECTION = (By.XPATH, "//div[@class='Home_FourPart__1uthg']")
    FAQ_HEADING = (By.XPATH, "//div[contains(@class, 'Home_FourPart')]//div[text()='Вопросы о важном']")
    
    # Вопросы в FAQ (стрелочки для раскрытия)
    FAQ_QUESTION_1 = (By.ID, "accordion__heading-0")
    FAQ_QUESTION_2 = (By.ID, "accordion__heading-1")
    FAQ_QUESTION_3 = (By.ID, "accordion__heading-2")
    FAQ_QUESTION_4 = (By.ID, "accordion__heading-3")
    FAQ_QUESTION_5 = (By.ID, "accordion__heading-4")
    FAQ_QUESTION_6 = (By.ID, "accordion__heading-5")
    FAQ_QUESTION_7 = (By.ID, "accordion__heading-6")
    FAQ_QUESTION_8 = (By.ID, "accordion__heading-7")
    
    # Ответы в FAQ
    FAQ_ANSWER_1 = (By.ID, "accordion__panel-0")
    FAQ_ANSWER_2 = (By.ID, "accordion__panel-1")
    FAQ_ANSWER_3 = (By.ID, "accordion__panel-2")
    FAQ_ANSWER_4 = (By.ID, "accordion__panel-3")
    FAQ_ANSWER_5 = (By.ID, "accordion__panel-4")
    FAQ_ANSWER_6 = (By.ID, "accordion__panel-5")
    FAQ_ANSWER_7 = (By.ID, "accordion__panel-6")
    FAQ_ANSWER_8 = (By.ID, "accordion__panel-7")
    
    # Кнопка принятия cookie
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

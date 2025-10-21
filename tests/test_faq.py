import pytest
import allure
from pages.main_page import MainPage
from test_data import TestData


@allure.feature('FAQ - Вопросы о важном')
class TestFAQ:
    """Тесты для раздела 'Вопросы о важном'"""
    
    @pytest.mark.parametrize(
        'question_number, expected_answer',
        [
            (1, TestData.FAQ_EXPECTED_ANSWERS[1]),
            (2, TestData.FAQ_EXPECTED_ANSWERS[2]),
            (3, TestData.FAQ_EXPECTED_ANSWERS[3]),
            (4, TestData.FAQ_EXPECTED_ANSWERS[4]),
            (5, TestData.FAQ_EXPECTED_ANSWERS[5]),
            (6, TestData.FAQ_EXPECTED_ANSWERS[6]),
            (7, TestData.FAQ_EXPECTED_ANSWERS[7]),
            (8, TestData.FAQ_EXPECTED_ANSWERS[8]),
        ],
        ids=[
            'Вопрос 1: Сколько это стоит?',
            'Вопрос 2: Хочу сразу несколько самокатов',
            'Вопрос 3: Как рассчитывается время аренды?',
            'Вопрос 4: Можно ли заказать самокат прямо на сегодня?',
            'Вопрос 5: Можно ли продлить заказ?',
            'Вопрос 6: Вы привозите зарядку?',
            'Вопрос 7: Можно ли отменить заказ?',
            'Вопрос 8: Я жизу за МКАДом',
        ]
    )
    @allure.title('Проверка раскрытия ответа на вопрос {question_number}')
    @allure.description('При нажатии на вопрос открывается соответствующий текст ответа')
    def test_faq_questions(self, driver, question_number, expected_answer):
        """Параметризованный тест для проверки всех вопросов FAQ"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.scroll_to_faq()
        
        # Нажать на вопрос
        main_page.click_faq_question(question_number)
        
        # Проверить, что ответ отображается
        assert main_page.is_faq_answer_visible(question_number), \
            f"Ответ на вопрос {question_number} не отображается"
        
        # Проверить текст ответа
        answer_text = main_page.get_faq_answer_text(question_number)
        assert expected_answer in answer_text, \
            f"Текст ответа на вопрос {question_number} не соответствует ожидаемому.\nОжидается: {expected_answer}\nПолучен: {answer_text}"

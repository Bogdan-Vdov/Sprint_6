# Автотесты для Яндекс.Самокат

Проект автоматизации тестирования сервиса "Яндекс.Самокат"

## Технологии
- Python 3.x
- Selenium WebDriver
- Pytest
- Page Object Model

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv venv
```

2. Активируйте виртуальное окружение:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск тестов

Запуск всех тестов:
```bash
pytest tests/
```

Запуск с HTML отчетом:
```bash
pytest tests/ --html=report.html --self-contained-html
```

Запуск с Allure отчетом:
```bash
pytest tests/ --alluredir=allure_results
allure serve allure_results
```

## Структура проекта

```
Sprint_6/
├── locators/           # Локаторы элементов страниц
│   ├── __init__.py
│   ├── main_page_locators.py
│   └── order_page_locators.py
├── pages/              # Page Object классы
│   ├── __init__.py
│   ├── base_page.py    # Базовый класс для страниц
│   ├── main_page.py    # Главная страница
│   └── order_page.py   # Страница заказа
├── tests/              # Тесты
│   ├── __init__.py
│   ├── test_faq.py     # Тесты для раздела FAQ
│   ├── test_order.py   # Тесты для заказа самоката
│   └── test_logos.py   # Тесты для логотипов
├── config.py           # Конфигурация
├── conftest.py         # Pytest фикстуры
├── test_data.py        # Тестовые данные
├── pytest.ini          # Настройки pytest
├── requirements.txt    # Зависимости
└── README.md          # Документация
```

## Тестовые сценарии

### 1. Тесты FAQ (test_faq.py)
- 8 отдельных тестов для каждого вопроса в разделе "Вопросы о важном"
- Проверка раскрытия ответа при клике на вопрос
- Проверка соответствия текста ответа ожидаемому

### 2. Тесты заказа самоката (test_order.py)
- Тест заказа через верхнюю кнопку "Заказать" (набор данных 1)
- Тест заказа через нижнюю кнопку "Заказать" (набор данных 2)
- Проверка полного флоу: заполнение форм + подтверждение + проверка успешного создания

### 3. Тесты логотипов (test_logos.py)
- Проверка перехода на главную страницу по клику на логотип Самоката
- Проверка открытия Дзена в новом окне по клику на логотип Яндекса

## URL сервиса
https://qa-scooter.praktikum-services.ru/

## Дополнительная документация

- [QUICKSTART.md](QUICKSTART.md) - Быстрый старт и примеры запуска
- [PARAMETRIZATION.md](PARAMETRIZATION.md) - Подробно о параметризации тестов
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Итоговое резюме проекта
- [ALLURE_REPORT.md](ALLURE_REPORT.md) - Подробно о Allure-отчётах
- [ALLURE_EXAMPLE.md](ALLURE_EXAMPLE.md) - Пример как выглядит Allure-отчёт
- [HOW_TO_RUN_WITH_ALLURE.md](HOW_TO_RUN_WITH_ALLURE.md) - Инструкция по запуску с Allure

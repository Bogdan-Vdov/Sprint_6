# Настройка VSCode для проекта Sprint_6

## Проблема
VSCode показывает 182 ошибки из-за того, что не может найти установленные библиотеки (selenium, pytest, allure и др.).

## Решение

### 1. Файлы конфигурации созданы автоматически:

#### `.vscode/settings.json`
Настройки Python для VSCode:
- Путь к интерпретатору Python: `C:\Program Files\Python313\python.exe`
- Отключены ненужные предупреждения типов
- Настроен Pylance для работы с проектом

#### `pyrightconfig.json`
Настройки проверки типов:
- Указана версия Python 3.13
- Отключены предупреждения о неизвестных типах
- Базовый режим проверки типов

### 2. Перезагрузите VSCode
После создания файлов конфигурации необходимо:
1. Закрыть VSCode полностью (Ctrl+Q или File → Exit)
2. Открыть проект заново

### 3. Проверьте интерпретатор Python в VSCode
1. Нажмите `Ctrl+Shift+P`
2. Введите "Python: Select Interpreter"
3. Выберите: `C:\Program Files\Python313\python.exe`

### 4. Очистите кеш (если ошибки остались)
```powershell
# Выполните в терминале VSCode:
Remove-Item -Recurse -Force .vscode/.pyright_cache -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force **/__pycache__ -ErrorAction SilentlyContinue
```

## Установленные библиотеки

Все необходимые библиотеки уже установлены:
```
selenium==4.15.2        # Автоматизация браузера
pytest==7.4.3           # Фреймворк тестирования
pytest-html==4.1.1      # HTML отчеты
allure-pytest==2.13.2   # Allure отчеты
webdriver-manager==4.0.1 # Управление драйверами
```

## Проверка работоспособности

### Проверить импорты:
```bash
python -c "from pages.base_page import BasePage; from pages.main_page import MainPage; print('OK')"
```

### Собрать тесты:
```bash
pytest --collect-only -q
```
Должно показать: `collected 12 items`

### Запустить все тесты:
```bash
pytest tests/ -v
```
Должно пройти: `12 passed`

## Результат
После настройки VSCode должен:
- ✅ Не показывать ошибки о неизвестных библиотеках
- ✅ Корректно подсвечивать код
- ✅ Предлагать автодополнение для всех методов
- ✅ Показывать типы при наведении на переменные

## Дополнительная информация

### Структура проекта
```
Sprint_6/
├── .vscode/
│   └── settings.json          # Настройки VSCode
├── locators/                  # Локаторы элементов
├── pages/                     # Page Object классы
├── tests/                     # Тесты
├── pyrightconfig.json         # Настройки проверки типов
├── requirements.txt           # Зависимости
└── README.md                  # Документация
```

### Если ошибки все еще появляются

1. **Проверьте расширения VSCode:**
   - Python (Microsoft) - должно быть установлено
   - Pylance (Microsoft) - должно быть установлено

2. **Убедитесь, что Python виден:**
   ```bash
   python --version
   # Должно вывести: Python 3.13.5
   ```

3. **Переустановите зависимости:**
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

4. **Обновите VSCode:**
   Help → Check for Updates

## Поддержка

Если проблемы остались:
1. Закройте все окна VSCode
2. Удалите папку `.vscode/.pyright_cache`
3. Откройте проект заново
4. Подождите 1-2 минуты пока VSCode проиндексирует файлы

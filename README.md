```
# Telegram Screenshot Bot

Это Telegram-бот, который принимает домен или IP-адрес сайта и возвращает скриншот указанного сайта.

## Описание
Бот написан на Python с использованием библиотеки `python-telegram-bot` для взаимодействия с Telegram API и `selenium` для создания скриншотов веб-страниц. Он полезен для быстрой проверки внешнего вида сайта без необходимости его открывать.

## Установка и запуск

### Требования
- Python 3.x
- Установленные библиотеки:
  - `python-telegram-bot`
  - `selenium`
- ChromeDriver (для работы Selenium)

### Шаги
1. **Клонируй репозиторий**:
   ```bash
   git clone https://github.com/твой_юзернейм/telegram-screenshot-bot.git
   cd telegram-screenshot-bot
   ```

2. **Установи зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Установи ChromeDriver**:
   - Скачай ChromeDriver, совместимый с твоей версией Chrome, с [официального сайта](https://chromedriver.chromium.org/downloads).
   - Размести его в папке проекта или добавь путь в переменные окружения.

4. **Настрой токен бота**:
   - Получи токен у @BotFather в Telegram.
   - Укажи токен как переменную окружения:
     - На Windows: `set TELEGRAM_BOT_TOKEN=твой_токен`
     - На Linux/Mac: `export TELEGRAM_BOT_TOKEN=твой_токен`

5. **Запусти бота**:
   ```bash
   python bot.py
   ```

## Использование
- Отправь боту команду `/start`, чтобы начать.
- Отправь домен (например, `google.com`) или IP-адрес (например, `8.8.8.8`), и бот пришлет скриншот сайта.

## Лицензия
Этот проект распространяется под лицензией [MIT](LICENSE).

## Контакты
- Автор: [TimkaMB](https://github.com/TimkaMB)
- Если есть вопросы, создай Issue в этом репозитории.
```

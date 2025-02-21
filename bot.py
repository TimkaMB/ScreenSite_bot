from config import TOKEN
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Проверяем, задан ли токен
if not TOKEN:
    raise ValueError("Токен бота не найден! Проверь файл config.py.")

# Функция для создания скриншота
def take_screenshot(url):
    # Настройки для headless-режима (без открытия окна браузера)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Запуск браузера
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 720)  # Размер окна

    # Исправляем URL, если нет http/https
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    # Открываем сайт и делаем скриншот
    driver.get(url)
    screenshot_path = 'screenshot.png'
    driver.save_screenshot(screenshot_path)
    driver.quit()

    return screenshot_path

# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправь мне домен или IP, и я пришлю скриншот сайта.')

# Обработка текстовых сообщений (URL или IP)
def handle_message(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    update.message.reply_text('Делаю скриншот, подожди...')
    
    try:
        screenshot = take_screenshot(url)
        with open(screenshot, 'rb') as photo:
            update.message.reply_photo(photo)
        os.remove(screenshot)  # Удаляем файл после отправки
    except Exception as e:
        update.message.reply_text(f'Ошибка: {str(e)}. Проверь URL или попробуй снова.')

# Основная функция для запуска бота
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Регистрируем команды и обработчики
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

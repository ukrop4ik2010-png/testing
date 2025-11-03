import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен бота (получите у @BotFather)
BOT_TOKEN = "import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен бота (получите у @BotFather)
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Повторяет полученное сообщение"""
    user_message = update.message.text
    
    # Отправляем обратно то же сообщение
    await update.message.reply_text(f"Вы сказали: {user_message}")

async def handle_other_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает другие типы сообщений (фото, стикеры и т.д.)"""
    await update.message.reply_text("Я повторяю только текстовые сообщения!")

def main():
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))
    
    # Обработчик всех остальных типов сообщений
    application.add_handler(MessageHandler(filters.ALL, handle_other_messages))
    
    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()"

async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Повторяет полученное сообщение"""
    user_message = update.message.text
    
    # Отправляем обратно то же сообщение
    await update.message.reply_text(f"Вы сказали: {user_message}")

async def handle_other_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает другие типы сообщений (фото, стикеры и т.д.)"""
    await update.message.reply_text("Я повторяю только текстовые сообщения!")

def main():
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))
    
    # Обработчик всех остальных типов сообщений
    application.add_handler(MessageHandler(filters.ALL, handle_other_messages))
    
    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
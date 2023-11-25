
from settings import BOT_TOKEN
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler
import ephem
from datetime import date
import logging
from collections import defaultdict

logging.basicConfig(level=logging.INFO)

user_word_frequencies = {}
word_frequency = defaultdict(int)
def process_message(incoming_message):
    words = incoming_message.split()
    for word in words:
        normalized_word = word.lower()
        word_frequency[normalized_word] += 1
        return word_frequency

def checker(incoming_message: str) -> str:    
    for item in incoming_message.split():
        if hasattr(ephem, item):
            logging.info(f'Попался {item}')
            cont_result = ephem.constellation(getattr(ephem,item)(date.today()))[1]
            return cont_result
    return f'Введены ошибочные данные'

async def echo(update: Update, some_context):
    await update.message.reply_text(process_message(update.message.text))
    await update.message.reply_text(checker(update.message.text))

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, echo))
    app.run_polling(allowed_updates=Update.ALL_TYPES)
if __name__ == '__main__':
    main()
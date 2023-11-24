
from settings import BOT_TOKEN
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import ephem
from datetime import date
import logging

logging.basicConfig(level=logging.INFO)
   

def checker(incoming_message: str) -> str:    
    logging.info(incoming_message.split())
    for item in incoming_message.split():
        if hasattr(ephem, item):
            logging.info(f'Попался {item}')
            cont_result = ephem.constellation(getattr(ephem,item)(date.today()))[1]
        else:
            return f'Введены ошибочные данные'
    return cont_result

async def echo(update: Update, context):
    await update.message.reply_text(checker(update.message.text))

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, echo))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
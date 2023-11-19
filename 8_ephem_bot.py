"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from settings import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



async def planet(update: Update, context: ContextTypes.DEFAULT_TYPE):
  try:
    planet_name = update.message.text.split()[1].capitalize()
    planet_obj = getattr(ephem, planet_name)()
    planet_obj.compute()
    constellation = ephem.constellation(planet_obj)[1]
    text_result = f'{planet_name} сейчас находится в созвездии {constellation}.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{text_result}')
  except IndexError:
    error_text = 'Планета не найдена. Введите корректное название планеты.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{error_text}')
        

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Привет введи комманду /planet Mars или любое название на английском')


if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    start_handler = CommandHandler('start', start)
    planet_handler = CommandHandler('planet', planet)
    application.add_handler(start_handler)
    application.add_handler(planet_handler)
    application.run_polling()
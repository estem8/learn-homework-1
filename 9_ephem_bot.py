from settings import BOT_TOKEN
import telebot
import ephem

bot = telebot.TeleBot(BOT_TOKEN)

planet_list=[
    'Mercury',
    'Venus',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
    'Pluto'
]

#Если в предложении упоминается планета
#возвращается True для message_handler(func=checker)
#и продолжает выпонятся def show_const

def checker(msg):
    planet_list=[
        'Mercury',
        'Venus',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune',
        'Pluto'
    ]
    for word in planet_list:
        if word.lower() in msg.text.lower():
            return True
    return False

def process_text(msg):
    planet_name = msg.text.capitalize()
    planet_obj = getattr(ephem, planet_name)()
    planet_obj.compute()
    constellation = ephem.constellation(planet_obj)[1]
    return constellation

#func=checker вызывает функцию проврки каждого слова на
#список планет
@bot.message_handler(func=checker)
def show_const(message):
    
    processed_result = process_text(message)

    bot.send_message(message.chat.id, processed_result)

if __name__ == '__main__':
    bot.infinity_polling()
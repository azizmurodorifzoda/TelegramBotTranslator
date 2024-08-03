import telebot
from telebot import types
from googletrans import Translator,LANGUAGES
import psycopg2


# connection=psycopg2.connect(
#     datebase="Aziziprogramist"
#     user="postgress"
#     host='localhost'
#     password='1902'
#     port='5432')



bot=telebot.TeleBot('6715595116:AAG7T6-foKWAqEvhPpmw4CytWzd7ggruH8M')

translator=Translator()

language1='en'
language2='ru'


@bot.message_handler()
def say_hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    btn2=types.KeyboardButton("/help")
    markup.row(btn1,btn2)
    bot.send_message(message.chat.id, "zinda bday...  переводчикай ", reply_markup=markup)
def translate_message(message):
    try:
        a=translator.translate(message.text,src=language1,dest=language2)
        bot.send_message(message.chat.id,a.text)
    except Exception as e:
        bot.send_message(message.chat.id,'error')


bot.infinity_polling()

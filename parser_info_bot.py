from time import sleep
import telebot
from telebot import types
import main

bot = telebot.TeleBot('5327535231:AAG7VpTLSkzkQ74M26jQ3FcOPgJSMNe0ZbQ')

@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Парсинг")
        item2=types.KeyboardButton("Поиск по названию")
        item3=types.KeyboardButton("Получить JSON")
        item4=types.KeyboardButton("Получить CSV")
        item5=types.KeyboardButton("Информация")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(m.chat.id, 'Нажми на кнопку \"Парсинг\" чтобы получить информацию с сайта',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Парсинг' :
        try:
            main.parse()
            bot.send_message(message.chat.id,'Success')
        except Exception:
            bot.send_message(message.chat.id,'Please try again')
    if message.text == 'Поиск по названию':
        bot.send_message(message.chat.id, "Введите название криптовалюты")
        key=message.text
        bot.send_message(message.chat.id,str(main.search_upper(main.cryptocurrency,key)))
    if message.text.strip() == 'Получить JSON':
        main.create_json(main.cryptocurrency)
        with open('./data.json', 'rb') as f1:
            bot.send_document(message.chat.id, f1)
    if message.text.strip() == 'Получить CSV':
        main.create_csv(main.cryptocurrency)
        with open('./data.csv', 'rb') as f1:
            bot.send_document(message.chat.id, f1)

bot.polling(none_stop=True)
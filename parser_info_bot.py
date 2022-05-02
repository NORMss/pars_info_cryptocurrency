from time import sleep
import telebot
from telebot import types
import main

# Создаем экземпляр бота
bot = telebot.TeleBot('5327535231:AAG7VpTLSkzkQ74M26jQ3FcOPgJSMNe0ZbQ')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
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

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Парсинг' :
        try:
            main.parse()
        except Exception:
            bot.send_message(message.chat.id,'Please try again')
    if message.text.strip() == 'Поиск по названию':
        bot.send_message(message.chat.id, "Введите название криптовалюты")
        sleep(10)
        key=message.text.strip()
        bot.send_message(message.chat.id,str(main.search_list(main.cryptocurrency,key)))
    if message.text.strip() == 'Получить JSON':
        main.create_json(main.cryptocurrency)
        with open('./data.json', 'rb') as f1:
            bot.send_document(message.chat.id, f1)
    if message.text.strip() == 'Получить CSV':
        main.create_csv(main.cryptocurrency)
        with open('./data.csv', 'rb') as f1:
            bot.send_document(message.chat.id, f1)
        # bot.send_message(message.chat.id,main.cryptocurrency[2])
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Информация':
        return
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, 'answer')
# Запускаем бота
bot.polling(none_stop=True, interval=0)
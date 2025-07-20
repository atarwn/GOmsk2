import telebot
from telebot import types

bot = telebot.TeleBot("7724534770:AAG8XbLZcCgqlwESGfbrT9z-BlDJfnCAvVI")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttonA = types.KeyboardButton('КАРО 7 Атриум')
    buttonB = types.KeyboardButton('Формула Кино')
    buttonC = types.KeyboardButton('Москва')
    buttonD = types.KeyboardButton('Пять звезд')
    markup.row(buttonA, buttonB)
    markup.row(buttonC, buttonD)
    bot.send_message(message.chat.id, 'Выбери кинотеатры:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def process_message(message):
    if message.text == "КАРО 7 Атриум":
        markup = types.InlineKeyboardMarkup()
        buttonA = types.InlineKeyboardButton('Жизнь Чака', callback_data='жизнь_чака')
        buttonB = types.InlineKeyboardButton('Нейробатя', callback_data='стоимость_жизнь_чака')
        buttonC = types.InlineKeyboardButton('Материалистка', callback_data='рпощлщзоплп')
        markup.row(buttonA)
        markup.row(buttonB)
        markup.row(buttonC)
        bot.send_message(message.chat.id, 'Выбери фильм:', reply_markup=markup)
        if message.text == "Жизнь Чака":
          markup = types.InlineKeyboardMarkup()
          buttonB = types.InlineKeyboardButton('Cтоимость: 350 рублей', callback_data='стоимость_жизнь_чака')
          markup.row(buttonB)
          bot.send_message(message.chat.id, 'Купить', reply_markup=markup)
    elif message.text == "Формула Кино":
        bot.send_message(message.chat.id, 'Формула Кино - ваш выбор.')
    elif message.text == "Москва":
        bot.send_message(message.chat.id, 'Москва - ваш выбор.')
    elif message.text == "Пять звезд":
        bot.send_message(message.chat.id, 'Пять звезд - ваш выбор.')
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда.')

# @bot.callback_query_handler(func=lambda call: True)
# def message(call):
#   bot.send_message(message.chat.id, 'Выбери фильм:', reply_markup=markup)
#     if call.data == 'Жизнь чака':
#         bot.send_message(call.message.chat.id, 'Жизнь Чака - это ваш фильм!')
#     elif call.data == 'стоимость_жизнь_чака':
#         bot.send_message(call.message.chat.id, 'Стоимость билета на "Жизнь Чака" - 350 руб.')

bot.polling(none_stop=True)

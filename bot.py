# -*- coding: utf-8 -*-
import os
import telebot

from queue import Queue  # in python 2 it should be "from Queue"
from threading import Thread

import telegram




token = "920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y"
bot = telebot.TeleBot(token)

def setup(token):
    # Create bot, update queue and dispatcher instances
    bot = Bot(token)
    update_queue = Queue()
    
    dispatcher = Dispatcher(bot, update_queue)


    @bot.message_handler(commands=["start"])
    def start(m):
        msg = bot.send_message(m.chat.id, "Вас приветствует Бот")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['О компании', 'Прайс-лист']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Акции', 'Контакты']])
        bot.send_message(m.chat.id, 'Выберите в меню что вам интересно!',
            reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)

    def name(m):
        if m.text == 'О компании':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(advert) for advert in ['Сертификаты']])
            keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
            bot.send_message(m.chat.id, 'инфа о компании',
                reply_markup=keyboard)
        elif m.text == 'Прайс-лист':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(advert) for advert in ['Общий', 'Одиночный']])
            keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
            bot.send_message(m.chat.id, 'Выберите прайс который нужен.',
                reply_markup=keyboard)
        elif m.text == 'Акции':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
            bot.send_message(m.chat.id, 'Сожалею, но в данный момент акций нет(',
                reply_markup=keyboard)





# Start the thread
    thread = Thread(target=dispatcher.start, name='dispatcher')
    thread.start()
    
    return update_queue
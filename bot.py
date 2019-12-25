# -*- coding: utf-8 -*-
import os
import telebot
from telebot import types




TOKEN = "920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Вас приветствует Бот")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Местоположение', request_location=True))
    keyboard.add(types.KeyboardButton('Инвентаризация'))
    keyboard.add(types.KeyboardButton('Инструкции'))
    
    bot.send_message(m.chat.id, 'Выберите нужный пункт',
        reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)

def name(m):
    if m.text == 'Местоположение':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Верно']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Ваше местоположение',
            reply_markup=keyboard)
    elif m.text == 'Инвентаризация':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Маршрутизатор', 'ТВ-приставка']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Веберите и сфотографируйте оборудование',
            reply_markup=keyboard)
    elif m.text == 'Инструкции':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Сделай всё отлично',
            reply_markup=keyboard)

#@bot.message_handler(commands=['Назад'])
#def

bot.polling(none_stop=True, interval=0)
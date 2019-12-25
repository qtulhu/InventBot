# -*- coding: utf-8 -*-
import telebot


bot = telebot.TeleBot("920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y")




# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Моё местоположение...', 'Инвентаризация', 'Инструкции']])
    msg = bot.send_message(message.chat.id, 'Давай сначала определим где ты находишься, а затем произведем инвентаризацию',
    	reply_markup=keyboard)
    bot.register_next_step_handler(msg,name)

#def option(message):
	#if message.text == 'Моё местоположение...':
	#	msg = bot.send_message(message.chat.id, )

 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass

bot.polling(none_stop=True, interval=0)
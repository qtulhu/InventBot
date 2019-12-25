# -*- coding: utf-8 -*-
import telebot


bot = telebot.TeleBot("920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y")
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! I am HabrahabrExampleBot. How can i help you?")
    
    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")
    
    else:
        bot.send_message(message.from_user.id, "Sorry, i dont understand you.")



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

bot.polling()
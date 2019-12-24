import telebot
from variables import *
import logging

bot = telebot.TeleBot(TOKEN)

def main(use_logging, level_name):
	if use_logging:
		telebot.logger.setLevel(logging.getLevelName(level_name))
	bot.polling(none_stop=True, interval=.5)

@bot.message_handler(commands=['help'])
def help_handler(message):
	bot.send_message(message.from_user.id, help_mess)

@bot.message_handler(func=lambda message: True)
def forward_handler(message):
	try:
		if message.chat.id == int(CHAT):
			bot.send_message(message.reply_to_message.forward_from.id, message.text)
		else:
			bot.forward_message(CHAT,message.chat.id)
	except Exception as error:
		print("Info:{}".format(error))


if __name__ == '__main__':
	main(True, 'DEBUG')
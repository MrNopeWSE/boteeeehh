import telebot
bot=telebot.TeleBot('1633002729:AAHE00Y9FoevHRRHbkqz4rBB-Cf60ODfn88')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, ты написал мне /start')
bot.polling()
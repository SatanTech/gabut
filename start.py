# mengimport package pyTelegramBotAPI
import telebot

# inisialisasi Token Bot Kita
bot = telebot.TeleBot('6670840720:AAF7taZHjmEIeg2C8sdL689JF39wq_bUd0M')

# Menghandle Pesan /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Ketik /menu')
    
#Menghandle Pesan /start
@bot.message_handler(commands=['menu'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Ini udah masuk menu')
    
while True:
    try:
        bot.polling()
    except:
        pass
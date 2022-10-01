import f_category
import telebot
import menu
import os
api_key = secret.TOKEN
bot = telebot.TeleBot(TOKEN)
count = False
bill = ''
bill_no = 1
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello World")
@bot.message_handler(commands=['order'])
def show_category(message):
	cat_list = ""
	i = 1
	for item in menu.category:
		cat_list +=f"{i}. {item}\n"
		i+=1
	bot.reply_to(message, cat_list)
	bot.send_message(message.chat.id,"Pick a category")
@bot.message_handler(func = lambda m:True)
def check_menu(message):
	global count,bill,bill_no
	food = str(message.text)
	food = food.lower()
	if(str(message.text) in menu.food):
		if(count != True):
			count = True
			bill = f"Bill no :{bill_no} Items \n"
			bill += message.text + "\n"
			bot.reply_to(message,bill)
		else:
			bill += message.text + '\n'
			bot.reply_to(message,bill)
	if(food == "end"):
		bot.reply_to(message,"final bill")
		bot.reply_to(message,bill)
		count = False
		bill = ''
		bill_no+=1








bot.infinity_polling()

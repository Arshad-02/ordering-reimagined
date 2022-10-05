import telebot
import menu
import os
#api_key = os.TOKEN


#global 

bot = telebot.TeleBot(TOKEN)
count = False
bill = ''
bill_no = 1

#handlers

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello World")

@bot.message_handler(commands=['order'])
def show_category(message):
	cat_list = ""
	i = 1
	for item in menu.type_f:
		cat_list +=f"{i}. {item}\n"
		i+=1
	bot.reply_to(message, cat_list)
	bot.send_message(message.chat.id,"Pick a category")

@bot.message_handler(commands=['available'])
def show_avail(message):
	avail_f = ''
	for food in menu.food:
		avail_f += food + "\n"
	bot.reply_to(message,avail_f)

@bot.message_handler(func = lambda m:True)
def check_menu(message):
	item = message.text.split(' ',1)
	global count,bill,bill_no
	if len(item) == 2 and int(item[0]):
		qty = int(item[0])
		food = str(item[1])
		food = food.lower()
		if(food in menu.food):
			if(count != True):
				count = True
				bill = f"Bill no :{bill_no}\n--------------------\nQty  Items\n--------------------\n"
				bill += f"{qty}   X  {food}" + "\n"
				bot.reply_to(message,bill)
			else:
				bill += f"{qty}   X  {food}" + "\n"
				bot.reply_to(message,bill)
	if(len(item) == 1 and item[0].lower() == "end"):
		bot.reply_to(message,"final bill")
		bot.reply_to(message,bill)
		count = False
		bill = ''
		bill_no+=1








bot.infinity_polling()

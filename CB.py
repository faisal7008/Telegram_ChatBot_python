# CORONA GO!

import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='1873088816:AAHmzJ8kyBx35scNUEWSk3e1--Pkjx2hs0g',use_context=True) 
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Hello! Welcome to EE Group \nFor Coronavirus Current Status \npress -> /New')

hello_handler = CommandHandler('start', hello)
dispatcher.add_handler(hello_handler)
updater.start_polling()

def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code == 200):  # Everything went okay, we have the data
        data = response.json()
        Global = data['Global']
        # print(Global['NewConfirmed'])
        string = "Worldwide Cases: " + "\nTotal Cases: " + str(Global['TotalConfirmed']) + "\nNew Cases: " + str(Global['NewConfirmed']) + "\nTotal Deaths: " + str(Global['TotalDeaths']) + "\nNew Deaths: " + str(
            Global['NewDeaths']) + "\nTotal Recovered: " + str(Global['TotalRecovered']) + "\nNew Recovered: " + str(Global['NewRecovered']) + "\nDate: " + str(Global['Date'])
        print("\n"+string)
        context.bot.send_message(chat_id=update.effective_chat.id, text=string)
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Error, something went wrong.")

def country(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    data = response.json()
    reply = str(update.message.text)
    print("\nUser's Reply :", reply)
    for x in data["Countries"]:
        if (x['Country'] == reply[1:]):
            # print(x)
            string = "Country: " + str(x['Country']) + "\nTotal Cases: " + str(x['TotalConfirmed']) + "\nNew Cases: " + str(x['NewConfirmed']) + "\nTotal Deaths: " + str(
                x['TotalDeaths']) + "\nNew Deaths: " + str(x['NewDeaths']) + "\nTotal Recovered: " + str(x['TotalRecovered']) + "\nNew Recovered: " + str(x['NewRecovered']) + "\nDate: " + str(x['Date'])
            print("\n"+string)
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=string)
            break

def display(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="For Global Cases, press-> /Global \nFor Country Wise Cases, \nEnter /country_name (first letter capital)")

c = CommandHandler('New',display)
dispatcher.add_handler(c)
updater.start_polling()
corona_summary_handler = CommandHandler('Global', summary)
dispatcher.add_handler(corona_summary_handler)
updater.start_polling()
unknown_handler = MessageHandler(Filters.command, country)
dispatcher.add_handler(unknown_handler)
updater.start_polling()

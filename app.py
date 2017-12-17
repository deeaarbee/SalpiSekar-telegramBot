# import telepot
# token = '503973362:AAFQtH-5KKljy-jIR-Eb66PfJFpkOI4GtHE'
# TelegramBot = telepot.Bot(token)
# print (TelegramBot.getMe())
# #print(TelegramBot.getUpdates())
# chat_id = #
# TelegramBot.sendMessage(chat_id, 'Hi, I am Mr.Salpi Sekar.')
#
import simplejson, urllib.request
from datetime import date
import calendar
from telegram.ext import Updater,MessageHandler, Filters
from telegram.ext import CommandHandler

#CONSTANTS

credits={
    "o":10,
    "O":10,
    "a+":9,
    "A+":9,
    "a":8,
    "A":8,
    "B+":7,
    "b+":7,
    "B":6,
    "b":6
}

result = 0
i = 0


updater = Updater(token='503973362:AAFQtH-5KKljy-jIR-Eb66PfJFpkOI4GtHE')
dispatcher = updater.dispatcher


def start(bot, update):
    origin_address = "#"
    destination_address = "1, 1st Cross Rd, Anna University, Kotturpuram, Chennai, Tamil Nadu 600025"

    url = 'http://maps.googleapis.com/maps/api/distancematrix/json?%s' % urllib.parse.urlencode((
        ('origins', origin_address),
        ('destinations', destination_address),
        ('mode', 'driving'),
        ('language', 'en-EN'),
        ('sensor', 'false')
    ))

    result = simplejson.load(urllib.request.urlopen(url))
    driving_time = result['rows'][0]['elements'][0]['duration']['text']
    print(driving_time)
    bot.sendMessage(chat_id=update.message.chat_id , text="It takes "+driving_time+" to reach college today")

def echo(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


#PROBLEM IN THIS FUNCTION. MAKE THIS WORK ASAP
def gpa(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text="How many Credits for this sem, Saar? ")
    totcre = int(update.message.text)
    print("above 4 cred")
    print(totcre)

    if int(totcre) in range(10,35):
        bot.sendMessage(chat_id=update.message.chat_id, text="Saar, Olunga enter pannunga Saar ")
        print("inside tot check cred")
        totalcredits = int( update.message.text )

    print(totalcredits)


    bot.sendMessage(chat_id=update.message.chat_id, text="How many 4 Credit Subjects, Saar? ")
    fourcedits = int(update.message.text)

    if fourcedits not in range(0,4):
        bot.sendMessage(chat_id=update.message.chat_id, text="Iyya, Please enter only a Single Digit.")


        print(fourcedits)
        if fourcedits>0:
            for i in range(1,fourcedits,step=1):
                bot.sendMessage(chat_id=update.message.chat_id, text="Enter the grade of your Four Credit subject")
                temp = int(update.message.text)
                result = result + credits[str(temp)] * 4

        bot.sendMessage(chat_id=update.message.chat_id, text="How many 3 Credit Subjects, Saar? ")
        if update.message.text not in range(0, 4):
            bot.sendMessage(chat_id=update.message.chat_id, text="Saar, Please enter only a Single Digit.")
        threecredits = int(update.message.text)
        print(threecredits)
        if threecedits > 0:
            for i in range(1, threecredits, step=1):
                bot.sendMessage(chat_id=update.message.chat_id, text="Enter the grade of your Three Credit subject")
                result = result + credits[str(update.message.text)] * 3

        bot.sendMessage(chat_id=update.message.chat_id, text="How many 2 Credit Subjects, Saar? ")
        if update.message.text not in range(0, 4):
            bot.sendMessage(chat_id=update.message.chat_id, text="Saar, Please enter only a Single Digit.")
        twocredits = int(update.message.text)
        print("in two creds" + twocredits)
        if twocredits > 0:
            for i in range(1, twocredits, step=1):
                bot.sendMessage(chat_id=update.message.chat_id, text="Enter the grade of your Two Credit subject")
                result = result + credits[str(update.message.text)] * 2

        result= result/totalcredits
        print(result)




start_handler = CommandHandler('start', start)
gpa_handler = CommandHandler('gpa',gpa)
echo_handler = MessageHandler(Filters.text,start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(gpa_handler)

updater.start_polling()


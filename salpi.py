import requests, pyowm, random
from telegram.ext import Updater, CommandHandler

quotes = {
    '1': "The Struggle you are in today is developing you for tomorrow",
    '2': "Success doesn't come from what you do occasionally, but what you do consistently ",
    '3': "You are capable of doing everything, JUST DO IT!",
    '4': "Dei college poda naaye",
    '5': "Today you have Raghi Mam Class!"
}
coin = ["Heads", "Tails"]

updater = Updater(token='503973362:AAFQtH-5KKljy-jIR-Eb66PfJFpkOI4GtHE')
dispatcher = updater.dispatcher


def start(bot, update):
    update.message.reply_text("I am Salpi-Sekar. Please make a Salpi request /help")


def weather(bot, update):
    owm = pyowm.OWM('43b1aa5e0641d33028a51ef4a9cc0721')
    observation = owm.weather_at_place("Chennai, India")
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')
    update.message.reply_text('The temperature outside is ' + str(temperature['temp']) + 'C')


def apdina(bot, update):
    txt = update.message.text
    txt = str(txt)
    txt = txt.replace('/apdina', '')
    txt = txt.lstrip()

    app_id = 'f7b879e8'
    app_key = 'bd587c9722f3fe842917b104455cfaa4'
    language = 'en'
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + txt.lower()
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    if r.status_code != 200:
        update.message.reply_text("Poda dubukku Mandaya :P  \nOlunga enter karo.")

    r = r.json()
    r1 = r['results']
    r2 = r1[0]['lexicalEntries']
    r3 = r2[0]['entries']
    r4 = r3[0]['senses']

    meaning = r4[0]['definitions']
    update.message.reply_text(meaning[0])


def coinflip(bot, update):
    update.message.reply_text(random.choice(coin))


def motivation(bot, update):
    dummy = random.randint(1, 5)
    update.message.reply_text(quotes[str(dummy)])


def about(bot, update):
    update.message.reply_text(
        "Dei I am the Sappa Bot of Telegram.\nFor more info about me, ask my Programmer @spidey07")


def help(bot, update):
    update.message.reply_text("This is all I can do for you : " +
                              " \n /weather - Get Weather Update" +
                              " \n /apdina (your word) - get meanings of English words" +
                              " \n /coinflip - Flip a coin" +
                              " \n /motivation - Motivate you to goto College" +
                              " \n /about - About me Salpi-Sekar"
                              )


def main():
    start_handler = CommandHandler('start', start)
    weather_handler = CommandHandler('weather', weather)
    apdina_handler = CommandHandler('apdina', apdina)
    coinflip_handler = CommandHandler('coinflip', coinflip)
    motivation_handler = CommandHandler('motivation', motivation)
    about_handler = CommandHandler('about', about)
    help_handler = CommandHandler('help', help)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(weather_handler)
    dispatcher.add_handler(apdina_handler)
    dispatcher.add_handler(coinflip_handler)
    dispatcher.add_handler(motivation_handler)
    dispatcher.add_handler(about_handler)
    dispatcher.add_handler(help_handler)

    updater.start_polling()
    updater.idle()
    updater.stop()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

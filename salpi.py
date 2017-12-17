import requests
import urllib.request,simplejson
import pyowm,random

quotes = {
    '1': "The Struggle you are in today is developing you for tomorrow",
    '2': "Success doesn't come from what you do occasionally, but what you do consistently ",
    '3': "You are capable of doing everything, JUST DO IT!",
    '4': "Dei college poda naaye",
    '5': "Today you have Raghi Mam Class!"
}


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

sekar = BotHandler("key")

def main():
    new_offset = None



    while True:

        sekar.get_updates(new_offset)

        last_update = sekar.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']


        if last_chat_text in ['/start'] :
            sekar.send_message(last_chat_id, 'I am SalpiSekar and I take care of getting you to college today somehow.. \n 1--> Weather Today \n 2-->Traffic to college \n 3-->College Motivation \n')


        elif last_chat_text in ['2','two'] :
            origin_address = "five furlong road, guindy,chennai"
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
            sekar.send_message(last_chat_id, text="It takes " + driving_time + " to reach college today")
            sekar.send_message(last_chat_id, 'I am SalpiSekar \n 1--> Weather \n 2-->College Ponum \n 3-->College Motivation \n')

        elif last_chat_text in ['1'] :
            owm = pyowm.OWM('key')
            observation = owm.weather_at_place("Chennai, India")
            w = observation.get_weather()
            temperature = w.get_temperature('celsius')
            sekar.send_message(last_chat_id, 'The temperature outside is '+ str(temperature['temp']) +'C')
            sekar.send_message(last_chat_id, 'I am SalpiSekar \n 1--> Weather \n 2-->College Ponum \n 3-->College Motivation \n')


        elif last_chat_text in ['3']:
            dummy  = random.randint(1,5)
            sekar.send_message(last_chat_id, quotes[str(dummy)])
            sekar.send_message(last_chat_id, 'I am SalpiSekar \n 1--> Weather \n 2-->College Ponum \n 3-->College Motivation \n')




        new_offset = last_update_id + 1



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
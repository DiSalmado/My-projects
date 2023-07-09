import schedule
import requests
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': #Mobile number here,
        'message': 'Hey, Good morning',
        'key': 'textbelt'
    })
    print(resp.json())


# schedule.every().day.at('12:00').do(send_message)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)


# NEED TO FIND AN API THAT WORKS FOR THE UK

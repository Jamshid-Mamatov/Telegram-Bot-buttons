import requests
import json
from pprint import pprint
import os

token=os.environ['token']
api_key=os.environ['api_key']

def update():

    url=f"https://api.telegram.org/bot{token}/getUpdates"

    r=requests.get(url)
    # print(r.url)
    data=r.json()
    # print(data)
    text=data['result'][-1]['message']['text']
    chat_id=data['result'][-1]['message']['chat']['id']
    update_id=data['result'][-1]['update_id']
    inform=[chat_id,update_id,text]

    return inform

# print(update())

def sendKeyboard(chat_id):
    url=f"https://api.telegram.org/bot{token}/sendMessage"

    payload={
        "chat_id":chat_id,
        "text":"If you want to know the weather forecast, press the button",
        "reply_markup" :{
            "keyboard":[
                [{'text':"location",
            "request_location":True}]
            ],
            "resize_keyboard":True
        }
    }
    r=requests.get(url,json=payload)
    return r.json()


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
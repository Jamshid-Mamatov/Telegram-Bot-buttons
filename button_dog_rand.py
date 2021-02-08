import requests
import json
import os
from pprint import pprint
token=os.environ['token']

def update():
    url=f"https://api.telegram.org/bot{token}/getUpdates"
    r=requests.get(url)

    data=r.json()['result']
    text=data[-1]['message']['text']
    chat_id=data[-1]['message']['chat']['id']
    inform=[text,chat_id]

    return inform


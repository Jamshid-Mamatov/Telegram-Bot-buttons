import requests
import json 
import os
from pprint import pprint

token=os.environ['token']


ids=[]

def update():
    url=f"https://api.telegram.org/bot{token}/getUpdates"
    r=requests.get(url)

    data=r.json()
    
    chat_id=data['result'][-1]['message']['chat']['id']
    

    return chat_id

def send_keyboard(id):
    url=f"https://api.telegram.org/bot{token}/sendMessage"
    payload={
        'chat_id':id,
        'text':"button",
        'reply_markup':{
            'keyboard':[['Yes,they certainly are'],["I'm not quite sure"],["NO.😡"]]
        }
    }

    r=requests.get(url,json=payload)

while True:

    chat_id=update()
    
    
    if chat_id not in  ids:
        send_keyboard(chat_id)
        ids.append(chat_id)
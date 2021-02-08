import requests
import json
import os
from pprint import pprint
token=os.environ['token']

ids=[]
last_update_id=None

def update():
    url=f"https://api.telegram.org/bot{token}/getUpdates"
    r=requests.get(url)

    data=r.json()['result']
    text=data[-1]['message']['text']
    chat_id=data[-1]['message']['chat']['id']
    update_id=data[-1]['update_id']
    inform=[text,chat_id,update_id]

    return inform


def sendMessage(id):
    url=f"https://api.telegram.org/bot{token}/sendMessage"
    payload={
        "chat_id":id,
        'text':"If you need a photo, press the button",
        "reply_markup":{
            "keyboard":[["🐶"]],
            "resize_keyboard":True
        }
    }
    r=requests.get(url,json=payload)
    



def sendPhoto(chat_id):
    url=f"https://api.telegram.org/bot{token}/sendPhoto"

    url_dog='https://random.dog/'
    r=requests.get(url_dog)

    url_rand_dog=str(r.text)

    ind_start=url_rand_dog.find("src=")+5
    ind_end=url_rand_dog.find(" />",ind_start)-1
    dog=url_rand_dog[ind_start:ind_end]
    
    photo_url=f"{url_dog}{dog}"

    payload={
        'chat_id':chat_id,
        "photo":photo_url
    }

    r=requests.get(url,payload)
    


while True:

    lst=update()
    new_update_id=lst[2]
    text=lst[0]
    id=lst[1]

    if last_update_id!=new_update_id:
        last_update_id=new_update_id
        if id not in ids :
            sendMessage(id)
            ids.append(id)
        elif text=="🐶":
            sendPhoto(id)
import requests
import json
from pprint import pprint
import os

token=os.environ['token']
api_key=os.environ['api_key']
old_update_id=None
ids=[]

def update():

    url=f"https://api.telegram.org/bot{token}/getUpdates"

    r=requests.get(url)
    
    data=r.json()
    
    
    chat_id=data['result'][-1]['message']['chat']['id']
    update_id=data['result'][-1]['update_id']   
    

    inform=[chat_id,update_id]
    
    return inform

def get_location():
    url=f"https://api.telegram.org/bot{token}/getUpdates"

    r=requests.get(url)
    
    data=r.json()
    location=data['result'][-1]['message'].get('location')
    return location


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

   
    
    

def weather(lon,lat):
    url=f"https://api.openweathermap.org/data/2.5/weather"
    payload={
        "lat":lat,
        'lon':lon,
        'appid':api_key
    }
    r=requests.get(url,payload)

    data=r.json()

    country=data['name']
    temp=int(data['main']['temp']-273.15)
    icon=data['weather'][0]['icon']
    description=data['weather'][0]['description']
    wind=data['wind']['speed']

    inform_weather=f"from:{country}\nTemp:{temp} {icon}\nDescription:{description}\nWind:{wind} m/s"

    return inform_weather

def sendMessage(id):
    url=f"https://api.telegram.org/bot{token}/sendMessage"

    location=get_location()

    if location==None:
        text="city not found"
    else:
        lon=location['longitude']
        lat=location['latitude']   
        text=weather(lon,lat)

    payload={
        "chat_id":id,
        "text":text
    }

    r=requests.get(url,payload)

while True:
    lst=update()
    id=lst[0]
    new_update_id=lst[1]   
    
    

    if old_update_id!=new_update_id:
        old_update_id=new_update_id

        if id not in ids:
            sendKeyboard(id)
            ids.append(id)
        sendMessage(id)


        

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
    location=data['result'][-1]['message'].get('location')

    inform=[chat_id,update_id,location]
    print(2)
    return inform



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
    print(1)
   
    
    

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


while True:
    lst=update()
    id=lst[0]
    new_update_id=lst[1]   
    location=lst[2]
    print(lst)
    if old_update_id!=new_update_id:
        old_update_id=new_update_id
        if id not in ids:
            sendKeyboard(id)
            ids.append(id)
        elif location!=None:
            lon=location['longitude']
            lat=location['latitude']
            weather(lon,lat)
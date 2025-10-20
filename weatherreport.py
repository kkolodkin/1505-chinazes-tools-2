import requests
import json
r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=55.7558&longitude=37.6176&current_weather=true')
json = r.json()
e = json['current_weather']
print(f"Температура воздуха в Москве:{e['temperature']} Скорость ветра:{e['windspeed']}")
if e['is_day'] == 1:
    print('Сейчас день')
else:
    print('Сейчас ночь')

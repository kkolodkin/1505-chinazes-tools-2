import requests
import json
from googletrans import Translator
resp = requests.get('http://api.quotable.io/random')
e = resp.json()
translator = Translator()
trans = translator.translate(e['content'], src='en', dest='ru')
#Савва Орлов лох
print(trans.text, e['author'])






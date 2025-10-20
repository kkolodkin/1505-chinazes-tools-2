text = input()
from googletrans import Translator
translator = Translator()           #савва орлов лох
trans = translator.translate(text, src='en', dest='ru')
print(trans.text)

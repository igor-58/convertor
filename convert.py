# -*- coding:utf-8 -*-
import requests
from datetime import datetime

resp = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
dt = datetime.now().date() 
kurs =0 
char_code = input('Введите буквенный код валюты: ')
if char_code in resp['Valute']:
    kurs = resp['Valute'][char_code]['Value']    
print(f'{char_code} {dt} стоит {kurs:.2f} RUB.')
summ = int(input('Введите сумму: '))
print(f'{summ} {char_code} стоит {kurs*summ:.2f} RUB.')
print('End')



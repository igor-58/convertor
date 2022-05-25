# -*- coding:utf-8 -*-
import requests
from datetime import datetime

# словарь из json файла
def respons():
    resp = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    return resp

# курс валюты 
def get_kurs(code):
    res = respons()
    if code in res['Valute']: 
        result = res['Valute'][code]['Value']
        return result

# номинал валюты
def get_nominal(code):
    res = respons()
    if code in res['Valute']: 
        result = res['Valute'][code]['Nominal']
        return result

# проверка правильности ввода кода валюты
def valid_code(code):
    dt = datetime.now().date() 
    res = respons()
    if code not in res['Valute']:
        print('неправильный код')
    else:
        print(f'{code} {dt} стоит {get_kurs(code):.2f} RUB.')
        summ = int(input('Введите сумму: '))
        print(f'{summ} {code} стоит {((get_kurs(code)*summ)/get_nominal(code)):.2f} RUB.')
        
# запрос к пользователю
def spros():
    char_code = input('Введите буквенный код валюты: ')
    return char_code
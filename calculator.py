# -*- coding:utf-8 -*-
import requests

class InvalidCurrency(Exception):
    pass

class Calculator:
    def __init__(self):
        self.rates = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        
    # расчет конвертации валюты    
    def calculate(self, currency, amount):
        if currency not in self.rates['Valute']:
            raise InvalidCurrency()
        nominal = self.rates['Valute'][currency]['Nominal']
        rate_api = self.rates['Valute'][currency]['Value']
        return (rate_api * amount) / nominal
    
    # получить стоимость валюты
    def get_rate(self, currency):
        if currency not in self.rates['Valute']:
            raise InvalidCurrency()
        return self.rates['Valute'][currency]['Value']
    
    # получить номинал валюты
    def get_nominal(self, currency):
        if currency not in self.rates['Valute']:
            raise InvalidCurrency()
        return self.rates['Valute'][currency]['Nominal']
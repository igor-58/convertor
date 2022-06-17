import requests

class InvalidCurrency(Exception):
    pass

class Calculator_Currency_From_To:
    def __init__(self):
        self.rates = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        
    # расчет стоимости 1 еденицы валюты
    def rate_currency(self, currency, nom):
        if currency not in self.rates['Valute']:
            raise InvalidCurrency()
        rate = self.rates['Valute'][currency]['Value']
        nom = self.rates['Valute'][currency]['Nominal']
        return rate/nom
    
    # получение номинала валюты
    def get_nominal(self, currency):
        if currency not in self.rates['Valute']:
            raise InvalidCurrency()
        return self.rates['Valute'][currency]['Nominal']
    
    # конвертация валют
    def converter(self, course, course_convert, summ):
        return (course/course_convert)*summ
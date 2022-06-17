# -*- coding:utf-8 -*-
from datetime import datetime
from calculator import Calculator_Currency_From_To, InvalidCurrency

def main():
    dt = datetime.now().date() 
    convertor = Calculator_Currency_From_To()
    currency_code = input('Введите код валюты: ').upper()
    try:
        nominal_currancy = convertor.get_nominal(currency_code)
        currency_code_convert = input('Введите код валюты для конвертации: ').upper()
        nominal_convert_currancy = convertor.get_nominal(currency_code_convert)
        rate_curr = convertor.rate_currency(currency_code, nominal_currancy)
        rate_convert_curr = convertor.rate_currency(currency_code_convert, nominal_convert_currancy)
        currency_amount = float(input('Введите сумму: '))
        currency_value = convertor.converter(rate_curr, rate_convert_curr, currency_amount)
        print(f'{currency_amount} "{currency_code}" на {dt} стоит {currency_value:.2f} "{currency_code_convert}".')
    except InvalidCurrency:
        print('неправильный код валюты')
    except ValueError:
        print('сумма должна быть числом')
        
main()
    

from datetime import datetime

def main():
    dt = datetime.now().date() 
    calculator = Calculator()
    code_currancy = input('Введите буквенный код валюты: ').upper()
    try:
        rate_api = calculator.get_rate(code_currancy)
        nominal = calculator.get_nominal(code_currancy)
        print(f'{nominal} "{code_currancy}" {dt} стоит {rate_api:.2f} RUB.')
        amount_currency = int(input('Введите сумму: '))
        sum_user = calculator.calculate(code_currancy, amount_currency)
        print(f'{amount_currency} "{code_currancy}" стоит "{sum_user:.2f}" RUB.')
    except InvalidCurrency:
        print("Неправильный код")

main()
#print('End')

# Написать программу – конвертер валют. Реализовать
# общение с пользователем через меню.

import requests as req
import json


def write(n, t, f):
    file = open(n, f)
    file.write(t)
    file.close()


def ftext(f):
    file = open(f)
    text = file.read()
    file.close()
    return text


path = 'rates'
response = req.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
if response.status_code > 400:
    rates = json.loads(ftext(path))
else:
    rates = response.json()
    write(path, json.dumps(rates), "w")


currencies = [i['cc'] for i in rates]
currencies.append('UAH')


def find_rate(curr, r):
    for i in r:
        if i['cc'] == curr:
            return i['rate']


def exchange(f, t, a):
    global rates
    global currencies
    if f == t == 'UAH':
        return a
    elif f == 'UAH':
        return round((a / find_rate(t, rates)), 4)
    elif t == 'UAH':
        return round((a * find_rate(f, rates)), 4)
    else:
        return round((a * find_rate(f, rates) / find_rate(t, rates)), 4)


for i, k in enumerate(sorted(currencies), start=1):
    print(k, end=" ")
    if i % 10 == 0:
        print("")
while True:
    from_currency = input("\n\nFrom: ").upper()
    if from_currency not in currencies:
        break
    to_currency = input("To: ").upper()
    if to_currency not in currencies:
        break
    try:
        amount = float(input("Amount: "))
        result = exchange(from_currency, to_currency, amount)
        print(f"{amount} {from_currency} = {result} {to_currency}\nDate: {rates[0]['exchangedate']}")
    except ValueError:
        print("wrong input")

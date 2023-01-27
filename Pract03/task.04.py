# Пользователь вводит с клавиатуры температуру по шкале Цельсия.
# Требуется перевести температуру в градусы по Фаренгейту и вывести на экран.

try:
    celcius_value = float(input("Input degrees in Celcius: "))
    farenheit_value = (celcius_value * (9/5)) + 32
    degree_sign = u'\N{DEGREE SIGN}'
    print(f"{celcius_value}{degree_sign}C equals {farenheit_value}{degree_sign}F")
except:
    print("Wrong value")

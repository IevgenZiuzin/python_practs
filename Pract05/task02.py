# Пользователь вводит с клавиатуры диаметр окружности.
# В зависимости от выбора пользователя посчитать
# площадь или периметр окружности.

from math import pi

while True:
    try:
        diameter = float(input("Input circle diameter: "))
        query = input("1 - circle area\n2 - circle circumference\n3 - quit\n: ")

        if query == "1":
            print("area: %.2f" % (pi * ((diameter / 2) ** 2)))
        elif query == "2":
            print("circumference: %.2f" % (2 * pi * (diameter / 2)))
        elif query == "3":
            break
    except:
        print("Wrong value")
# Напишите программу, вычисляющую площадь прямоугольника.
# Пользователь с клавиатуры вводит ширину и высоту прямоугольника.

try:
    num1 = float(input("Type width: "))
    num2 = float(input("Type height: "))
    print("\t\tArea: %.1f%s" % ((num1 * num2), " square units"))
except:
    print("Wrong value")
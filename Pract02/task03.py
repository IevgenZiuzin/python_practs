# Пользователь вводит с клавиатуры два числа. Необходимо найти
# сумму чисел, разницу чисел, произведение числе.
# Результат вычислений вывести на экран.

try:
    num1 = float(input("Type number 1: "))
    num2 = float(input("Type number 2: "))
    print("\t\tSum: %.1f\n\t\tDiff: %.1f\n\t\tProd: %.1f" % (num1 + num2, num1 - num2, num1 * num2))
except:
    print("Wrong value")

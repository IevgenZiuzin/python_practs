# Пользователь вводит с клавиатуры два числа. \
# Первое число — это значение, второе число процент, который необходимо посчитать.
# Например, мы ввели с клавиатуры 50 и 10. Требуется вывести на экран
# 10 процентов от 50. Результат: 5

try:
    num1 = float(input("Type number 1: "))
    num2 = float(input("Type number 2: "))
    print("\t\tPercents: %.1f%s" % (((num1 / 100) * num2), "%"))
except:
    print("Wrong value")
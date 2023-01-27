# Пользователь вводит с клавиатуры число. Требуется
# посчитать факториал числа. Например, если введено 3,
# факториал числа 1*2*3 = 6.
# Формула для расчета факториала: n! = 1*2*3…*n, где
# n — число для расчета факториала.

try:
    number = int(input("Type number: "))

    result = 1

    for i in range(1, number + 1):
        result *= i
    print(f"{number}! = {result}")

except:
    print("wrong value")
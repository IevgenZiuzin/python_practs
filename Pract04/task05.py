# Пользователь вводит с клавиатуры два числа. В зависимости от выбора
# пользователя нужно показать сумму двух чисел, разницу двух чисел, среднеарифметическое
# или произведение двух чисел.

try:
    num_1 = float(input("Type first number: "))
    num_2 = float(input("Type second number: "))
    answer = input("1 - Sum\n2 - Difference\n3 - Average\n")
    if answer == "1":
        result = num_1 + num_2
    elif answer == "2":
        result = abs(num_1 - num_2)
    elif answer == "3":
        result = (num_1 + num_2) / 2
    print(result)
except:
    print("Wrong value")
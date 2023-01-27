# Пользователь вводит с клавиатуры два числа.
# Необходимо найти минимум из двух чисел и показать его на экран.

try:
    num_1 = float(input("Type first number: "))
    num_2 = float(input("Type second number: "))
    if num_1 < num_2:
        print(num_1)
    elif num_1 > num_2:
        print(num_2)
    else:
        print("equal numbers")
except:
    print("Wrong value")
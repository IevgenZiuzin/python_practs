# Пользователь вводит с клавиатуры две цифры. Необходимо создать число, содержащее эти цифры.
# Например, если с клавиатуры введено 9, 7, тогда нжуно сформировать число 97.

try:
    digit_1 = input("Type first digit: ")
    digit_2 = input("Type second digit: ")
    num = int(digit_1 + digit_2)
    print(num, "Next:", num+1)
except:
    print("Wrong value")
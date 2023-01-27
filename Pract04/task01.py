# Пользователь вводит с клавиатуры число. Необходимо проверить его на четность и нечетность.
# Если число четное требуется вывести на экран число и надпись Even number.
# Если число нечетное выведите на экран число и надпись Odd number.

try:
    number = int(input("Type number: "))
    if number % 2 != 0:
        print(number, "Odd number")
    else:
        if number == 0:
            print(number, "Null")
        else:
            print(number, "Even number")
except:
    print("Wrong value")

# Пользователь с клавиатуры вводит двухзначное число. Например, 26.
# Нужно показать на разных строках значение первого и второго разряда.
# В нашем случае это будет выглядеть так:
# 2
# 6

try:
    num = input("Type two-digits number: ")
    for i in num:
        print(i)
except:
    print("Wrong value")
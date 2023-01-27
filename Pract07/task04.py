# Пользователь вводит с клавиатуры два числа.
# Нужно показать все числа в указанном диапазоне в порядке убывания.

try:
    numbers = (int(input("Type number one: ")), int(input("Type number two: ")))

    start = max(numbers)
    end = min(numbers)

    for i in range(start, end - 1, -1):
        print(i, end=" ")
except:
    print("wrong value")
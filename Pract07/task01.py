# Пользователь вводит с клавиатуры два числа. Нужно
# показать все числа в указанном диапазоне.

try:
    numbers = (int(input("Type number one: ")), int(input("Type number two: ")))

    start = min(numbers)
    end = max(numbers)

    for i in range(start, end + 1, 1):
        print(i, end=" ")
except:
    print("wrong value")




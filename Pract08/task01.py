# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать сумму чисел в указанном диапазоне, а также
# среднеарифметическое.

try:
    numbers = (int(input("Type number one: ")), int(input("Type number two: ")))

    start = min(numbers)
    end = max(numbers)

    total = 0

    for i in range(start, end + 1):
        total += i
    print(f"Sum: {total}, Average: {total / i}")

except:
    print("wrong value")
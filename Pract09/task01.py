# Показать таблицу умножения для числа, введенного
# пользователем. Например, если пользователь вводит
# число 7, нужно показать:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# …

try:
    number = int(input("Type number: "))
    for i in range(1, 11):
        print(f"{i} * {number} = {i * number}")
except:
    print("wrong value")

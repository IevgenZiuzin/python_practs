# Пользовательно вводит число.
# Определить количество цифр в этом числе, посчитать их сумму и среднее арифметическое.
# Определить количество нулей в этом числе.
# Общение с пользователем организовать через меню.

while True:
    user_number = input("Type integer (not integer for exit): ")
    if user_number.isdecimal():
        numbers = [int(i) for i in user_number]
        while True:
            query = input("1 - Digits amount\n2 - Sum\n3 - Average\n4 - Zero amount\n5 - Another integer\n: ")
            if query == "1":
                print(f"\nDigits amount: {len(numbers)}\n")
            elif query == "2":
                print(f"\nSum: {sum(numbers)}\n")
            elif query == "3":
                print(f"\nAverage: {round((sum(numbers) / len(numbers)), 2)}\n")
            elif query == "4":
                print(f"\nZero amount: {numbers.count(0)}\n")
            elif query == "5":
                break
    else:
        break






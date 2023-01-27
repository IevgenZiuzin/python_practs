# Пользователь вводит с клавиатуры время в секундах, прошедшее с начала дня.
# В зависимости от выбора пользователя посчитать, сколько часов, минут и секунд осталось до полуночи.

while True:
    try:
        total_seconds = 24 * 60 * 60
        gone_seconds = int(input("Input seconds value: "))
        left_seconds = total_seconds - gone_seconds

        query = input("1 - hours left\n2 - minutes left\n3 - seconds left\n4 - quit\n: ")

        if query == "1":
            result = f"{left_seconds // (60 * 60)} hours left"
        elif query == "2":
            result = f"{left_seconds // 60} minutes left"
        elif query == "3":
            result = f"{left_seconds} seconds left"
        elif query == "4":
            break
        print(result)
    except:
        print("Wrong value")
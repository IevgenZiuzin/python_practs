# Пользователь с клавиатуры вводит количество часов.
# Если полученное значение находится в диапазоне
# от 0 до 6 нужно вывести надпись Good Night,
# если в диапазоне от 6 до 13 Good Morning,
# если в диапазоне от 13 до 17 Good Day,
# если в диапазоне от 17 до 0 Good Evening. \
# Верхняя граница диапазона не включается. Например, число 6 относится к 6 до 13.

while True:
    try:
        hour = int(input("Enter hour: "))

        if 0 <= hour < 6:
            result = "Good Night!"
        elif 6 <= hour < 13:
            result = "Good Morning!"
        elif 13 <= hour < 17:
            result = "Good Day!"
        elif 17 <= hour <= 23:
            result = "Good Evening!"
        else:
            result = "wrong value"
        print(result)
    except:
        print("wrong value")
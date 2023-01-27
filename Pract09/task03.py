# Пользователь вводит с клавиатуры две границы диапазона и число.
# Если число не попадает в диапазон,
# программа просит пользователя повторно ввести число,
# и так до тех пор, пока он не введет число правильно.
# Программа отображает все числа диапазона,
# выделяя число восклицательными знаками.
# Например: 1 2 3 !4! 5 6 7.


numbers = (int(input("Type range start: ")), int(input("Type range end: ")))

start = min(numbers)
end = max(numbers)
while True:
    guess = int(input("Type number of range: "))
    if start < guess < end:
        for i in range(start, end + 1):
            if i == guess:
                print(f"!{guess}!", end=" ")
            else:
                print(i, end=" ")

    break

# Написать игру «Угадай число». Программа загадывает
# число в диапазоне от 1 до 500. Пользователь пытается
# его угадать. После каждой попытки программа выдает
# подсказки, больше или меньше его число загаданного.
# В конце программа выдает статистику: за сколько
# попыток угадано число, сколько времени это заняло.
# Предусмотреть выход по 0 в случае, если пользователю
# надоело угадывать число.

import random as r
import datetime as d

number = r.randint(1, 500)
tries = 0
more_message = "more"
less_message = "less"
start_time = d.datetime.now()
while True:
    guess = int(input("Guess number in range from 1 to 500 (or 0 for break): "))
    if guess == 0:
        break
    tries += 1
    if guess > number:
        print(less_message)
    elif guess < number:
        print(more_message)
    else:
        end_time = d.datetime.now()
        print(f'\nYes it is {number}. It has taken you: {tries} tries and {(end_time - start_time).seconds} seconds.')
        break

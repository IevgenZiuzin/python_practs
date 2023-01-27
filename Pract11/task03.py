# Написать программу, которая проверяет пользователя на знание таблицы умножения.
# Программа выводит на экран два числа, пользователь должен ввести их произведение.
# Разработать несколько уровней сложности
# (отличаются сложностью и количеством вопросов), Вывести пользователю оценку его знаний.


import random as r


class Level:
    def __init__(self, start, stop, tries, nums, skill):
        self.start = start
        self.stop = stop
        self.tries = tries
        self.nums = nums
        self.skill = skill


def level(n):
    if n == 0:
        return Level(2, 5, 5, 2, "junior")
    if n == 1:
        return Level(6, 9, 4, 2, "middle")
    if n == 2:
        return Level(6, 9, 3, 3, "senior")


def product(arr):
    result = 1
    for num in arr:
        result *= num
    return result


total_score = 0
tries = 0
levels = 3
used_randoms = []
skill = "trainee"
end_game = False

for i in range(levels):
    total_score += level(i).tries

print("\n(type not integer for break)")

for i in range(levels):

    if end_game:
        break

    l = level(i)

    print(f"\nLevel {i + 1}\n")

    for k in range(l.tries):

        while True:
            randoms = [r.randint(l.start, l.stop) for i in range(l.nums)]
            if randoms not in used_randoms:
                used_randoms.append(randoms)
                break

        exp = " * ".join([str(i) for i in randoms])
        guess = input(f"\n{exp} = ")

        if not guess.isdecimal():

            print("\nSee you next time.")
            end_game = True
            break

        else:

            if int(guess) != product(randoms):

                print(f"Wrong answer. {exp} = {product(randoms)}\n")
                end_game = True
                break

            else:

                tries += 1
                if k == l.tries - 1:
                    skill = l.skill

    print(f"\nYour multiplication skill is {skill}.\nScore: {round(tries / total_score * 100)}%")

if tries == total_score:
    print("Excellent!")

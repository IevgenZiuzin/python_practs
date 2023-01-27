import random

desc = """
Напишите функцию, которая проверяет является ли шестизначное число «счастливым».
Число передаётся в качестве параметра.
Если число счастливое нужно вернуть из функции true, иначе false.
«Счастливое шестизначное число» — это число у которого сумма первых трёх цифр равна сумме трёх вторых цифр.
Например, 123420 – счастливое 1+2+3 = 4+2+0, а 723422 – несчастливое 7+2+3 != 4+2+2."""


def check_lucky(n):
    numbers = [i for i in str(n)]
    return sum([int(i) for i in numbers[:3]]) == sum([int(i) for i in numbers[3:]])


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    number = random.randint(100000, 999999)
    lucky = 456087
    print(f'Random: {number}\n'
          f'Random is lucky: {check_lucky(number)}\n'
          f'Example: {lucky}\n'
          f'Example is lucky: {check_lucky(lucky)}')

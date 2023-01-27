import random

desc = """
Напишите функцию, которая принимает два числа 
в качестве параметра и отображает все нечетные числа 
между ними."""


def get_odds(start, end):
    first = min(start, end)
    last = max(start, end)
    return [number for number in range(first, last) if number % 2 != 0]


if __name__ == '__main__':
    print(f'{desc}\n----------')
    num1, num2 = random.randint(1, 20), random.randint(1, 20)
    print(f'Start: {min(num1, num2)}\n'
          f'End: {max(num1, num2)}\n'
          f'Odds: {get_odds(num1, num2)}\n')

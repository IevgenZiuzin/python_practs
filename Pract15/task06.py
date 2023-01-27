import random

desc = """
Напишите функцию, которая проверяет является ли 
число простым. Число передаётся в качестве параметра. 
Если число простое нужно вернуть из метода true, иначе 
false."""


def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(f'{desc}\n----------')
    number = random.randint(1, 100)
    print(f'Arg: {number}\n'
          f'Is prime: {check_prime(number)}')


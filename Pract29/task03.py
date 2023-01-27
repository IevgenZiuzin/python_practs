desc = """
Создайте класс для подсчета максимума из четырех 
аргументов, минимума из четырех аргументов,
среднеарифметического из четырех аргументов, факториала 
аргумента. Функциональность необходимо реализовать 
в виде статических методов.
"""


class Calc:

    @staticmethod
    def max_four(*args):
        return max(*args)

    @staticmethod
    def min_four(*args):
        return min(*args)

    @staticmethod
    def average_four(*args):
        return sum([*args]) / len([*args])

    @staticmethod
    def factorial(n):
        if n == 1:
            return n
        return n * Calc.factorial(n-1)


if __name__ == '__main__':
    print(f'{desc}\n----------\n')

print(Calc().factorial(7))
import math

desc = """
Напишите функцию, высчитывающую факториал каждого элемента списка целых.
Функция возвращает новый список, содержащий полученные факториалы."""


def factorials(collection):
    facts = [math.factorial(number) for number in collection]
    return facts


if __name__ == '__main__':
    pass

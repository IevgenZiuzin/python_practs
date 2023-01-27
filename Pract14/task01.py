import random
from functools import reduce

desc = """В списке целых, заполненном случайными числами вычислить:
■ Сумму отрицательных чисел;
■ Сумму четных чисел;
■ Сумму нечетных чисел;
■ Произведение элементов с индексами кратными 3;
■ Произведение элементов между минимальным и максимальным элементом;
■ Сумму элементов, находящихся между первым и последним положительными элементами"""


def collection_of_ten():
    return [random.choice([i for i in range(-10, 10)]) for _ in range(10)]


def sum_of_negative(collection):
    return sum([i for i in collection if i < 0])


def sum_of_even(collection):
    return sum([i for i in collection if i % 2 == 0])


def sum_of_odd(collection):
    return sum([i for i in collection if i % 2 != 0])


def product_of_index_mult_of_three(collection):
    return reduce(lambda a, b: a * b, [number for index, number in enumerate(collection) if index % 3 == 0], 1)


def sum_between_first_last_positive(collection: list):
    start = 0
    end = 0
    for i in collection:
        if i > 0:
            start = collection.index(i) + 1
            break
    for i in collection[::-1]:
        if i > 0:
            end = len(collection) - collection[::-1].index(i) - 1
            break
    return sum(collection[start:end])


def main():
    print(desc, '\n')
    collection = collection_of_ten()
    print(f'List: {collection}\n\n'
          f'Sum of negative: {sum_of_negative(collection)}\n'
          f'Sum of even: {sum_of_even(collection)}\n'
          f'Sum of odd: {sum_of_odd(collection)}\n'
          f'Product of numbers with indexes multiplied of three: {product_of_index_mult_of_three(collection)}\n'
          f'Sum of numbers between first and last positives: {sum_between_first_last_positive(collection)}')


if __name__ == '__main__':
    main()







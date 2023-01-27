import random

desc = """
Есть кортеж с целыми числами. Нужно вывести статистику по количеству цифр в элементах кортежа. Например:
■ Одна цифра — 3 элемента;
■ Две цифры — 4 элемента;
■ Три цифры — 5 элементов.
"""


def collection_of_ten():
    return tuple(random.choice([i for i in range(0, 150)]) for _ in range(10))


def digits_counter(numbers, digits=1):
    amount = 0
    for i in numbers:
        if len(str(i)) == digits:
            amount += 1
    return amount


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = collection_of_ten()
    print(f'Tuple: {collection}\n'
          f'One digit: {digits_counter(collection)} elements\n'
          f'Two digits: {digits_counter(collection, 2)} elements\n'
          f'Three digits: {digits_counter(collection, 3)} elements\n')

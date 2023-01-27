import random

desc = """
Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число, введенное 
пользователем. Используйте алгоритм бинарного поиска.
"""


def collection_of_ten():
    return [random.choice([i for i in range(0, 11)]) for _ in range(10)]


def binary_search(collection, value):
    left, right = 0, len(collection) - 1

    while left <= right:
        middle = (left + right) // 2

        if collection[middle] == value:
            return middle

        if collection[middle] < value:
            left = middle + 1
        elif collection[middle] > value:
            right = middle - 1
    return -1


def main():
    collection = collection_of_ten()
    rand_int = random.randint(0, 11)
    print(f'Collection: {collection}\n'
          f'Random int to find: {rand_int}\n'
          f'Result: {binary_search(collection, rand_int)}')


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    main()

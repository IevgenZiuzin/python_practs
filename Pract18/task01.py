import random

desc = """
Написать программу, выполняющую сортировку 
списка целых чисел методом пузырьковой сортировки."""


def collection_of_ten():
    return [random.choice([i for i in range(-10, 10)]) for _ in range(10)]


def bubble_sort(numbs):
    n = len(numbs)
    for i in range(1, n):
        for k in range(0, n-i):
            if numbs[k] > numbs[k + 1]:
                numbs[k], numbs[k + 1] = numbs[k + 1], numbs[k]
    return numbs


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = collection_of_ten()
    print(f'Collection: {collection}\n'
          f'Sorted: {bubble_sort(collection)}')



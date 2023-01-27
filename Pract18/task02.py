import random

desc = """
Написать программу, выполняющую сортировку 
списка целых чисел методом вставок."""


def collection_of_ten():
    return [random.choice([i for i in range(-10, 10)]) for _ in range(10)]


def insert_sort(numbs):
    N = len(numbs)
    for top in range(1, N):
        k = top
        while k > 0 and numbs[k - 1] > numbs[k]:
            numbs[k], numbs[k - 1] = numbs[k - 1], numbs[k]
            k -= 1
    return numbs


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = collection_of_ten()
    print(f'Collection: {collection}\n'
          f'Sorted: {insert_sort(collection)}')


import random


desc = """
Написать программу, выполняющую сортировку 
списка целых чисел методом Шелла.
"""


def collection_of_ten():
    return [random.choice([i for i in range(-10, 10)]) for _ in range(10)]


def shell_sort(collection):
    n = len(collection)
    gap = int(n // 2)

    while gap > 0:
        for i in range(gap, n):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
        gap = int(gap // 2)

    return collection


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = collection_of_ten()
    print(f'Collection: {collection}\n'
          f'Sorted: {shell_sort(collection)}')

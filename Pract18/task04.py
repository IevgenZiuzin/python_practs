import random

desc = """
Написать программу, выполняющую сортировку 
списка целых чисел методом слияния."""


def collection_of_ten():
    return [random.choice([i for i in range(-10, 10)]) for _ in range(10)]


def choise_sort(numbs):
    N = len(numbs)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if numbs[k] < numbs[pos]:
                numbs[k], numbs[pos] = numbs[pos], numbs[k]
    return numbs


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = collection_of_ten()
    print(f'Collection: {collection}\n'
          f'Sorted: {choise_sort(collection)}')

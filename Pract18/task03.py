import random

desc = """
Есть список целых. Необходимо первую половину 
списка отсортировать по убыванию, вторую половину 
по возрастанию."""


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


def split_and_sort(numbs):
    split_index = (len(numbs) // 2)
    return insert_sort(numbs[:split_index]) + insert_sort(numbs[split_index:])[::-1]


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = collection_of_ten()
    print(f'Collection: {collection}\n'
          f'Sorted: {split_and_sort(collection)}')


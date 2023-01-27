import random


desc = """
Есть стопка оладий различного радиуса. Единственная 
операция, проводимая с ними — между любыми двумя 
суем лопатку и меняем порядок оладий над лопаткой 
на обратный. Необходимо за минимальное количество 
операций таких отсортировать снизу вверх по убыванию 
радиуса.
"""


def collection_of_ten():
    return [random.choice([i for i in range(5, 10)]) for _ in range(10)]


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(collection, low, high):
    if low < high:
        pi = partition(collection, low, high)
        quick_sort(collection, low, pi - 1)
        quick_sort(collection, pi + 1, high)
    return collection


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = collection_of_ten()
    print(f'Collection: {collection}\n'
          f'Sorted: {quick_sort(collection, 0, len(collection) - 1)}')

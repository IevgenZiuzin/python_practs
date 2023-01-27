import random

desc = """
Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число, введенное 
пользователем. Используйте алгоритм линейного поиска.
"""


def collection_of_ten():
    return [random.choice([i for i in range(0, 11)]) for _ in range(10)]


def linear_search(collection, value):
    for item in collection:
        if value == item:
            return collection.index(item)
    return -1


def recursive_linear_search(collection, index, value):
    if index == -1:
        return -1
    if collection[index] == value:
        return index
    return recursive_linear_search(collection, index-1, value)


def main():
    collection = collection_of_ten()
    print(f'Collection: {collection}\n')
    while True:
        number = input('Number: ')
        if number.isdigit():
            print(f'Result: {linear_search(collection, int(number))}')
            break
        else:
            print("Integer expected")


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    main()


import copy
import random

desc = """Есть список целых, заполненный случайными числами. 
На основании данных этого массива нужно:
■ Создать список целых, содержащий только четные числа из первого списка;
■ Создать список целых, содержащий только нечетные числа из первого списка;
■ Создать список целых, содержащий только отрицательные числа из первого списка;
■ Создать список целых, содержащий только положительные числа из первого списка."""


def collection_of_ten():
    return [random.choice([i for i in range(-10, 10)]) for _ in range(10)]


def evens(collection):
    collection = copy.deepcopy(collection)
    return [number for number in collection if number % 2 == 0]


def odds(collection):
    collection = copy.deepcopy(collection)
    return [number for number in collection if number % 2 != 0]


def negatives(collection):
    collection = copy.deepcopy(collection)
    return [number for number in collection if number < 0]


def positives(collection):
    collection = copy.deepcopy(collection)
    return [number for number in collection if number > 0]


def main():
    print(desc, '\n')
    collection = collection_of_ten()
    print(f'List: {collection}\n\n'
          f'Evens: {evens(collection)}\n'
          f'Odds: {odds(collection)}\n'
          f'Negatives: {negatives(collection)}\n'
          f'Positives: {positives(collection)}\n')


if __name__ == '__main__':
    main()

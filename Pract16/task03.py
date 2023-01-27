import random

desc = """
Напишите функцию, определяющую количество 
чётных, нечётных, положительных, отрицательных элементов списка целых.
Список передаётся в качестве параметра."""

def collection_of_ten():
    return [random.choice([i for i in range(-10, 10)]) for _ in range(10)]


def evens(collection):
    return [number for number in collection if number % 2 == 0]


def odds(collection):
    return [number for number in collection if number % 2 != 0]


def negatives(collection):
    return [number for number in collection if number < 0]


def positives(collection):
    return [number for number in collection if number > 0]


def get_list_stat(collection):
    result = (evens(collection),
              odds(collection),
              negatives(collection),
              positives(collection))
    return result


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = collection_of_ten()
    result = get_list_stat(collection)
    print(f'List: {collection}\n'
          f'Evens: {result[0]}\n'
          f'Odds: {result[1]}\n'
          f'Negatives: {result[2]}\n'
          f'Positives: {result[3]}\n')


import random

desc = """
Есть кортеж с названиями производителей автомобилей (название производителя может встречаться 
от 0 до N раз). Пользователь вводит с клавиатуры название 
производителя и слово для замены. Необходимо заменить 
в кортеже все элементы с этим названием на слово для 
замены. Совпадение по названию должно быть полным.
"""

brands_list = ["Toyota", "Honda", "Chevrolet", "Ford", "Mercedes-Benz", "Jeep", "BMW", "Porsche", "Subaru",
               "Nissan"]


def get_tuple():
    global brands_list
    return tuple([random.choice(brands_list) for _ in range(10)])


def get_input():
    return input('Type replaceable: ').lower(), input('Type replacer: ').lower()


def replace(collection, replaceable, replacer):
    collection = list(collection)
    for index, value in enumerate(collection):
        if value.lower() == replaceable:
            collection[index] = replacer
    return tuple(collection)


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = get_tuple()
    print(f'Tuple:\n{collection}\n')
    print(f'Updated tuple:\n {replace(collection, *get_input())}')


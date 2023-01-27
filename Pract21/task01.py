import random

desc = """
Пользователь вводит с клавиатуры название фрукта. 
Необходимо вывести на экран количество раз, сколько 
фрукт встречается в кортеже в качестве элемента.
"""

fruits = ('lemon', 'apple', 'banana', 'cherry', 'orange', 'avocado', 'apricot', 'pear', 'kiwi', 'mango')


def get_fruits():
    global fruits
    return tuple([random.choice(fruits) for _ in range(6)])


def get_input():
    return input('Type fruit name: ').lower()


def count_occur(collection, key):
    amount = 0
    for i in collection:
        if i.lower() == key:
            amount += 1
    return amount


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = get_fruits()
    print(f'Fruits: {collection}')
    print(f'Occurrences: {count_occur(collection, get_input())}')

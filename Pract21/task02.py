import random

desc = """
Добавьте к заданию 1 подсчет количества раз, когда 
название фрукта является частью элемента. Например: 
banana, apple, bananamango, mango, strawberry-banana.
В примере выше banana встречается три раза.
"""


fruits = ('lemon', 'apple', 'banana', 'cherry', 'orange', 'avocado', 'apricot', 'pear', 'kiwi', 'mango')


def get_fruits():
    global fruits
    return tuple([random.choice(fruits) + random.choice(['', '-', ' ']) + random.choice(fruits) for _ in range(5)])


def get_input():
    return input('Type fruit name: ').lower()


def count_occur(collection, key):
    amount = 0
    for i in collection:
        amount += i.lower().count(key)
    return amount


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = get_fruits()
    print(f'Fruits: {collection}')
    print(f'Occurrences: {count_occur(collection, get_input())}')

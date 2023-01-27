import time

desc = """
Создайте приложение по выпечке пиццы. Каждая 
пицца содержит разные компоненты. Используя механизм 
декораторов создайте разные пиццы: 
■ Маргарита;
■ Четыре сыра;
■ Капричоза;
■ Гавайская.
"""


def margarita(f):
    def wrapper():
        print('\nMargarita in progress')
        time.sleep(1.5)
        f('Margarita')
    return wrapper


def four_cheeses(f):
    def wrapper():
        print('\nFour Cheeses in progress')
        time.sleep(1.5)
        f('Four cheeses')
    return wrapper


def capricciosa(f):
    def wrapper():
        print('\nCapricciosa in progress')
        time.sleep(1.5)
        f('Capricciosa')
    return wrapper


def hawaii(f):
    def wrapper():
        print('\nHawaii in progress')
        time.sleep(1.5)
        f('Hawaii')
    return wrapper


def bake(pizza_name):
    print(f'{pizza_name} is ready!\n')


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    pizzas = (margarita, four_cheeses, capricciosa, hawaii)
    choice = not None
    while choice:
        notfound = True
        for index, pizza in enumerate(pizzas, 1):
            print(f'{index}. {pizza.__name__.title()}', end=' ')
        print('\n')
        choice = input('Select, please: ')
        if not choice.isdigit():
            continue
        for index, pizza in enumerate(pizzas, 1):
            if str(index) == choice:
                notfound = False
                pizza = pizza(bake)
                pizza()
        if notfound:
            print('Not found')



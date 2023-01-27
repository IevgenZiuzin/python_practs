desc = """
Создать базовый класс «Домашнее животное» и производные классы «Собака», «Кошка», «Попугай», «Хомяк». 
С помощью конструктора установить имя каждого животного и его характеристики. Реализуйте для каждого 
из классов методы: 
■ Sound — издает звук животного (пишем текстом в консоль);
■ Show — отображает имя животного;
■ Type — отображает название его подвида;
"""


class DomesticAnimal:
    def __init__(self, name=None, subspecies=None):
        self._name = name
        self._subspecies = subspecies

    def show(self):
        print(self._name)

    def subspecies(self):
        return self._subspecies

    def sound(self):
        ...


class Dog(DomesticAnimal):
    def sound(self):
        print('wow-wow')


class Cat(DomesticAnimal):
    def sound(self):
        print('meow-meow')


class Parrot(DomesticAnimal):
    def sound(self):
        print('twitt-twitt')


class Hamster(DomesticAnimal):
    def sound(self):
        print('knack-knack')


def object_info(obj):
    class_name = obj.__class__.__name__
    attributes = [key for key in obj.__dict__.keys()]
    return f'Class name: {class_name}\n' \
           f'Attributes: {attributes}\n\n'


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    guys = [Cat('Pussy', 'felis'), Dog('Snoop', 'canis'), Parrot('Ed', 'cacatua'), Hamster('Hobo', 'cricetus')]
    for guy in guys:
        guy.show()
        guy.sound()
        print(object_info(guy))
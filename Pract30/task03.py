desc = """
Создать базовый класс «Животное» и производные 
классы «Тигр», «Крокодил», «Кенгуру».
С помощью конструктора установить 
имя каждого животного и его характеристики.
Создайте для каждого класса необходимые методы и поля.
"""


class Animal:
    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Tiger(Animal):
    pass


class Crocodile(Animal):
    pass


class Cangoroo(Animal):
    pass


def object_info(obj):
    class_name = obj.__class__.__name__
    attributes = [key for key in obj.__dict__.keys()]
    return f'Class name: {class_name}\n' \
           f'Attributes: {attributes}\n\n'


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    instances = [Tiger('tiger'), Crocodile('croco'), Cangoroo('cango')]
    for instance in instances:
        print(instance.name)
        print(object_info(instance))

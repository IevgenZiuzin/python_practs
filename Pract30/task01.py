desc = """
Создайте класс Human, который будет содержать 
информацию о человеке.
С помощью механизма наследования, реализуйте класс 
Builder (содержит информацию о строителе), класс Sailor 
(содержит информацию о моряке), класс Pilot (содержит 
информацию о летчике).
Каждый из классов должен содержать необходимые 
для работы методы.
"""


class Human:
    def __init__(self):
        self._name = None
        self._age = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


class Builder(Human):
    pass


class Sailor(Human):
    pass


class Pilot(Human):
    pass


def object_info(obj):
    class_name = obj.__class__.__name__
    attributes = [key for key in obj.__dict__.keys()]
    return f'Class name: {class_name}\n' \
           f'Attributes: {attributes}\n\n'


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    instances = [Human(), Builder(), Sailor(), Pilot()]
    for i in instances:
        print(object_info(i))
    sailor = Sailor()
    sailor.name = 'John'
    print(f'Setter test: {sailor.name}')

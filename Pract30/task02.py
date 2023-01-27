desc = """
Создайте класс Passport (паспорт), который будет 
содержать паспортную информацию о гражданине заданной страны.
С помощью механизма наследования, реализуйте 
класс ForeignPassport (загран.паспорт) производный от Passport.
Напомним, что заграничный паспорт содержит помимо паспортных данных,
также данные о визах, номер заграничного паспорта.
Каждый из классов должен содержать необходимые методы.
"""


class Passport:
    def __init__(self):
        self._name = None
        self._birth_date = None
        self._code = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value


class InternationalPassport(Passport):
    def __init__(self):
        super().__init__()
        self._visas = []

    @property
    def visas(self):
        return self._visas

    @visas.setter
    def visas(self, value):
        self._visas = value

    def add_visa(self, visa):
        self._visas.append(visa)


def object_info(obj):
    class_name = obj.__class__.__name__
    attributes = [key for key in obj.__dict__.keys()]
    return f'Class name: {class_name}\n' \
           f'Attributes: {attributes}\n\n'


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    instances = [Passport(), InternationalPassport()]
    for i in instances:
        print(object_info(i))
    int_pass = InternationalPassport()
    int_pass.name = 'John'
    print(f'Setter test: {int_pass.name}\n')
    int_pass.add_visa('some visa')
    print(f'Attributes test: {int_pass.__dict__}')

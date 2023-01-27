desc = """
К уже реализованному классу «Человек» добавьте 
статический метод, который при вызове возвращает
количество созданных объектов класса «Человек»
"""


class Human:
    __instances = 0

    def __init__(self):
        self._name = None
        self._birthdate = None
        self._phone = None
        self._city = None
        self._country = None
        self._address = None
        self.__instances += 1

    @staticmethod
    def instances():
        return Human.__instances

    @property
    def _name(self):
        return self._name

    @property
    def birthdate(self):
        return self._birthdate

    @property
    def phone(self):
        return self._phone

    @property
    def city(self):
        return self._city

    @property
    def country(self):
        return self._country

    @property
    def address(self):
        return self._address

    @_name.setter
    def _name(self, value):
        self._name = value

    @birthdate.setter
    def birthdate(self, value):
        self._birthdate = value

    @phone.setter
    def phone(self, value):
        self._phone = value

    @city.setter
    def city(self, value):
        self._city = value

    @country.setter
    def country(self, value):
        self._country = value

    @address.setter
    def address(self, value):
        self._address = value


if __name__ == '__main__':
    print(f'{desc}\n----------\n')

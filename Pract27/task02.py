desc = """
Создайте класс «Город». Необходимо хранить в полях класса: название города, название региона, название 
страны, количество жителей в городе, почтовый индекс 
города, телефонный код города. Реализуйте методы класса 
для ввода данных, вывода данных, реализуйте доступ к 
отдельным полям через методы класса.
"""


class City:
    def __init__(self):
        self._name = None
        self._region = None
        self._country = None
        self._population = None
        self._postcode = None
        self._phonecode = None

    @property
    def name(self):
        return self._name

    @property
    def region(self):
        return self._region

    @property
    def country(self):
        return self._country

    @property
    def population(self):
        return self._population

    @property
    def postcode(self):
        return self._postcode

    @property
    def phonecode(self):
        return self._phonecode

    @name.setter
    def name(self, value):
        self._name = value

    @region.setter
    def region(self, value):
        self._region = value

    @country.setter
    def country(self, value):
        self._country = value

    @population.setter
    def population(self, value):
        self._population = value

    @postcode.setter
    def postcode(self, value):
        self._postcode = value

    @phonecode.setter
    def phonecode(self, value):
        self._phonecode = value


if __name__ == '__main__':
    print(f'{desc}\n----------\n')

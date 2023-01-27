desc = """
Создайте класс «Страна». Необходимо хранить в 
полях класса: название страны, название континента, 
количество жителей в стране, телефонный код страны, 
название столицы, название городов страны. Реализуйте
методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса. 
"""


class Country:
    def __init__(self):
        self._name = None
        self._continent = None
        self._population = None
        self._phonecode = None
        self._capital = None
        self._cities = []

    @property
    def name(self):
        return self._name

    @property
    def continent(self):
        return self._continent

    @property
    def population(self):
        return self._population

    @property
    def phonecode(self):
        return self._phonecode

    @property
    def capital(self):
        return self._capital

    @property
    def cities(self):
        return self._cities

    @name.setter
    def name(self, value):
        self._name = value

    @continent.setter
    def continent(self, value):
        self._continent = value

    @population.setter
    def population(self, value):
        self._population = value

    @phonecode.setter
    def phonecode(self, value):
        self._phonecode = value

    @capital.setter
    def capital(self, value):
        self._capital = value

    @cities.setter
    def cities(self, value):
        self._cities = value


if __name__ == '__main__':
    print(f'{desc}\n----------\n')

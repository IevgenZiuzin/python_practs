desc = """
Создайте класс «Дробь». Необходимо хранить в полях 
класса: числитель и знаменатель. Реализуйте методы класса 
для ввода данных, вывода данных, реализуйте доступ к 
отдельным полям через методы класса. Также создайте 
методы класса для выполнения арифметических операций
(сложение, вычитание, умножение, деление, и т.д.)
"""


class Fraction:
    def __init__(self, dividend=None, divisor=None):
        self._dividend = dividend
        self._divisor = divisor

    @property
    def dividend(self):
        return self._dividend

    @property
    def divisor(self):
        return self._divisor

    @dividend.setter
    def dividend(self, value):
        self._dividend = value

    @divisor.setter
    def divisor(self, value):
        self._divisor = value

    @property
    def value(self):
        return self.dividend / self.divisor

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    print(f'Test add method: {Fraction(5, 10) + Fraction(3, 6)}')

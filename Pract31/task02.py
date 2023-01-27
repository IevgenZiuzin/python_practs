desc = """
Создайте класс Дробь (или используйте уже ранее 
созданный вами). Используя перегрузку операторов 
реализуйте для него арифметические операции для работы 
с дробями (операции +, -, *, /).
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
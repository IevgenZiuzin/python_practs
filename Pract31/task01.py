desc = """
Создайте класс Число (или используйте уже ранее 
созданный вами). Класс число хранит внутри одно значение.
Используя перегрузку операторов реализуйте для 
него арифметические операции для работы с числом 
(операции +, -, *, /).
"""


class Number:
    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __add__(self, other):
        return self._value + other.value

    def __sub__(self, other):
        return self._value - other.value

    def __mul__(self, other):
        return self._value * other.value

    def __truediv__(self, other):
        return self._value / other.value


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    print(f'Test methods: {Number(10) / Number(5)}')

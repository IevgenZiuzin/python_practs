from __future__ import annotations
from random import randint

desc = """
Создайте реализацию паттерна Facade. Протестируйте 
работу созданного класса.
"""


class Logic1:
    def get_nums(self):
        return [randint(1, 100) for _ in range(10)]

    def power(self):
        return list(map(lambda x: x ** 3, self.get_nums()))


class Logic2:
    def __init__(self):
        self.result = None

    def divide(self, ls):
        self.result = [i / randint(2, 10) for i in ls]

    def display_result(self):
        print(self.result)


class Facade:
    def __init__(self, logic1, logic2):
        self._logic1 = logic1
        self._logic2 = logic2

    def execute(self):
        self._logic1.get_nums()
        powered = self._logic1.power()
        self._logic2.divide(powered)
        self._logic2.display_result()


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    facade = Facade(Logic1(), Logic2())
    facade.execute()





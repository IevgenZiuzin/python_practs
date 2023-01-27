desc = """
Создайте класс для подсчета площади геометрических 
фигур. Класс должен предоставлять функциональность 
для подсчета площади треугольника по разным формулам, 
площади прямоугольника, площади квадрата, площади 
ромба. Методы класса для подсчета площади должны 
быть реализованы с помощью статических методов. Также 
класс должен считать количество подсчетов площади и 
возвращать это значение с помощью статического метода.
"""


class Area:
    __instances = 0

    def __init__(self):
        self.__class__.__instances += 1

    @staticmethod
    def instances():
        return Area.__instances

    @staticmethod
    def triangle(a, h):
        return 1/2 * a * h

    @staticmethod
    def rectangle(w, h):
        return w * h

    @staticmethod
    def square(a):
        return a ** 2

    @staticmethod
    def diamond(p, q):
        return (p * q) / 2


if __name__ == '__main__':
    print(f'{desc}\n----------\n')

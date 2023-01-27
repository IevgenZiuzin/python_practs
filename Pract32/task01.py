desc = """
Используя понятие множественного наследования, 
разработайте класс «Окружность, вписанная в квадрат».
"""


class Circle:
    def __init__(self, radius=None):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value


class Square:
    def __init__(self, side=None):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value


class CircleInSquare(Circle, Square):
    def __init__(self):
        Circle.__init__(self)
        Square.__init__(self)


def object_info(obj):
    class_name = obj.__class__.__name__
    attributes = [key for key in obj.__dict__.keys()]
    return f'Class name: {class_name}\n' \
           f'Attributes: {attributes}\n\n'


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    circ_in_sq = CircleInSquare()
    print(object_info(circ_in_sq))

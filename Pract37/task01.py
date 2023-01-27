import pickle

desc = """
Создайте класс «Самолет». Наполните его необходимыми
характеристиками и методами.
Реализуйте упаковку и распаковку объектов класса «Самолет»
с использованием модуля pickle.
"""


class Airplane:
    def __init__(self, model=None, airlift=None):
        self._model: str = model
        self._airlift: int = airlift  # in kg

    def __str__(self):
        return str(self.__dict__)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def airlift(self):
        return self._airlift

    @airlift.setter
    def airlift(self, value):
        self._airlift = value

    def to_pickle(self):
        return pickle.dumps(self.__dict__)

    @staticmethod
    def from_pickle(file):
        dc = pickle.loads(file)
        return Airplane(dc['_model'], dc['_airlift'])


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    some_plane = Airplane('Boeing', 80000)
    packed = some_plane.to_pickle()
    unpacked = Airplane().from_pickle(packed)
    print(str(some_plane) == str(unpacked))

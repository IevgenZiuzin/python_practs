import pickle
import json


desc = """
Добавьте к заданию 1 возможность упаковки/распаковки с использованием модуля json.
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

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(file):
        dc = json.loads(file)
        return Airplane(dc['_model'], dc['_airlift'])


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    some_plane = Airplane('Boeing', 80000)
    packed_to_pickle = some_plane.to_pickle()
    unpacked_from_pickle = Airplane().from_pickle(packed_to_pickle)
    packed_to_json= some_plane.to_json()
    unpacked_from_json = Airplane().from_json(packed_to_json)
    print(str(unpacked_from_json) == str(unpacked_from_pickle) == str(some_plane))


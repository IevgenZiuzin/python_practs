import json
import pickle


desc = """
К уже реализованному классу «Часы» добавьте возможность упаковки и распаковки данных
с использованием json и pickle.
"""


class Watch:
    def __init__(self, model=None, price=None):
        self.model: str = model
        self.price: int = price

    def __str__(self):
        return str(self.__dict__)

    def to_pickle(self):
        return pickle.dumps(self.__dict__)

    @staticmethod
    def from_pickle(file):
        dc = pickle.loads(file)
        return Watch(dc['model'], dc['price'])

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(file):
        dc = json.loads(file)
        return Watch(dc['model'], dc['price'])


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    watch = Watch('Orient', 80000)
    packed_to_pickle = watch.to_pickle()
    unpacked_from_pickle = Watch().from_pickle(packed_to_pickle)
    packed_to_json = watch.to_json()
    unpacked_from_json = Watch().from_json(packed_to_json)
    print(str(unpacked_from_json) == str(unpacked_from_pickle) == str(watch))
import json
import pickle


desc = """
К уже реализованному классу «Дробь» добавьте возможность упаковки и распаковки данных
с использованием json и pickle.
"""


class Fraction:
    def __init__(self, dividend=None, divisor=None):
        self.dividend: int = dividend
        self.divisor: int = divisor

    def __str__(self):
        return str(self.__dict__)

    def to_pickle(self):
        return pickle.dumps(self.__dict__)

    @staticmethod
    def from_pickle(file):
        dc = pickle.loads(file)
        return Fraction(dc['dividend'], dc['divisor'])

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(file):
        dc = json.loads(file)
        return Fraction(dc['dividend'], dc['divisor'])


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    frac = Fraction(5, 10)
    packed_to_pickle = frac.to_pickle()
    unpacked_from_pickle = Fraction().from_pickle(packed_to_pickle)
    packed_to_json = frac.to_json()
    unpacked_from_json = Fraction().from_json(packed_to_json)
    print(str(unpacked_from_json) == str(unpacked_from_pickle) == str(frac))

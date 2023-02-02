import pickle
import json

desc = """
Создайте реализацию паттерна Adapter. Протестируйте 
работу созданного класса.
"""


class Car:
    def set_driver(self, name):
        print(f'Is driven by {name}')


class Motorcycle:
    def set_rider(self, name):
        print(f'{name._title()} is riding this bike')


class MotorcycleAdapter:
    def __init__(self, motorcycle):
        self.motorcycle = motorcycle

    def set_driver(self, name):
        self.motorcycle.set_rider(name)


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    car = Car()
    motorcycle = Motorcycle()
    bike = MotorcycleAdapter(motorcycle)
    vehicles = [car, bike]
    names = ['John', 'Jane']
    for vehicle, name in zip(vehicles, names):
        vehicle.set_driver(name)




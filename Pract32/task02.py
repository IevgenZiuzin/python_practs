desc = """
Используя механизм множественного наследования 
разработайте класс “Автомобиль”. Должны быть классы 
«Колеса», «Двигатель», «Двери» и т.д.
"""


class Engine:
    def __init__(self, volume=None):
        self.volume = volume


class Drive:
    def __init__(self, drive=None):
        self.drive = drive


class Body:
    def __init__(self, body_type=None):
        self.type = body_type


class Car(Engine, Drive, Body):
    def __init__(self, engine_volume, drive_type, body_type):
        Engine.__init__(self, engine_volume)
        Drive.__init__(self, drive_type)
        Body.__init__(self, body_type)


def object_info(obj):
    class_name = obj.__class__.__name__
    attributes = [key for key in obj.__dict__.keys()]
    return f'Class name: {class_name}\n' \
           f'Attributes: {attributes}\n\n'


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    car = Car(2.0, 'forward', 'sedan')
    print(object_info(car))
    print(car.__dict__)

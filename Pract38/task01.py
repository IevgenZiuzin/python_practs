import json

desc = """
Создайте классическую реализацию паттерна Singleton. 
Протестируйте работу созданного класса.
"""


class JsonSource(dict):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(JsonSource, cls).__new__(cls)
        return cls.__instance

    def __init__(self, path=None):
        super().__init__()
        self._path = path
        if path is not None:
            self.update(self.__source())

    def __source(self):
        with open(self._path, 'r', encoding='utf-8') as file:
            return json.loads(file.read())

    def save(self):
        with open(self._path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self))


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    loaded1 = JsonSource()
    loaded2 = JsonSource()
    print(id(loaded1) == id(loaded2))



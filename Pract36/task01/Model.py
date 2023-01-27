import json


class Dict(dict):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Dict, cls).__new__(cls)
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

    def find(self, query):
        for key, value in self.items():
            if key == query or value == query:
                return key

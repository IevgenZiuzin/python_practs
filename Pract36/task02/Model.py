import json
from typing import List


class Album:
    def __init__(self, title: str, year: str):
        self.title = title
        self.year = year


class Albums(List[Album]):
    pass


class Artist:
    def __init__(self, title: str, albums: List[Album]):
        self.title = title
        self.albums = albums


class Artists(List[Artist]):
    pass


class DB(list):
    def __init__(self, path):
        super().__init__()
        self._path = path
        self.content = self._init(self._path)
        if self.content:
            self.extend(self.content)

    def _init(self, path):
        try:
            with open(path, 'r') as file:
                return json.loads(file.read())
        except Exception as e:
            print('Data loading failed', e)

    def update(self, body):
        try:
            with open(self._path, 'w') as file:
                return json.dumps(file.write(body))
        except Exception as e:
            print('Data saving failed', e)

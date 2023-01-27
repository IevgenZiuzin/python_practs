import json
from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def add(self, value):
        ...

    @abstractmethod
    def delete(self, value):
        ...

    @abstractmethod
    def find(self, value):
        ...


class ListOfDictsEntity(list, Entity, ABC):
    def add(self, value):
        self.append(value)

    def delete(self, value):
        self.pop(value)

    def find(self, value):
        for i in self:
            for k in i.keys():
                if value == i[k]:
                    return self.index(i)


class DictWithListEntity(dict, Entity, ABC):
    def add(self, value):
        self.update(value)

    def delete(self, value):
        self.pop(value)

    def find(self, value):
        return self.get(value)


class Group(DictWithListEntity, ABC):
    def __init__(self, title=None):
        super().__init__()
        self.title = title


class Albums(ListOfDictsEntity, ABC):
    pass


class Album(DictWithListEntity, ABC):
    def __init__(self, title=None, year=None):
        super().__init__()
        self.tile = title
        self.year = year

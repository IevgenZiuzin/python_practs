from Model import *
from View import *

desc = """
Есть некоторый словарь, который хранит названия 
стран и столиц. Название страны используется в качестве 
ключа, название столицы в качестве значения. Необходимо 
реализовать: добавление данных, удаление данных, поиск 
данных, редактирование данных, сохранение и загрузку 
данных (используя упаковку и распаковку).
"""


class DictController:
    def __init__(self, source=None):
        self._source: Dict = source

    def add(self):
        _country, _capital = get_input('Country'), get_input('Capital')
        if not _country:
            return
        self._source.update({_country: _capital})
        self.save()

    def find(self):
        query = get_input('Country or capital')
        if query:
            key = self._source.find(query)
            display({key: self._source[key]})
            return key

    def delete(self):
        _country = get_input('Country')
        if self._source.get(_country):
            del self._source[_country]
            self.save()

    def edit(self):
        key = self.find()
        if key is not None:
            self._source.pop(key)
            self.add()
            self.save()

    def display(self):
        display(self._source)

    def save(self):
        self._source.save()


def run(query, commands):
    for index, command in enumerate(commands, 1):
        if query == str(index):
            try:
                command()
            except TypeError:
                print(f"{command} failed.")
                return


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    c = DictController(Dict('capitals.json'))
    titles = ['Add', 'Remove', 'Find', 'Edit', 'Display']
    operations = [c.add, c.delete, c.find, c.edit, c.display]
    while True:
        run(display_menu(titles), operations)


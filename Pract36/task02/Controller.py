from Model import *
from View import *

desc = """
Есть некоторый словарь, который хранит названия 
музыкальных групп(исполнителей) и альбомов.
Название группы используется в качестве ключа,
названия альбомов в качестве значения. 
Необходимо реализовать: 
добавление данных, удаление данных, поиск данных, 
редактирование данных, сохранение и загрузку данных 
(используя упаковку и распаковку).
"""


def bind(fn, *args, **kwargs):
    def inner(*a, **kw):
        return fn(*args, *a, **kwargs, **kw)
    return inner


def run(query, commands):
    for index, command in enumerate(commands, 1):
        if query == str(index):
            try:
                command()
            except TypeError:
                print(f"{command} failed.")
                return


def main():
    pass


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    main()

import json
from abc import ABC, abstractmethod

desc = """
Создайте класс, выполняющий операции с массивом: 
отображение данных в файл или на экран, переворот 
данных, нахождение максимума, нахождение минимума. 
Класс может получить набор значений с клавиатуры или 
из файла. При реализации используйте паттерн Strategy 
и другие необходимые паттерны.
"""


class UpdateStrategy(ABC):
    @abstractmethod
    def load(self):
        ...


class LoadFromFile(UpdateStrategy):
    def load(self):
        list_path = input('Path: ')
        with open(list_path, 'r') as file:
            return json.loads(file.read())


class CreateFromInput(UpdateStrategy):
    def load(self):
        inputs = []
        while True:
            query = input('Number: ')
            if query.isdigit():
                inputs.append(int(query))
            else:
                break
        return inputs


class LogStrategy(ABC):
    @abstractmethod
    def log(self, value):
        ...


class LogConsole(LogStrategy):
    def log(self, value):
        print(value)


class LogFile(LogStrategy):
    log_path = 'log.json'

    def log(self, value):
        with open(self.__class__.log_path, 'w') as file:
            file.write(json.dumps(value))


class UserList(list):
    def update(self, strategy: UpdateStrategy):
        ls = strategy.load()
        self.extend(ls)

    def log(self, strategy: LogStrategy):
        strategy.log(self)

    def reversed(self):
        ls = self.copy()
        ls.reverse()
        return ls


def set_log_path():
    LogFile.log_path = input('First set file log path (.json): ')


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    set_log_path()
    a = UserList()
    a.update(CreateFromInput())
    a.log(LogFile())
    print(min(a))
    print(max(a))
    print(a.reversed())

from abc import ABC, abstractmethod
from datetime import datetime


desc = """
Пользователь вводит с клавиатуры набор чисел и путь 
к файлу для сохранения полученных данных. Необходимо:
■ Сохранить все полученные числа.
■ Найти максимум, минимум. Эти значения сохранить в том же файле.
■ Отобразить числа.
■ Отобразить максимум и минимум.
■ Создать класс для логгирования операций.
При создании объекта класса нужно уточнить куда производится 
логгирование: экран или файл. В программе можно 
создать только один объект класса. Все действия 
в программе необходимо логгировать с помощью 
объекта этого класса.
"""


class ICommand(ABC):
    @abstractmethod
    def execute(self):
        ...


class UserData:
    def __init__(self, numbers=None, path=None):
        self.numbers = numbers
        self.path = path


class GetMax(ICommand, UserData):
    def __str__(self):
        return 'getting max: '

    def execute(self):
        return max(self.numbers)


class GetMin(ICommand, UserData):
    def __str__(self):
        return 'getting min: '

    def execute(self):
        return min(self.numbers)


class SaveNumbers(ICommand, UserData):
    def __str__(self):
        return f'saving numbers {self.numbers} to path {self.path}'

    def execute(self):
        with open(self.path, 'a') as file:
            file.write(str(self.numbers))


class SaveMax(ICommand, UserData):
    def __str__(self):
        return f'saving max'

    def execute(self):
        with open(self.path, 'a') as file:
            file.write(str(max(self.numbers)))


class SaveMin(ICommand, UserData):
    def __str__(self):
        return f'saving min'

    def execute(self):
        with open(self.path, 'a') as file:
            file.write(str(min(self.numbers)))


class DisplayNumbers(ICommand, UserData):
    def __str__(self):
        return f'printing numbers: {self.numbers}'

    def execute(self):
        print(self.numbers)


class DisplayMax(ICommand, UserData):
    def __str__(self):
        return f'Printing max: {max(self.numbers)}'

    def execute(self):
        print(max(self.numbers))


class DisplayMin(ICommand, UserData):
    def __str__(self):
        return f'Printing min: {min(self.numbers)}'

    def execute(self):
        print(min(self.numbers))


class Invoker:
    def __init__(self, numbers, path, log_path=None, console_log=False):
        self.numbers = numbers
        self.path = path
        self.log_path = log_path
        self._console_log = console_log

    def file_log(self, body):
        with open(self.log_path, 'a') as file:
            file.write(f'{datetime.now().strftime("%Y %m %d %H %M : %S %f")} - {body}\n')

    @staticmethod
    def console_log(body):
        print(f'{datetime.now().strftime("%Y %m %d %H %M : %S %f")} - {body}')

    def run(self) -> None:

        steps = [DisplayNumbers,
                 SaveNumbers,
                 GetMax,
                 DisplayMax,
                 SaveMax,
                 GetMin,
                 DisplayMin,
                 SaveMin]
        for step in steps:
            command = step(self.numbers, self.path)
            command.execute()
            if self.log_path:
                self.file_log(command)
            if self._console_log:
                self.console_log(command)


def user_numbers():
    numbers = []
    while True:
        query = input(f'Number: ')
        if query.isdigit():
            numbers.append(int(query))
        else:
            break
    return numbers


def user_path():
    while True:
        path = input(f'Path: ')
        if path is None:
            print('path is required')
        else:
            return path


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    invoker = Invoker(user_numbers(), user_path(), 'log.txt', console_log=True)
    invoker.run()


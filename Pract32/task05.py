desc = """
Для классов из задания 4 реализуйте магический 
метод str, а также метод int (должен возвращать возраст служащего).
"""


class Employer:
    def __init__(self, name=None, age=None):
        self._name = name
        self._age = age

    def __str__(self):
        return str(self._name)

    def __int__(self):
        return int(self._age)

    def Print(self):
        print(f'This is a {self.__class__.__name__}.\n')


class President(Employer):
    pass


class Manager(Employer):
    pass


class Worker(Employer):
    pass


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    employees = [President('Joe', 80), Manager('Pete', 50), Worker('James', 40)]
    for employee in employees:
        print(f'{employee} is {int(employee)}.')
        employee.Print()

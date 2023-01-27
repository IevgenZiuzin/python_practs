desc = """
Создать базовый класс Employer (служащий) с функцией Print().
Она должна выводить информацию о служащем. В случае базового класса
это может быть строка с надписью This is Employer class.
Создайте от него три производных класса: President, 
Manager, Worker. Переопределите функцию Print() для 
вывода информации, соответствующей каждому типу 
служащего.
"""


class Employer:
    def Print(self):
        print(f'This is a {self.__class__.__name__}.')


class President(Employer):
    pass


class Manager(Employer):
    pass


class Worker(Employer):
    pass


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    employees = [President(), Manager(), Worker()]
    for employee in employees:
        employee.Print()

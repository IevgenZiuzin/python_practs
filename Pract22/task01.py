import menu

desc = """
Есть множество, содержащее название стран. Необходимо предоставить пользователю возможности:
■ Добавление стран;
■ Удаления стран;
■ Поиска стран по введенным символам;
■ Проверки существует ли страна внутри множества.
"""

biggest_economies = {'USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Brazil', 'Italy', 'Canada'}


class StringSet:
    def __init__(self, strset: set):
        self.strset = strset

    def __str__(self):
        return str(self.strset)

    @staticmethod
    def get_input():
        return input('Input: ').title()

    def add(self):
        self.strset.add(self.get_input())
        print(self)

    def remove(self):
        self.strset.remove(self.get_input())
        print(self)

    def search(self):
        key = self.get_input()
        for i in self.strset:
            if i.startswith(key):
                print(i)
                return i

    def is_present(self):
        key = self.get_input()
        print(key in self.strset)
        return key in self.strset

    def edit(self):
        m = menu.init(['Add', 'Remove', 'Search', 'Is present'],
                      [self.add, self.remove, self.search, self.is_present])
        m.run()


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    countries = StringSet(biggest_economies)
    print(f'Set: {countries.strset}')
    countries.edit()

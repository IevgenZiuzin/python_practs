import menu

desc = """
В словаре хранится набор пар: Название страны -> Столица.
Нужно реализовать функциональность по добавлению, удалению, поиску и замене.
"""


class StringDict(dict):
    def __init__(self, strdict):
        super().__init__()
        self.update(strdict)
        self.key = list(self.keys())[0]

    @staticmethod
    def get_input():
        return input(f'input: ').title()

    def display(self):
        for i in self:
            print(f'{i}:')
            for d in self[i]:
                for k, v in d.items():
                    print(f'\t{k}: {v}')

    def add(self):
        print('Country', end=' ')
        country = self.get_input()
        print('Capital', end=' ')
        capital = self.get_input()
        self[self.key].append({country: capital})

    def remove(self):
        print('Country or capital', end=' ')
        key = self.get_input()
        for index, d in enumerate(self[self.key]):
            for k, v in d.items():
                if k == key or v == key:
                    self[self.key].pop(index)

    def search(self):
        print('Country or capital', end=' ')
        key = self.get_input()
        for i in self[self.key]:
            for k, v in i.items():
                if k == key or v == key:
                    print(i)

    def replace(self):
        print('Country', end=' ')
        country = self.get_input()
        print('Capital', end=' ')
        capital = self.get_input()
        for i in self[self.key]:
            for k, v in i.items():
                if k == country:
                    i[k] = capital

    def edit(self):
        m = menu.init(['Display', 'Add', 'Remove', 'Search', 'Replace'],
                      [self.display, self.add, self.remove, self.search, self.replace])
        m.run()


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    collection = StringDict({
        'Latin America': [
            {'Argentina': 'Buenos Aires'},
            {'Chile': 'Santiago'},
            {'Colombia': 'Bogota'},
            {'Ecuador': 'Quito'},
            {'Paraguay': 'Asuncion'}
        ]
    })
    collection.edit()

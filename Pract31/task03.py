desc = """
Создайте класс Библиотека. Класс предназначен для 
хранения информации о библиотеке (название, адрес, количество книг и т.д.). 
Реализуйте необходимые для класса методы.
Используя перегрузку операторов реализуйте для 
него следующие арифметические операции:
■ + добавляет к количеству книг указанное значение;
■ - вычитает из количества книг указанное значение;
■ += добавляет к количеству книг указанное значение;
■ -= вычитает из количества книг указанное значение;
Используя перегрузку операторов реализуйте (сравнение по количеству книг):
■ <;
■ >;
■ <=;
■ >=;
■ ==;
■ !=.
"""


class Library:
    def __init__(self, name=None, address=None, books_amount=None):
        self._name = name
        self._address = address
        self._books_amount = books_amount

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def books_amount(self):
        return self._books_amount

    @books_amount.setter
    def books_amount(self, value):
        self._books_amount = value

    def __add__(self, other):
        return self._books_amount + other.books_amount

    def __sub__(self, other):
        return self._books_amount - other.books_amount

    def __iadd__(self, other):
        self._books_amount += other.books_amount
        return self._books_amount

    def __isub__(self, other):
        self._books_amount -= other.books_amount
        return self._books_amount

    def __lt__(self, other):
        return self._books_amount < other.books_amount

    def __gt__(self, other):
        return self._books_amount > other.books_amount

    def __le__(self, other):
        return self._books_amount <= other.books_amount

    def __ge__(self, other):
        return self._books_amount >= other.books_amount

    def __eq__(self, other):
        return self._books_amount == other.books_amount

    def __ne__(self, other):
        return self._books_amount != other.books_amount


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    print(f'Test adding instances: {Library(books_amount=10) + Library(books_amount=20)}')

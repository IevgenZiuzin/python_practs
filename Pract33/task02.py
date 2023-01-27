from datetime import datetime


desc = """
Добавьте ещё одну функцию для декорирования вывода 
данных. Эта функция должна добавить новые элементы 
в форматирование вывода.
"""


def dollars(f):
    def wrapper():
        print('$' * 10)
        f()
        print('$' * 10)
    return wrapper


def stars(f):
    def wrapper():
        print('*' * 10)
        f()
        print('*' * 10)
    return wrapper


@dollars
@stars
def display_time():
    print(datetime.now().strftime('%H:%M'))


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    display_time()
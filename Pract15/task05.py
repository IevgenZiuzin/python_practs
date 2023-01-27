desc = """
Напишите функцию, которая возвращает сумму чисел 
в указанном диапазоне. Границы диапазона передаются 
в качестве параметров."""


def sum_in_range(start, end):
    first = min(start, end)
    last = max(start, end)
    return sum([i for i in range(first, last)])


if __name__ == '__main__':
    print(f'{desc}\n----------')
    a, b = 0, 10
    print(f'Args: {a, b}\n'
          f'Sum in range: {sum_in_range(a, b)}')


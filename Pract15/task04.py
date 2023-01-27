desc = """
Напишите функцию, которая возвращает максимальное из четырёх чисел.
Числа передаются в качестве  параметров."""


def get_max(a, b, c, d):
    return max(a, b, c, d)


if __name__ == '__main__':
    print(f'{desc}\n----------')
    a, b, c, d = 1, 2, 3, 4
    print(f'Args: {a, b, c, d}\n'
          f'Max: {get_max(a, b, c, d)}')


desc = """
Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает пользователь.
Проиллюстрируйте работу функции примером."""


def display_stars(n):
    star = "*"
    if n == 0:
        return
    print(star, end='')
    display_stars(n - 1)


if __name__ == '__main__':
    display_stars(5)


desc = """
Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b.
Пользователь вводит a и b. Проиллюстрируйте работу функции примером."""


def recurs_sum(first, last):
    if first == last:
        return last
    return first + recurs_sum(first + 1, last)


if __name__ == '__main__':
    print(recurs_sum(1, 4))




desc = """
Написать рекурсивную функцию нахождения степени числа."""


def power(base, exp):
    if exp == 1:
        return base
    return base * power(base, exp - 1)


if __name__ == '__main__':
    pass


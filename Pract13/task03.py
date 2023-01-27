print("""Пользователь с клавиатуры вводит элементы списка целых.
Необходимо посчитать сумму всех элементов и их среднеарифметическое.
Результаты вывести на экран.""")


def collect_integers():
    integers = []
    print(f'\nnot integer for stop adding')
    while True:
        integer = input("Add: ")
        try:
            integers.append(int(integer))
        except ValueError:
            break
    return integers


def get_sum(integers):
    return sum(integers)


def get_average(integers):
    if integers:
        return sum(integers)/len(integers)
    else:
        return 0


def main():
    integers = collect_integers()
    print(f'Your integers: {integers}')
    print(f'Sum: {get_sum(integers)}')
    print(f'Average: {get_average(integers)}')


if __name__ == '__main__':
    main()

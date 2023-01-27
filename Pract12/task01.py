# Задание 1
# Пользователь вводит с клавиатуры строку. Произведите поворот строк и полученный результат выведите
# на экран.


def reverse_line(line):
    return ''.join(reversed([i for i in line]))


def main():
    line = input('Type something to reverse: ')
    print(reverse_line(line))


if __name__ == '__main__':
    main()



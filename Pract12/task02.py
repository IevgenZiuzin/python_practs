# Задание 2
# Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба
# количества на экран.

def count_letters(line):
    return len([i for i in line if i.isalpha()])


def count_digits(line):
    return len([i for i in line if i.isdigit()])


def main():
    line = input('type string to count letters and digits: ')
    print(f'letters: {count_letters(line)}\n'
          f'digits: {count_digits(line)}')


if __name__ == '__main__':
    main()

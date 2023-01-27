# Задание 4
# Пользователь вводит с клавиатуры строку и слово
# для поиска. Посчитайте сколько раз в строке встречается
# искомое слово. Полученное число выведите на экран.

import re


def count_words(line, word):
    return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), line))


def main():
    line = input('Line: ')
    word = input('Word: ')
    print(f'occurrences: {count_words(line, word)}')


if __name__ == '__main__':
    main()

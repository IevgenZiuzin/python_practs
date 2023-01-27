# Задание 5
# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите
# на экране.


def main():
    line = input('Line: ')
    to_replace = input('Word to replace: ')
    replacer = input('Replace word: ')
    print(line.replace(to_replace, replacer))


if __name__ == '__main__':
    main()

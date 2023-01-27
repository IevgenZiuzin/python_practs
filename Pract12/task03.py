# Задание 3
# Пользователь вводит с клавиатуры строку и символ
# для поиска. Посчитайте сколько раз в строке встречается
# искомый символ. Полученное число выведите на экран.

def main():
    line = input(f'type something: ')
    symbol = input(f'type symbol to count its occurrences in line\n(line)\n: ')
    print(f'occurrences: {line.count(symbol)}')


if __name__ == '__main__':
    main()

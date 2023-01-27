import re

desc = """
Дан текстовый файл. Подсчитать количество слов, 
начинающихся с символа, который задаёт пользователь.
"""


def file_read(path):
    with open(path, 'r') as file:
        return file.read()


def get_input():
    return input('Your symbol: ')


def count_words(text, symbol):
    amount = 0
    words = re.findall(r'[\w]+', text)
    for i in words:
        if i.startswith(symbol):
            amount += 1
    return amount


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    content = file_read('text.txt')
    print(f'\nContent:\n\n{content}\n')
    print(f'Amount: {count_words(content, get_input())}')

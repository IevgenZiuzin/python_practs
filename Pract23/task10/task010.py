from pathlib import Path
desc = """
Дан текстовый файл. Подсчитать количество строк в нём.
"""


def file_read(path):
    with open(path, 'r') as file:
        return file.read()


def count_lines(text):
    return len(text.split('\n'))


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    print(f'Lines: {count_lines(file_read("text.txt"))}')

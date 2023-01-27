desc = """
Дан текстовый файл. Подсчитать количество символов в нём.
"""


def file_read(path):
    with open(path, 'r') as file:
        return file.read()


def count_chars(text):
    return len(text)


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    print(f'Characters: {count_chars(file_read("text.txt"))}')

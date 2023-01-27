desc = """
Дан текстовый файл. Необходимо переписать его 
строки в другой файл. Порядок строк во втором файле 
должен быть обратным по отношению к порядку строк 
в заданном файле.
"""


def file_read(path):
    with open(path, 'r') as file:
        return file.read()


def file_write(path, body):
    with open(path, 'w') as file:
        file.write(body)


def reverse_lines(text):
    return '\n'.join(text.split('\n')[::-1])


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    file_write('reversed.txt', reverse_lines(file_read('text.txt')))

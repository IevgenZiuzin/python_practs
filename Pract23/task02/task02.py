desc = """
Дан текстовый файл. Необходимо переписать его 
строки в другой файл. Порядок строк во втором файле 
должен совпадать с порядком строк в заданном файле.
"""


def file_read(path):
    with open(path, 'r') as file:
        return file.read()


def file_write(path, body):
    with open(path, 'w') as file:
        file.write(body)


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    file_write('copy.txt', file_read('text.txt'))

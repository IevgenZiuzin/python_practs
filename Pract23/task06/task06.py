desc = """
Дан текстовый файл. Переписать в другой файл все его 
строки с заменой в них символа * на символ & и наоборот
"""


def file_read(path):
    with open(path, 'r') as file:
        return file.read()


def file_write(path, body):
    with open(path, 'w') as file:
        file.write(body)


def toggle(content, symb1, symb2):
    content = [s for s in content]
    for i, s in enumerate(content):
        if s == symb1:
            content[i] = symb2
        if s == symb2:
            content[i] = symb1
    return ''.join(content)


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    file_write('toggled.txt', toggle(file_read('text.txt'), '*', '&'))


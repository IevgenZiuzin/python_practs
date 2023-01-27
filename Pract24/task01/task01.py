desc = """
Дан текстовый файл. Необходимо создать новый файл 
убрав из него все неприемлемые слова. Список неприемлемых слов находится в другом файле.
"""


def file_read(path):
    with open(path, 'r') as file:
        return file.read()


def file_write(path, body):
    with open(path, 'w') as file:
        file.write(body)


def banned_list(path):
    return file_read(path).split(', ')


def delete_banned(text, banned: list):
    for i in banned:
        text = text.replace(i, '')
    return text


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    source = file_read('text.txt')
    ban = file_read('ban.txt')
    print(f'\n\nSource:\n\n{source}\n\n')
    print(f'\n\nBan:\n\n{ban}\n\n')
    result = delete_banned(source, banned_list('ban.txt'))
    file_write('result.txt', result)
    print(f'In new file:\n\n{file_read("result.txt")}')




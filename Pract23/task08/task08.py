desc = """
Дан массив строк. Записать их в файл, расположив 
каждый элемент массива на отдельной строке с сохранением порядка.
"""


def file_write(path, body):
    with open(path, 'w') as file:
        file.write(body)


def list_to_strings(lst: list):
    return '\n'.join(lst)


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    lines = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor',
             'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,',
             'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.']
    file_write('lat.txt', list_to_strings(lines))
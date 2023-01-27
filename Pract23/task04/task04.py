desc = """
Дан текстовый файл. Добавить в него строку из двенадцати звездочек (************), поместив ее после последней 
из строк, в которых нет запятой. Если таких строк нет, 
то новая строка должна быть добавлена после всех строк 
имеющегося файла. Результат записать в другой файл.
"""


def file_read(path):
    with open(path, 'r') as file:
        return file.read()


def file_write(path, body):
    with open(path, 'w') as file:
        file.write(body)


def get_lines(text):
    return text.split('\n')


def last_without(lines: list, value: str):
    for line in lines[::-1]:
        if line.count(value) == 0:
            return lines.index(line)
    return len(lines) - 1


def insert_after(lines, idx, value):
    lines.insert(idx + 1, value)
    return '\n'.join(lines)


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    stars = '************'
    content = file_read('text.txt')
    print(f'\nContent:\n\n{content}\n')
    strings = get_lines(content)
    file_write('inserted.txt', insert_after(strings, last_without(strings, ','), stars))
    print(f'\nInserted:\n\n{file_read("inserted.txt")}\n')

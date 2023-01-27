import re

desc = """
Дан текстовый файл. Необходимо создать новый файл, 
в который требуется переписать из исходного файла все 
слова, состоящие не менее чем из семи букв.
"""


def file_read(path):
    with open(path, 'r') as file:
        return file.read()


def file_write(path, body):
    with open(path, 'w') as file:
        file.write(body)


def filter_by_length(text, length):
    words = re.findall(r'[\w]+', text)
    return list(filter(lambda word: len(word) >= length, words))


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    content = file_read('text.txt')
    print(f'Content:\n\n{content}\n')
    filtered = ' '.join(filter_by_length(content, 7))
    print(f'Filtered:\n\n{filtered}\n')
    file_write('filtered.txt', filtered)

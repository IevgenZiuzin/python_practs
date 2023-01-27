import os
import random
import string

desc = """
Пользователь с клавиатуры вводит названия файлов, 
до тех пор, пока он не введет слово quit. После завершения 
ввода программа должна объединить содержимое всех 
перечисленных пользователем файлов в один.
"""


def file_read(path):
    with open(path, encoding='utf-8', mode='r') as file:
        return file.read()


def file_write(path, body):
    with open(path, encoding='utf-8', mode='w') as file:
        file.write(body)


def some_string():
    return ', '.join([str(random.randint(1, 6)) for i in range(4)])


def generate_files(n):
    letters = string.ascii_lowercase
    for i in range(n):
        if n <= len(letters):
            file_write(f'{letters[i]}.txt', some_string())


def txt_in_dir(path_list):
    content = []
    for i in path_list:
        content.append(file_read(i))
    return '\n'.join(content)


def users_paths():
    path_list = []
    while True:
        filename = (input('File name: '))
        if filename == 'quit' or filename == '':
            break
        path_list.append(f'{filename}.txt')
    return path_list


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    generate_files(4)
    file_write('joined.txt', txt_in_dir(users_paths()))
    print(file_read('joined.txt'))



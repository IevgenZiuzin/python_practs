desc = """
Написать программу транслитерации с русского на 
английский и наоборот. Данные для транслитерации 
берутся из файла и записываются в другой файл. Направление перевода определяется через меню пользователя.
"""


symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")


def file_read(path):
    with open(path, encoding='utf-8', mode='r') as file:
        return file.read()


def file_write(path, body):
    with open(path, encoding='utf-8', mode='w') as file:
        file.write(body)


def cyrillic_latin():
    return {ord(a): ord(b) for a, b in zip(*symbols)}


def latin_cyrillic():
    return {ord(b): ord(a) for a, b in zip(*symbols)}


def translate_file(path, key):
    return file_read(path).translate(key)


def main():
    q = input('1. Cyrillic-Latin 2. Latin-Cyrillic\n: ')
    if q.isdigit():
        if q == '1':
            file_write('translated.txt', translate_file('cyr.txt', cyrillic_latin()))
        elif q == '2':
            file_write('translated.txt', translate_file('lat.txt', latin_cyrillic()))
        print(f'\nTranslated file:\n\n{file_read("translated.txt")}')
    else:
        return


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    main()



import sys


def get_input(desc=None):
    string = input(f'{desc}: ')
    return string if string != '' else False


def display_dict(d):
    for key, value in d.items():
        print(f'{key} - {value}')


def display_list(l):
    for i in l:
        print(f'{i}')


def display_menu(titles):
    quit_num = 0
    for number, title in enumerate(titles, 1):
        print(f"{number}.{title}", end="  ")
        quit_num = number + 1
    print(f"{quit_num}.Quit")

    query = input("\n: ")

    if not query.isdigit():
        return
    if int(query) == quit_num:
        sys.exit()
    return query

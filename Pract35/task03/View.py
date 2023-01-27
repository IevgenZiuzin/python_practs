import sys


def display_users(users_list):
    for index, user in enumerate(users_list, 1):
        print(f'{index}.\n'
              f'login: {user.login}\n'
              f'password: {user.password}\n')


def login():
    _login = input('Login: ')
    return _login if _login != '' else False


def password():
    _password = input('Password: ')
    return _password if _password != '' else False


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

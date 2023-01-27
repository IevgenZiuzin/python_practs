from Model import *
from View import *

desc = """
Необходимо разработать приложение, которое позволит сохранять
информацию о логинах пользователей и их паролях.
Каждому пользователю соответствует пара логин — пароль.
При старте приложение отображается меню:
■ Добавить нового пользователя
■ Удалить существующего пользователя
■ Проверить существует ли пользователь
■ Изменить логин существующего пользователя
■ Изменить пароль существующего пользователя
Для реализации задания обязательно используйте 
одну из структур данных. При выборе руководствуйтесь постановкой задачи. 
"""


def add_user():
    global users

    _login, _password = login(), password()
    if not _login:
        return
    user = User()
    user.login,  user.password = _login, _password
    users.append(user)


def remove_user():
    global users
    users.remove(login())


def find_user():
    global users
    user = users.find(login())
    print(user)
    display_users([user])
    return user


def edit_user():
    global users
    user = find_user()
    if user is not None:
        _login, _password = login(), password()
        if not _login:
            return
        user.login, user.password = _login, _password


def display():
    global users
    display_users(users.as_list())


def run(query, commands):
    for index, command in enumerate(commands, 1):
        if query == str(index):
            try:
                command()
            except TypeError:
                print(f"{command} failed.")
                return


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    users = Users()
    titles = ['Add', 'Remove', 'Find', 'Edit', 'Display']
    operations = [add_user, remove_user, find_user, edit_user, display]
    while True:
        run(display_menu(titles), operations)

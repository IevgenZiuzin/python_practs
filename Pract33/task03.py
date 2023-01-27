from datetime import datetime


desc = """
Решите задачу из первого задания с использованием 
синтаксиса декораторов.
Практическое задание

"""


def stars(f):
    def wrapper():
        print('*' * 10)
        f()
        print('*' * 10)
    return wrapper


@stars
def display_time():
    print(datetime.now().strftime('%H:%M'))


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    display_time()

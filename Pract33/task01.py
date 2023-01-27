from datetime import datetime


desc = """
Создайте функцию для отображения текущего времени. 
Функция не принимает параметров. Функция не используя синтаксис декораторов, произведите декорирование 
функции с помощью другой функции. Потенциальный вывод данных на экран:
***************************
23:00
***************************
В этом выводе на экран две линии из звездочек – результаты декорирования.
"""


def stars(f):
    def wrapper():
        print('*' * 10)
        f()
        print('*' * 10)
    return wrapper


def display_time():
    print(datetime.now().strftime('%H:%M'))


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    decorated_time = stars(display_time)
    decorated_time()





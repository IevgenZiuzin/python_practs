import datetime

desc = """
Создайте класс Date, который будет содержать информацию о дате (день, месяц, год).
С помощью механизма перегрузки операторов, определите операцию разности 
двух дат (результат в виде количества дней между датами),
а также операцию увеличения даты на определенное количество дней.
"""


class Date(datetime.datetime):
    pass


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    print(f'Test timedelta: {Date.now() - Date(2019, 10, 29)}\n\n'
          f'Test increase date: {Date.now() + datetime.timedelta(days=3)}\n\n')


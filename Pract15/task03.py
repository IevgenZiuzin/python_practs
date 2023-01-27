desc = """
Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа. 
Функция принимает в качестве параметра: длину линии, направление, символ."""


def display_line(symbol, length, direction=True):
    end = ''
    if direction:
        end = '\n'
    for i in range(length):
        print(symbol, end=end)


if __name__ == '__main__':
    print(f'{desc}\n----------')
    display_line('-', 5)
    display_line('-', 5, direction=False)

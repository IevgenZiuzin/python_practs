# Пользователь вводит с клавиатуры длину и ширину прямоугольника.
# Требуется отобразить на экран незаполненный прямоугольник
# (отображаются только границы прямоугольника).
# Размер длины и ширины равен введенным данным.

height = int(input("Type side height: "))
width = int(input("Type side width: "))
hor = "-"
vert = "|"
space = " "
for i in range(height):
    for k in range(width):
        if i == 0 or i == (height - 1):
            print(hor, end="")
        elif k == 0 or k == (width - 1):
            print(vert, end="")
        else:
            print(space, end="")
    print("")
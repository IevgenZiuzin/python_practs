# Пользователь вводит с клавиатуры размер стороны квадрата.
# Требуется отобразить на экран незаполненный квадрат
# (отображаются только границы квадрата).
# Размер стороны равен введенному размеру.

side = int(input("Type side length: "))
hor = "-"
vert = "|"
space = " "
for i in range(side):
    for k in range(side):
        if i == 0 or i == (side - 1):
            print(hor, end="")
        elif k == 0 or k == (side - 1):
            print(vert, end="")
        else:
            print(space, end="")
    print("")
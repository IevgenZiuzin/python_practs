# Пользователь вводит с клавиатуры ширину и высоту прямоугольника.
# Требуется отобразить на экран заполненный прямоугольник с указанными высотой и шириной.
# Например, если пользователь ввел высоту 3, а ширину 5,
# на экране будет выведено:
# *****
# *****
# *****

height = int(input("Type height: "))
width = int(input("Type width: "))
sign = "*"
for i in range(height):
    print(sign * width)
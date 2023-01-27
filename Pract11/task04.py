# Вывести на экран ромб из звездочек
width = 18
half_width = int(width / 2)

sign = " * "
space = "---"

for i in range(half_width):
    increment = sign * i * 2
    decrement = space * (half_width - i)
    print(decrement, increment, decrement)
for i in range(1, (half_width + 1)):
    increment = space * i
    decrement = sign * (width - 2 * i)
    print(increment, decrement, increment)





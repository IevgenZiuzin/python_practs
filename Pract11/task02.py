# Написать программу, которая выводит на экран шахматную доску с заданным размером клеточки.

board_side = 8
black = "***"
white = "---"

while True:
    user_input = input("Type field size (space for exit): ")
    if not user_input.isdecimal():
        break
    field_side = int(user_input)

    for i in range(board_side):
        for k in range(field_side):
            for l in range(board_side):
                for m in range(field_side):
                    if l % 2 == i % 2:
                        print(white, end="")
                    else:
                        print(black, end="")
            print("")

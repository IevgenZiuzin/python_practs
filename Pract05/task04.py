# Пользователь вводит с клавиатуры размер файла в гигабайтах и скорость интернет-соединения в битах в секунду.
# В зависимости от выбора пользователя посчитать, за сколько часов или минут, или секунд скачается файл.
import sys

while True:
    try:
        size = float(input("Enter file.py size in Gb: "))
        speed = float(input("Enter connection speed in bit/s: "))
        seconds = (size * 8589934592) / speed
        print(seconds)
        query = input("1 - hours\n2 - minutes\n3 - seconds\n4 - quit\n: ")

        if query == "1":
            print("time: %0.f hours" % (seconds // 3600))
        elif query == "2":
            print("time: %0.f minutes" % (seconds // 60))
        elif query == "3":
            print("time: %0.f seconds" % seconds)
        elif query == "4":
            break
    except:
        print("wrong value")
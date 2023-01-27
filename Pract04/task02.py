# Пользователь вводит с клавиатуры число. Необходимо проверить его на кратность 7. Если число кратно
# требуется вывести на экран число и надпись Number is
# multiple 7. Если число не кратно выведите на экран число
# и надпись Number is not multiple 7

try:
    number = int(input("Type number: "))
    if number % 7 != 0:
        print(number, "Number is not multiple 7")
    else:
        if number == 0:
            print(number, "Number is Null")
        else:
            print(number, "Number is multiple 7")
except:
    print("Wrong value")
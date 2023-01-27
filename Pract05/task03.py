# Пользователь вводит с клавиатуры стоимость
# одной игровой приставки, их количество и процент скидки.
# В зависимости от выбора пользователя
# посчитать общую сумму заказа или стоимость одной приставки с учетом скидки.

try:
    price = float(input("Enter console price: "))
    amount = int(input("Enter amount: "))
    rebate = float(input("Enter rebate percent: "))
    rebate /= 100
    query = input("1 - piece price\n2 - total\n3 - quit\n: ")
    if query == "1":
        print("piece price: $%.2f" % (price - (price * rebate)))
    elif query == "2":
        print("total: $%.2f" % ((price - (price * rebate)) * amount))
    elif query == "3":
        pass
except:
    print("wrong value")

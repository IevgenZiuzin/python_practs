# Выведите на экран надпись " Anyone who stops learning is old, whether at twenty or eighty" Henry Ford
# на разных строках. Пример вывода:
# “Anyone who
#   stops
#       learning is old,
#           whether at twenty or eighty”.
#                                     Henry Ford

tab = "\t"
print(f'"Anyone who\n{tab}stops\n{tab*2}learning is old,\n{tab*3}whether at twenty or eighty".\
        \n{tab*9}Henry ford')
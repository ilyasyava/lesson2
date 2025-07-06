# '''
# *
# Написать рекурсивную функцию, которая принимает список
# и печатает каждых элемент на новой строке.
# Если элемент списка - список, то его элементы должны выводиться
# с отступом относительно родительского на 2 символа.
# Символ для отступа передать дополнительными необязательным параметром.
#
# ** написать такую же функцию но без рекурсии
#
# Пример1: some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
# 1
# 2
# 3
# --4
# ----5
# ----6
# --7
# 8
# 9
#
# Пример2: some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
# 1
# --2
# ------3
# ----4
# 5
# ------6
# ------7
# 8
# --------9
# --------10
# ----11
# 12
#
# '''
some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]

def list_recursive(some_list, space=0, symbol="-" ):
    for i in some_list:
        if isinstance(i, list):
            list_recursive(i, space + 2, symbol)
        else:
            print(f"{symbol * space} {i}")

def list_rec_1(some_list, space=0, symbol="-"):
    my_list = [(i, space) for i in reversed(some_list)]

    while my_list:
        i, lev = my_list.pop()
        if isinstance(i, list):
            my_list.extend((sub_i, lev + 2) for sub_i in reversed(i))
        else:
            print(f"{symbol * lev} {i}")

print("Рекурсия: \n")
list_recursive(some_list)

print("\nНе рекурсия: \n")
list_rec_1(some_list)

'''
Лучше всего запускать в консоли виндовс
она имеет 30 строк - как раз один кадр

Данный пример генерирует каждый кадр случайный набор снежинок.

Переделать программу так чтобы каждый кадр каждая существующая 
снежинка опускалась вниз, а сверху генерировались новые.

Дополнительные варианты:
    - снежинки могут быть разные (* . +)
    - крупные снежинки падают быстрей
    - иногда меняется ветер и снежинки летят или прямо или в любую сторону
    - снежинки при генерации не должны быть рядом 

'''



from random import Random
from rich.console import Console

random = Random()
console = Console()

# while True:
#     try:
#         rows = int(input("Введите высоту елочки от 3 до 20: "))
#     except ValueError:
#         print("Введите число")
#         continue

#     if rows < 3 or rows > 20:
#         print("Неверное значение")
#     else:
#         break

def c_tree(rows):
    # Рисуем елочку  со случайными белыми снежинками
    t = []
    for i in range(0, rows):      
        t1 = []
        for k in range(0, rows - i - 1):
            t1.append((" " if random.randint(0, 5) else "."))
        t1.append(" ")
        t1 = t1+  list("*" * (2 * i + 1))
        t1.append(" ")
        for k in range(0, rows - i - 1):
            t1.append((" " if random.randint(0, 5) else "."))
        t.append(t1)
    tree = "\n".join("".join(line) for line in t)
    # print(tree)
    return tree
    

import time

while 1:
    tree = c_tree(30)
    print(tree, end = '')
    print('\b'*len(tree), end = '', flush = True)    
    time.sleep(0.1)
   
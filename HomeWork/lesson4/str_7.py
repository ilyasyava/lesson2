# Запросить число
# вывести это число разбитое на порядки
#     Пример:
#     1234567 -> 1 234 567
#     5678 -> 5 678
#
#     (решить без for)
from dataclasses import replace

num = int(input("Введите ваше число: "))
num_sp = format(num, ",")
nums = num_sp.replace(",", " ")

print(f"{num} -> {nums}")
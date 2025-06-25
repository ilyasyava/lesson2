# '''
# Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
# '''
a, b, c = map(int, input("Введите три числа через пробел: ").split())

print("Наибольшее число: ", end="")

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
# '''
# Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.
# '''
def factorial(n: int):
    if n <0:
        return "Ошибка! Только положительные числа"
    elif n == 0 or n == 1:
        return 1

    res = 1
    for i in range(1, n + 1):
        res *= i

    return res

n = int(input("Введите число: "))
print(f"Факториал для {n} = {factorial(n)}")


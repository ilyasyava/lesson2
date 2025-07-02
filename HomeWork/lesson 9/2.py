# '''
# Написать рекурсивную функцию, которая вычисляет
# факториал переданного в нее числа.
# '''
def factorial(n):
    if n == 0 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Введите число, для проверки факториала: "))
print(f"{num}! ==> {factorial(num)}")



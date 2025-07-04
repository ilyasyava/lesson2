# '''
# Написать рекурсивную функцию, которая вычисляет
# факториал переданного в нее числа.
# '''
def factorial(n):
    if n == 0 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
while True:
    try:
        num = int(input("Введите число, для проверки факториала: "))
        break
    except ValueError:
        print("\nВы ввели не число или ввели не корректно!\n")
print(f"{num}! ==> {factorial(num)}")



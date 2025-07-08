
# """
# Написать генератор factorial, который возвращает подряд значения факториала
#
# Например:
#
# factorial_gen = factorial()
#
# next(factorial_gen) -> 1
# next(factorial_gen) -> 2
# next(factorial_gen) -> 6
# next(factorial_gen) -> 24
# """
def factorial(last_number=10):
    f = 1
    for j in range(1, last_number + 1):
        f *= j
        yield f

max_num = 10
factorial_gen = factorial(max_num)

for i in range(1, max_num + 1):
    print(f"Шаг {i}! --> {next(factorial_gen)}")
# """
# Написать функцию hello, которая принимает 2 аргумента name и surname и
# выводит принтом "Привет, {name} {surname}"
#
# Написать декоратор log_decorator, который перед выполнением
# функции печатает на экран строку, вида
# Выполняеся функция <имя> с аргусентами <аргументы>
# После выполнения функции напечатать строку "<имя функции> - завершена"
# """
def log_decorator(func):
    def wrapper(*args):
        print(f"Выполняется функция {func.__name__} с аргументами {args}")

        res = func(*args)

        print(f"Работа {func.__name__} - завершена!")

        return res
    return wrapper


@log_decorator
def hello(name, surname):
    print(f"Привет, {name} {surname}")

hello("Иван", "Иванов")


# """
# Написать декоратор который позволит не останавливать программу
# в случае если любая декорируемая функция выбрасывает ошибку,
# а выводить имя функции в которой произошла ошибка и информацию об ошибке в.
# Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))
#
# * сделать настраиваемы параметр который определяет печать в консоль или в файл
# и если в файл передать название файла
# """

def handle_errors(log_to_file=False, filename="errors.txt"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_msg = f"Ошибка в функции {func.__name__}: {str(e)}"
                print(error_msg)

                if log_to_file:
                    with open(filename, "a", encoding="utf-8") as f:
                                f.write(error_msg + "\n")

        return wrapper
    return decorator


@handle_errors(log_to_file=True, filename="my_errors.txt")
def divide(a, b):
    return a / b


@handle_errors()
def convert(text):
    return int(text)

divide(10, 0)
convert("Не число")
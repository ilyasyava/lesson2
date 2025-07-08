def f1(y):
    x = 11
    def wrapper(b):
        print(1, x, y, y*b)
    return wrapper
 

a1 = f1(11)
a2 = f1(22)

a1(2)
a2(3)

print(a2.__closure__[0].cell_contents)
print(a2.__closure__[1].cell_contents)
# ----------------------



# def print1(a):
#     def wrapper(b):
#         print(f"{a}{' - ' if a else ''}{b}")
#     return wrapper

# pr_err = print1("Error")
# pr_info = print1("Внимание")
# pr = print1("")

# pr_err("Пароль неверный") # перед сообщением будет слово Error
# pr_info("В пароле должно быть более 7 символов")
# pr("Ok")


    

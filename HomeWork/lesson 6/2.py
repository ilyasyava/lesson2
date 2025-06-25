# '''
# запросить у пользователя логин пароль и возраст
# вывести доступ разрешен:
#     логин:admin   пароль:123456    возраст: любой
#     логин:vasya   пароль: vas123   возраст: менее 60
#     логин:guest   пароль: любой    возраст:более 18
#
# в остальных случаях - "доступ запрещен".
# '''
user_data = {"admin" : {"passw" : "123456", "age" : "*"},
             "vasya" : {"passw" : "vas123", "age" : "<60"},
             "guest" : {"passw" : "*", "age" : ">18"}
}
log, passw, age = (input("Введите логин: "),
                   input("Введите пароль: "),
                   int(input("Введите ваш возраст: "))
)
if log in user_data:
    if (user_data[log]["passw"] == passw or
    user_data[log]["passw"] == "*"):
        if user_data[log]["age"] == "*" or eval(
            str(age) + user_data[log]["age"]):
            print("Доступ разрешен!")
        else:
            print("Доступ запрещён, не верный возраст!")
    else:
        print("Доступ запрещён, не верный логин/пароль")

#Или самый простой вариант который только может быть:

# if log == "admin" and passw == "123456" and age:
#     print("Доступ разрешен")
# elif log == "vasya" and passw == "vas123" and age < 60:
#     print("Доступ разрешен")
# elif log == "guest" and passw and age > 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещён")





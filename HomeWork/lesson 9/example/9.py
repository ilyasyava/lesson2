# def f1():
#     global a
#     l.append(55)
#     print(a2)
#     a = 2
#     a += 1
#     b = 2
#     print(2, locals())
#     def f2():
#         # global b
#         nonlocal b
#         a = 3    
                 
#         print(333, locals())
#         print('bbbb', b)
#         b += 2
        
#     print(1234, b)
#     f2()
#     print(12345, b)
    

# a = 1
# a2 = 3
# l = [1, 2, 3]
# f1()
# # f2()
# print(a)

# print(1, globals())
# # print(2, locals())
# print(l)

# -----------------------------
# рекурсия
# 
# n = 0
# def f1():
#     global n
#     n += 1
#     print(n)
#     f1()
    
# f1()

# def f2(text):
#     # if text:
#     #     print(text)
#     #     f2(text[:-1])
#     # return 
#     if not text:
#         return
#     print(text)
#     f2(text[:-1])
    
# f2("Hello PYTHON")


# ----------------------------------------
# неограниченное количество параметров/аргументов


# def f1(*args, sep="\n"):
#     print(*args, sep=sep)
#     # for item in text:
#     #     print(item)

# def f2(*, p1, p2):
#     print(p1, p2)
    
# # print(1, 2, 3, 4, 5)
# f1("Hello", "Python", 2, 3, 7, " ", sep=" - ")
# f2(p1=1, p2=2)

# def f3(val4, **kwargs):
#     print(kwargs)
#     print(kwargs.get('val3'))

# f3(val1=1, val2=3, val3="Hello", val4=1234)


# def f4(p1,  p2=0, *args, **kwargs):
#     print(p1, p2, args, kwargs)

# f4(123, 111, 1, 5, 10, v1=123, v2=1234)
# f4(123, 111, v1=123, v2=1234)

# f4(123, 111, 1, 5, 10, p2=222, v1=123, v2=1234)
# TypeError: f4() got multiple values for argument 'p2'
# Потому что второй позиционный аргумент "111", он уже назначен p2, 
#   а потом опять p2=111 ещё раз.



# ---------------------------

# a = 1, 2, 3
# a, *b, c = [1, 2, 3, 4, 5]
# print(a, b, c)
# --------------------------

# lambda  - анонимная функция

# def f1(x):
#     # s = x+2*2
#     return x+2*2


# print(f1(2))
# print((lambda x: x+2*2)(2))
# a = lambda x: x+2*2
# print(a(2))

# b = [1, 2, 3, 10]
# b2 = map(f1, b)
# print(*b2)
# b3 = map(lambda x:x+x*x, b)
# print(*b3)

# print((lambda x: True if x == 1 else False)(5))
# print((lambda x: x==1)(5))
# print((lambda x1, x2: x1+x2+24)(5, 7))

# --------- sorted


# def f1(x):
#     return x[-1]

# l = ["qwe", 'dsdsda', 'b', 'dsdd']
# l.sort(key=len)
# l.sort(key=lambda x: x[-1])
# l.sort(key=f1)
# print(l)

# a = [[11, 2], [2, 4], [1, 5], [8, 3]]
# b = sorted(a, key=lambda x: x[1])


# сортировка словарей
# d = {1:11, 9:22, 3:33, 4:77, 7:44}
# print(d.items())
# d2 = dict(sorted(d.items(), key=lambda item:item[0])) # сортировка по ключу
# d3 = dict(sorted(d.items(), key=lambda item:item[1])) # сортировка по значению
# print(d2)
# print(d3)

# users = [
#     {'name':'vasia!',
#         'age':25, 
#         'surname':'vasiapupkin!', 
#         'phone':'3752323232'},
#     {'name':'DIma11111111111', 
#         'age':33,
#         'surname':'DimaKr!ivenyz', 
#         'phone':'3752323232'},
#     {'name':'Petia', 
#         'age':21,
#         'surname':'DimaKrivenyz', 
#         'phone':'3752323232'}
# ]

# b = sorted(users, key=lambda user: user['age'], reverse=True)
# b = sorted(users, key=lambda user: len(user['name']), reverse=True)

# print(b)

# # -----------------
# # filter

# def f1(user):
#     return "!" in user['surname']

# users2 = filter(lambda user: "!" in user['surname'], users)
# users2 = filter(f1, users)
# print(*users2)







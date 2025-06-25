from time import sleep

# while (пока)- когда не знаем сколько повторов
# for - когда знаем сколько раз повторить, или что то перебрать

# -----------------------------------------

a = 1
b = 3
# while True:
#     print(1)
#     print(2)

# while a < 10 and b==2: 
#     print(a)   
#     sleep(0.3)
#     a += 1 # переменная счетчик

# print('ok')


# pas = input("pas: ")
# while pas != '1234':
#     print('err')
#     pas = input("pas: ")
#     if pas == 'stop':
#         break
# else:
#     print('else')

# print('ok')

# ----------------------------------


# menu = '''
# 1 - ПОГОДА
# 2 - АНЕКДОТ
# 3 - КУРСЫ ВАЛЮТ
# 0 - ВЫХОД
# '''

# res = input(menu)

# while res != '0':
#     if res == '1':
#         print(1)
#     elif res == '2':
#         print(2)
#     elif res == '3':
#         print(3)
#     else:
#         print('err')
#     res = input(menu)
#     break

# a = 0 
# a = 1 
# b = "Hello"
# while 1:
# while a:
# while len(b):
#     b = b[:-1]

# --------------------------------------

# for i in range(3): # повторить 3 раза
#     # i = 1
#     print(1, "номер - " + str(i))
#     print(2, "номер - " + str(i))
#     print(3, "номер - " + str(i))
#     print("--------")
    

# a = range(10)
# a = range(10, 50)
# a = range(10, 50, 5)
# print(list(a))

# for i in range(3):
#     pass

for i in range(3):
     print(i)
else:
    print('ok')

# for i in [0, 1, 5, 6]:
#     print(i)


# for i in "___":
#     print(i)
#     i = i * 50
#     print(i)
    
# j  = 10
# for i in "___":
#     print(i)
#     i = i * j
#     print(i)
#     j *= 2



# bad_symbol = "!@#$%^&*()"
# login = 'Vasya123@!'
# for s in login:
#     if s in bad_symbol:
#         print("errr", s)
#     # print(s)
    

    
users = ["user1", "user2", "user3", "user4"]

# for user in users:
#     print(user)

# for i in range(len(users)):
#     print(i+1, users[i])

# for i, user in enumerate(users, 1):
#     print(i, user)
    
# print(*users, sep='\n')  

# --------------------------------------

# users = [
#     {"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya2", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya3", "login":"vva@siiiia!",  "age":23},    
#     {"name":"Vasya4", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya5", "login":"vvasiiiia!",  "age":23},    
#     {"name":"Vasya6", "login":"vv#asiiiia",  "age":23},    
#     {"name":"Vasya7", "login":"vvasiiiia",  "age":23},    
#     {"name":"Vasya8", "login":"vvasiiiia!",  "age":23}
# ]

# for user in users:
#     print(user['name'], user['age'])

# for user in users:
#     for key in user:
#         # print(key, user[key], user['age'])
#         print(user[key], end=' ')
        
        
#     print('===')

  
# user = {"name":"Vasya1", "login":"vvasiiiia",  "age":23}

# for key in user:
#     print(key, user[key])
    
# for v in user.values():
#     print(v)
    
# for user1 in user.items():
#     print(user1, user1[0], user1[1])
    
# for key, val in user.items():
#     print(key, val)    
    
# -------------------------------

a = [1, 2, 3]
b = [4, 5, 6]
c = [8, 9, 0]
for i1, i2, i3 in zip(a, b, c): # перебор двух списков
    print(i1, i2, i3)
    
    

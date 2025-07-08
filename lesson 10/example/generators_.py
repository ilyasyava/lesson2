
# a = [i for i in range(1_000_000)]
# b = (i for i in range(1_000_000))

# for i in b:
#     print(i)
    
# print(a.__sizeof__())
# print(b.__sizeof__())

# def f1(): 
#     # print(1)   
#     yield 11
#     # print(2)
#     yield 22
#     yield 33
#     yield 44
    
# a = f1()

# # a[1] # ошибка

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# for i in a:
#     print(111, i)
    
# for i in f1():
#         print(2222, i)
        
# def f1(n):
#     for i in range(n):
#         yield i*i+i
        
# def f2(n):
#     i = 0
#     while i<n:
#         yield i*n
#         i+=1
    
# a = f2(10)

# # print(len(a))

# for i in f2(10):
#     print(i)


# ---------------------------


# --------------
# def f1():
#     yield 111
#     yield 222
#     yield 333
    
# def f2():
#     yield 11111
#     yield 22222
#     yield 33333
    
# def f3(a=f1(), b=f2()):        
#     while 1:
#         try:
#             yield next(a)
#             yield next(b)
#         except StopIteration:
#             break

# for item in f3():
#     print(item)
    
    

def ping():
    yield "ping1"
    yield "ping2"
    yield "ping3"

def main():
    yield "start"
    yield from ping()
    yield "end"

for x in main():
    print(x)
    
    # -----------------------


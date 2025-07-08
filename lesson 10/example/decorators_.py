from time import time, sleep

# def f1(func):    
#     def wrapper(*args, **kwargs):
#         print(1)
#         res = func(*args, **kwargs)
#         print(2)
#         return res
#     return wrapper

# def f11(func):    
#     def wrapper(*args, **kwargs):
#         start = time()
#         print("Hello")
#         res = func(*args, **kwargs)        
#         print(round(time() - start,2))
#         return res
#     return wrapper


# # @f11
# @f1
# def f2(word1, word2, a=0, b=0):
#     print(f"Hello {word1} {word2}")
#     sleep(1)
#     return 123
    
# @f11
# def f3():
#     print("Hello World")   
    
    
# # print(f2("Python", "Python2"))
# # f3()

# a = f2.__closure__[0].cell_contents
# print(a)
# a(1, 2)
    

    
     
     
     

# ------------------------------
# декораторы с настройкой параметров
    
def loging(filename='3.txt'):
    # print(filename)
    def _loging(func):
        def wrapper(*args, **kwargs):
            with open (filename, "a", encoding='utf8') as f:
                from time import time, ctime, strftime
                # f.write(f"{ctime()} - запущена {func.__name__}\n")
                f.write(f"{strftime('%M:%S')} - запущена {func.__name__}\n")                
            func(*args, **kwargs)                            
        return wrapper
    return _loging


@loging(filename="log1.txt")
def f1():
    a = 1+1
    
@loging(filename="log2.txt")
def f2():
    a = 1+1
    
@loging()
def f3():
    a = 1+1
    
f1()
         
# file = open("lesson10\\example\\111.txt", "a")
# file.write("Hello 123" + "\n")
# file.close()

# print(__file__)
import os
path = os.path.dirname(__file__)
# print(path)

with open(os.path.join(path, "123.txt"), "a", encoding="utf-8") as f:
    f.write("Привет 123" + "\n")

# with open("lesson10\\example\\111.txt", "r", encoding="utf-8") as f:
# #     # a = f.read(3)
# #     # a = f.read()
# #     # a = f.readlines()
# #     # print(a)
#     for line in f:
#         print(line, end="")
    
    
    
# print(123)
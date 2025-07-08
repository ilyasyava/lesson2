# """
# Написать функцию которая принимает строку в которой есть
# круглые скобки и возвращает True или False анализируя все ли скобки
# являются закрытыми и расставлены в правильном порядке.
# Примеры:
#     (()()) -> True
#     (()()() -> False
#     (hello(2)ver()(33)python) -> True
#     (hello(2()ver(33)python)) -> True
#     (hello(2()ver(33)python) -> False
#
# """
def check_brackets(s):
    s = "".join([i for i in s if i in "()"])
    count = 0
    for i in s:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


print(check_brackets("(()())"))
print(check_brackets("(()()()"))
print(check_brackets("(hello(2)ver()(33)python)"))
print(check_brackets("(hello(2()ver(33)python))"))
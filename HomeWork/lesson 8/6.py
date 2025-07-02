# """
# Напишите функцию yes_or_no, которая принимает список из целых чисел,
# а возвращает список из Yes или No для каждого элемента,
# Yes - если число уже встречалось и No, если нет
# [1,2,3,1,4] => [no, no, no, yes, no]
#
# если в списке не все целые числа вернуть False.
# """
def yes_or_no(nums):
    for n in nums:
        if not isinstance(n, int):
            return False

    slovar = set()
    res = []

    for num in nums:
        if num in slovar:
            res.append("yes")
        else:
            res.append("no")
            slovar.add(num)

    return res

nums = list(map(int, input("Введите цифры: ")))

print(yes_or_no(nums))
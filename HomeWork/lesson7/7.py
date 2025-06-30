# """
# Запросить любое число не менее 10.
# Вывести на экран сумму квадратов каждой цифры составляющей это число.
# Например: дано 236 => 2*2 + 3*3 + 6*6 = 49
# """
nums = (input("Введите число не менее 10: "))

if nums.isdigit() and int(nums) > 10:
    num = list(nums)
    formula = ' + '.join(f"{d}*{d}" for d in num)
    sum_sq = sum(int(d) ** 2 for d in num)
    print(f"Нам дано число {nums} ==> {formula} = {sum_sq}")
else:
    print("Введите число больше 10!")









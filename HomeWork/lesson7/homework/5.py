# '''
#
# Дан списк:
# ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
# Для каждого элемента в списке
#     - вывести на экран сначала номер элемента
#     - сам элемент
#     - символ данного элемента, соответствующий номеру его позиции в списке.
# Образец:
# 1 - qwertyu - q
# 2 - asdfggh - s
# 3 - zxcvbnm - c
# и так далее...
#
#
# '''
lis = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']

for i, j in enumerate(lis, 1):
    for q in j:
        q = j[i - 1]
    print(f"{i} - {j} - {q}")
# """
# дан словарь
# d = {'one':11, 'two':22, 'hello':'python', True:False}
# запросить номер элемента и удалить его из словаря с помощью del.
# """
d = {'one':11, 'two':22, 'hello':'python', True:False}

el = int(input("Введите номер элемента, который хотите удалить: "))
if el == 1:
    el = 'one'
elif el == 2:
    el = 'two'
elif el == 3:
    el = 'hello'
elif el == 4:
    el = True

del d[el]

print(d)

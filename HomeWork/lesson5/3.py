# """
# дан словарь
# d = {'one':11, 'two':22, 'hello':'python', True:False}
# запросить номер элемента и удалить его из словаря с помощью del.
# """
d = {'one':11, 'two':22, 'hello':'python', True : False}

el = int(input("Введите номер элемента, который хотите удалить: "))
del d[list(d.keys())[int(el) - 1]]

print(d)

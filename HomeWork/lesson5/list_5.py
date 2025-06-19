# '''
# Дан список
# ['samsung', 'lg', 'xerox', 'bosch']
# Удалить элемент с именем 'xerox'
# Добавить элемент на 2 место 'indesit'
# '''
company = ['samsung', 'lg', 'xerox', 'bosch']
company.remove('xerox')
company.insert(1, 'indesit')

print(company)
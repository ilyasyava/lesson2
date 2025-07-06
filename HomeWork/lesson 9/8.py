# '''
# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы
#  - остались только строки.
#  - остался только логический тип.
# '''
data = [123, "hello", True, 3.14, False, [1, 2], {"key": "value"}, 'world', 0]
string = list(filter(lambda x: isinstance(x, str), data))
booleans = list(filter(lambda x: isinstance(x, bool), data))

print(f"Остались только строки: \n{string}")
print(f"Остался только логический тип: \n{booleans}")

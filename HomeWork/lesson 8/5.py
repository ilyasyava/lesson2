# '''
# Написать функцию count_char, которая принимает строковое значение,
# из которого создает и возвращает словарь, следующего вида:
# {'буква': 'количество-вхождений-в-строку'}
# Нельзя пользоваться collections.Counter!
# '''
def count_char(text: str):
    text = text.lower().replace(" ", "").replace(".", "").replace(",", "")

    res = {}
    for i in text:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

text = input("Введите текст: ")

print(count_char(text))
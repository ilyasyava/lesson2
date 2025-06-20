# """
# Запросить фразу
#     - вывести на экран количество уникальных символов
#     - вывести на экран количество уникальных слов
#     -* вывести символ который встречался чаще всего
# """
from collections import Counter

text = input("Введите фразу: ")

uniq_s = set(text)
words = text.split()
unic_w = set(words)

m_com_s, count = Counter(text).most_common(1)[0]

print(f"-Уникальное количество символов = {len(uniq_s)}\n"
      f"-Уникальное количество слов = {len(unic_w)}\n"
      f"-Самый частый символ - {m_com_s} - {count} раз"
)




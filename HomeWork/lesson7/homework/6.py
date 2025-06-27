# """
# 1. Запросить у пользователей имя и отзыв о магазине.
# Программа должна запрашивать данные пока не введено слово "stop".
# Все данные сложить в словарь.
#     -распечатать количество отзывов
#     -распечатать отдельно имена пользователей
#     -распечатать отдельно отзывы
#
# """
from soupsieve.util import lower

feedback_dict = {}

while True:
    fb_n = input("Введите ваше имя: ")
    if lower(fb_n) == "stop":
        break
    fb = input("Введите ваш отзыв: ")
    if lower(fb) == "stop":
        break
    feedback_dict[fb_n] = fb

print(f"{'Статистика':-^40}\n"
      f"    - Количество отзывов: {len(feedback_dict)}\n"
      f"    - Имена посетителей: {list(feedback_dict.keys())}\n"
      f"    - Отзывы: {list(feedback_dict.values())}")

# Или такой вариант:

# print(f"{'Статистика':-^40}\n"
#       f"    - Количество отзывов: {len(feedback_dict)}")
#
# print("Имена:")
# for i in feedback_dict.keys():
#     print(f"    -{i}")
# print("Отзывы:")
# for j in feedback_dict.values():
#     print(f"    -{j}")


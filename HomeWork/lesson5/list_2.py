# '''
# Запросить по очереди у пользователя 5 имен. Добавить все в список.
# Отсортировать.
# Вывести на экран.
# Вывести True при наличии в списке имени 'Вася'
# '''
name_1 = str(input("Введите 1 имя: ")).capitalize()
name_2 = str(input("Введите 2 имя: ")).capitalize()
name_3 = str(input("Введите 3 имя: ")).capitalize()
name_4 = str(input("Введите 4 имя: ")).capitalize()
name_5 = str(input("Введите 5 имя: ")).capitalize()

names = [name_1, name_2, name_3, name_4, name_5]
names.sort()

print(f"{names}\n"
      f"Вася в вашем списке имен: {"Вася" in names}"
)


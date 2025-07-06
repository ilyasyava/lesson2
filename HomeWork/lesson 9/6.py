# """
# Дан словарь наблюдения за температурой
# {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}.
# Отсортировать словарь по температуре в порядке возрастания и обратно.
# """
temp_d = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}
temp_d1 = dict(sorted(temp_d.items(), key=lambda item:item[1]))
temp_d2 = dict(sorted(temp_d.items(), key=lambda item:item[1], reverse=True))
print(temp_d1)
print(temp_d2)
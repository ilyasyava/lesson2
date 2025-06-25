# """
# Запросить у пользователя год рождения и в соответствии с его возрастом
# охарактеризовать пользователя -
# ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
# """
import time

year_bir = int(input("Введите год вашего рождения: "))
current_year = time.localtime().tm_year
age = current_year - year_bir

if age <= 10:
    print("Вы - ребёнок")
elif age <= 15:
    print("Вы - подросток")
elif age <= 20:
    print("Вы - юноша")
elif age <= 45:
    print("Вы в расцвете сил")
elif age <= 65:
    print("Вы - пожилой")
else:
    print("Вы - старик")
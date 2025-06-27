# """
# Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0.
# Выдать средний бал ученика.
# """
print("Введите оценки ученика по одной")

mks = []

while True:
    try:
        mk = int(input("Оценка: "))
        if mk == 0:
            break
        elif 1 <= mk <=10:
            mks.append(mk)
        else:
            print("Введите оценку от 1 до 10")
    except ValueError:
        print("Введите число!")

print(f"Средняя оценка ученика: {sum(mks) / len(mks):.2f}")










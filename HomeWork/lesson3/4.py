num = int(input("Введи ваше число: "))

thus = num // 1000
huns = (num // 100) % 10
tens = (num // 10) % 10
last = num % 10

print(f"Вы ввели число: {num}\n"
      f"Тысячи = {thus}\n"
      f"Сотни = {huns}\n"
      f"Десятки = {tens}\n"
      f"Еденицы = {last}"
      )
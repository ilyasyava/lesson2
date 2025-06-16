your_sec = int(input("Введите количество секунд: "))

a = your_sec

hrs = a // 3600
a_new = a % 3600
mins = a_new // 60
secs = a_new % 60

print(f"Вы ввели {your_sec} секунд, в переводе на часы это:\n"
      f"{hrs:02d}:{mins:02d}:{secs:02d}\n"
)

print(hrs, mins, secs, sep=":")


# Но мне кажется это очень просто и не красиво
# Хотя можно было сделать ещё переменную и заменить её
# На форматную строку и написать так:
# time_f = "{:02d}:{:02d}:{:02d}".format(hrs, mins, secs)
# print(time_f)

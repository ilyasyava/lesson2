# """
# Написать функцию  которая принимает фамилию имя и отчество одной стройкой,
# а возвращает в виде краткого формата.
# Функция должна содержать необязательный параметр в виде логического значения
# и в зависимости от него возвращала ФИО в двух следующих форматах:
#  -  Николаев И.С.
#  -  И.С.Николаев
# """
def fio(full_name: str, rev=True):
    parts = full_name.split()

    if len(parts) != 3:
        return "Вы не ввели ФИО корректно"

    surname, name, pat = parts

    if rev:
        res = f"{surname} {name[0]}. {pat[0]}."
    else:
        res = f"{name[0]}. {pat[0]}. {surname}"
    return res

full_name = input("Введите ФИО через пробел: ")

print(f" - {fio(full_name)}\n "
      f"- {fio(full_name, rev=False)}")







# '''
#
# Написать функцию, которая возвращает любое число в виде денежной величины
# с разделителями групп разрядов в качестве пробела и валютой в конце.
# Денежная величина всегда должна содержать количество копеек в виде дух
# знаков после точки, даже если исходное число целое.
# *Нельзя использовать форматную строку.
# Например: 1234567 -> "1 234 567.00 руб."
#
# с помощью try перехватить возможные ошибки.
# '''
def format_money(n: float):
    try:
        rubs = int(n)
        kops = round((n - rubs) * 100)
        if kops < 10:
            kops_str = "0" + str(kops)
        else:
            kops_str = str(kops)
        gruppa = []
        rubs_str = str(rubs)
        i = len(rubs_str)

        while i > 0:
            i -= 3
            start = max(i, 0)
            gruppa.append(rubs_str[start:i+3])

        form_rubs = ' '.join(reversed(gruppa))

        return form_rubs + '.' + kops_str + ' руб.'

    except:
        return "Ошибка ввода"

n = float(input("Введите число: "))

print(format_money(n))





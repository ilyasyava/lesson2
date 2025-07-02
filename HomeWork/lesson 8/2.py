# '''
# Написать функцию которая принимает 2 стороны прямоугольника
# и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.
# '''
def s_or_p(a, b, area=True):
    if a <= 0 or b <= 0:
        print("err: Некорректный ввод")
    elif area:
        return a * b
    else:
        return (a + b) * 2

try:
    while True:
        data = input("Введите стороны прямоугольника и слово"
                    "'периметр' или 'площадь' через пробел: ").lower().split()
        a, b, ch = data
        a, b = int(a), int(b)

        if ch == "площадь":
            res = s_or_p(a, b, area=True)
            print(f"Площадь прямоугольника = {res}")
            break
        elif ch == "периметр":
            res = s_or_p(a, b, area=False)
            print(f"Периметр прямоугольника = {res}")
            break
        else:
            print("Ошибка ввода. Введите 'периметр' или 'площадь'")
except ValueError:
    print("Вы ввели не число")






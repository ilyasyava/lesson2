while True:
    try:
        first_num = int(input("Введите ваше первое число: "))
        second_num = int(input("Введите ваше второе число: "))

        a = first_num
        b = second_num

        print(f'Возвёв число {a} в степень {b}, мы получили число:', a**b)
        break
    except ValueError:
        print("Пожалуйста, введите число корректно")

        #Знаю-знаю, забежал вперед)
        #Но так код выглядит приятнее)
        #Дальше по курсу будет)
# '''
# Запросить число от 1 до 12.
# Если ввели другое число сообщить об ошибке.
# Если ввели не число сообщить об ошибке.
# Когда введут допустимое число - вывести на экран соответствующее
# название месяца, пору года и сколько дней в данном месяце.
# '''
num = input("Введите число от 1 до 12: ")

month_data = {
    "1": {"month_name": "Январь", "days": 31, "season": "Зима"},
    "2": {"month_name": "Февраль", "days": 28, "season": "Зима"},
    "3": {"month_name": "Март", "days": 31, "season": "Весна"},
    "4": {"month_name": "Апрель", "days": 30, "season": "Весна"},
    "5": {"month_name": "Май", "days": 31, "season": "Весна"},
    "6": {"month_name": "Июнь", "days": 30, "season": "Лето"},
    "7": {"month_name": "Июль", "days": 31, "season": "Лето"},
    "8": {"month_name": "Август", "days": 31, "season": "Лето"},
    "9": {"month_name": "Сентябрь", "days": 30, "season": "Осень"},
    "10": {"month_name": "Октябрь", "days": 31, "season": "Осень"},
    "11": {"month_name": "Ноябрь", "days": 30, "season": "Осень"},
    "12": {"month_name": "Декабрь", "days": 31, "season": "Зима"},
}
if not num.isdigit():
    print("Ошибка! Вы ввели не число!")
elif num not in month_data:
    print("Ошибка! Вы ввели число вне диапазона от 1 до 12")
else:
    month = month_data[num]
    print(
f"Вы ввели {month['month_name']}, это {month['season']}, в нем {month['days']} дней."
)
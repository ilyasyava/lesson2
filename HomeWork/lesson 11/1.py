# """
# Создать класс Phone, у которого будут следующие атрибуты:
#
# Определить атрибуты:
#
# - brand - бренд
# - model - модель
# - issue_year - год выпуска
#
# Определить методы:
#
# - инициализатор __init__
# - receive_call, который принимает имя звонящего и выводит на экран:
#         <Бренд-Модель> - Звонит {name}
# - get_info, который будет возвращать кортеж (brand, model, issue_year)
# - метод __str__, который выводит на экран информацию об устройстве:
# Бренд: {}
# Модель: {}
# Год выпуска: {}
# """
class Phone:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def receive_call(self, name: str):
        print(f"{self.brand}-{self.model} - Звонит {name}")

    def get_info(self):
        return (self.brand, self.model, self.year)

    def __str__(self):
        return f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}"


phone1 = Phone("iPhone", "15 Pro", 2023)
phone2 = Phone("Samsung", "Galaxy S24", 2024)

phone1.receive_call("Анна\n")

print(phone1, "\n")

print(phone1.get_info(), "\n")





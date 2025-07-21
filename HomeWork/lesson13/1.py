# """
# Создать класс User с атрибутами:
#
# Свойства:
# 	- name - имя - содержит только буквы русского алфавита
# 	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
# 	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия:
#                 содержит менее шести символов
#                 содержит строчную букву
#                 содержит заглавную букву
#                 содержит число
# 	- is_blocked - заблокирован
# 	- subscription_date - дата до какой действует подписка
# 	- subscription_mode - вид подписки (free, paid)
#
#
# Методы:
# 	- bloc - принимает логическое значение и помечает пользователя заблокированным
# 	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату.
# 						Если дата не передана значит на дату проверки.
# 						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
# 	- change_pass - смена пароля и присваивание его в качестве действующего.
# 						Пароль должен пройти валидацию.
# 						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
# 	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.
#
#
#
# Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
# Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
# При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
# При изменении даты подписки  вид подписки меняется на платный.
# Валидацию данных сделать через регулярные выражения
# """
import re
import random
import string
from datetime import datetime, timedelta

class User:
    def __init__(self, name, login, password=None):
        self.name = self._validate_name(name)
        self.login = self._validate_login(login)
        self.password = self._validate_or_generate(password)
        self.is_blocked = False
        self.subscription_date = datetime.now() + timedelta(days=30)
        self.subscription_mode = "free"

    def _validate_name(self, name):
        if not re.fullmatch(r'^[а-яА-ЯёЁ]+$', name):
            raise ValueError("Имя должно быть только на русском языке!")
        return name

    def _validate_login(self, login):
        if not re.fullmatch(r'^[a-zA-Z0-9_]{6,}$', login):
            raise ValueError("Логин должен содержать не менее 6 символов: латинские буквы, цифры, _")
        return login

    def _is_valid_password(self, password):
        return (len(password) >= 6 and
                re.search(r'[a-z]', password) and
                re.search(r'[A-Z]', password) and
                re.search(r'\d', password))

    def _generate_password(self):
        while True:
            pwd = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            if self._is_valid_password(pwd):
                return pwd

    def _validate_or_generate(self, password):
        if password:
            if not self._is_valid_password(password):
                raise ValueError("Пароль не соответствует требованиям")
            return password
        pwd = self._generate_password()
        print(f"Сгенерированный пароль: {pwd}")
        return pwd

    def block(self, status: bool):
        self.is_blocked = status

    def check_subscr(self, date=None):
        target_date = datetime.strptime(date, "%Y-%m-%d").date() if date else datetime.now().date()
        end_date = self.subscription_date.date()
        days_left = (end_date - target_date).days
        return {
            "active": days_left >= 0,
            "mode": self.subscription_mode,
            "days_left": max(days_left, 0)
        }

    def change_pass(self, new_pass=None):
        self.password = self._validate_or_generate(new_pass)

    def set_subscription(self, end_date, mode="paid"):
        self.subscription_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.subscription_mode = mode

    def get_info(self):
        if self.is_blocked:
            print(f"Пользователь {self.name} ({self.login}) заблокирован")
            return

        sub_info = self.check_subscr()
        print(f"Имя: {self.name}")
        print(f"Логин: {self.login}")
        print(f"Пароль: {'*' * len(self.password)}")
        print(f"Подписка: {self.subscription_mode}")
        print(f"Подписка до: {self.subscription_date.strftime('%Y-%m-%d')}")
        print(f"Статус: {'активна' if sub_info['active'] else 'неактивна'}")

try:
    user1 = User("Иванов", "ivan_123", "A1b2c3d")
    user2 = User("Петров", "petr_2025")  # без пароля — сгенерируется автоматически

    print("Информация о пользователе:")
    user1.get_info()

    user1.block(True)
    print("\nПосле блокировки:")
    user1.get_info()

    print("\nСмена пароля:")
    user2.change_pass("newPass123")
    user2.get_info()

    print("\nПроверка подписки на 2025-07-29:")
    print(user1.check_subscr("2025-07-29"))

    user1.set_subscription("2025-07-20", "paid")
    print("\nНовая подписка:")
    user1.get_info()


except Exception as e:
    print("Ошибка:", e)


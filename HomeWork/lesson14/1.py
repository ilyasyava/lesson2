# """
# Используя класс из пред.урока обеспечить хранение и сохранение любых изменений в базе
# данных. Для этого можно к примеру добавить в класс метод save который будет сохранять или
# создавать пользователя в базе данных и использовать его при любых изменениях.
#
#
# * в базе данных создать таблицу предоставляемых услуг со след полями
# 	название
# 	тип (1 - платная 0 - бесплатная)
# 	стоимость
# 	период в днях
# ** в класс пользователя добавить методы:
# 	добавить услугу (услуг у одного пользователя может быть несколько)
# 	продлить услугу (продлить можно если услуга еще не закончена, иначе добавить)
# 	удалить услугу
# *** создать консольное или оконное приложение которое показывает меню и отрабатывает выбранный пункт.
# 	Меню:
# 		1 - показать пользователей
# 		2 - информация о пользователе (в т.ч. и подключенные услуги)
# 		3 - список услуг
# 		4 - показать пользователей с определенной услугой
# 		5 - показать пользователей у которых за прошедший месяц окончился период хоть одной услуги
#
# """
import sqlite3
import re
from datetime import datetime, timedelta

DB_NAME = "users_.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            login TEXT UNIQUE,
            password TEXT,
            is_blocked INTEGER,
            subscription_date TEXT,
            subscription_mode TEXT
        )""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type INTEGER,
            cost REAL,
            period_days INTEGER
        )""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_services (
            user_id INTEGER,
            service_id INTEGER,
            start_date TEXT,
            end_date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(service_id) REFERENCES services(id)
        )""")


class User:
    def __init__(self, login):
        self.login = login
        self.load_from_db()

    def load_from_db(self):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE login=?", (self.login,))
            data = cursor.fetchone()
            if not data:
                raise Exception("Пользователь не найден.")
            self.id, self.name, self.login, self.password, self.is_blocked, sub_date, self.subscription_mode = data
            self.subscription_date = datetime.strptime(sub_date, "%Y-%m-%d")

    def get_info(self):
        print(f"\nИмя: {self.name}")
        print(f"Логин: {self.login}")
        print(f"Пароль: {'*' * len(self.password)}")
        print(f"Подписка до: {self.subscription_date.date()}, режим: {self.subscription_mode}")
        print(f"Статус: {'Заблокирован' if self.is_blocked else 'Активен'}")

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT s.name, s.type, s.cost, us.end_date FROM user_services us
                JOIN services s ON s.id = us.service_id
                WHERE us.user_id=?
            """, (self.id,))
            rows = cursor.fetchall()
            if not rows:
                print("Нет подключённых услуг.")
            else:
                print("Услуги:")
                for row in rows:
                    typ = "Платная" if row[1] else "Бесплатная"
                    print(f"  - {row[0]} ({typ}, {row[2]} руб.) до {row[3]}")

    def change_password(self):
        new = input("Новый пароль: ")
        if not self._is_valid_password(new):
            print("Пароль должен содержать минимум 6 символов, 1 заглавную, 1 строчную и 1 цифру.")
            return
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("UPDATE users SET password=? WHERE id=?", (new, self.id))
        print("Пароль обновлён.")

    def block_user(self, status=True):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("UPDATE users SET is_blocked=? WHERE id=?", (int(status), self.id))
        self.is_blocked = status
        print("Пользователь заблокирован." if status else "Пользователь разблокирован.")

    def add_service(self, service_id):
        now = datetime.now()
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT period_days FROM services WHERE id=?", (service_id,))
            res = cursor.fetchone()
            if not res:
                print("Услуга не найдена.")
                return
            period = res[0]
            end_date = now + timedelta(days=period)
            cursor.execute("""
                INSERT INTO user_services (user_id, service_id, start_date, end_date)
                VALUES (?, ?, ?, ?)
            """, (self.id, service_id, now.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
            print("Услуга подключена.")

    def remove_service(self, service_id):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("DELETE FROM user_services WHERE user_id=? AND service_id=?", (self.id, service_id))
        print("Услуга удалена.")

    def _is_valid_password(self, password):
        return (len(password) >= 6 and
                re.search(r'[a-z]', password) and
                re.search(r'[A-Z]', password) and
                re.search(r'\d', password))


def create_test_data():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            users = [
                ("Иванов", "ivan_123", "A1b2c3D", 0, "2025-08-30", "paid"),
                ("Петров", "petr_2025", "B2c3d4E", 0, "2025-09-15", "free"),
                ("Сидоров", "sidor_999", "C3d4e5F", 1, "2025-07-10", "paid"),
            ]
            for u in users:
                cursor.execute("""
                    INSERT INTO users (name, login, password, is_blocked, subscription_date, subscription_mode)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, u)

        cursor.execute("SELECT COUNT(*) FROM services")
        if cursor.fetchone()[0] == 0:
            services = [
                ("Антивирус", 1, 199.0, 30),
                ("Облачное хранилище", 1, 99.0, 30),
                ("Бесплатная поддержка", 0, 0.0, 60),
            ]
            for s in services:
                cursor.execute("""
                    INSERT INTO services (name, type, cost, period_days)
                    VALUES (?, ?, ?, ?)
                """, s)

        conn.commit()


def main_menu():
    while True:
        print("\nМеню:")
        print("1 - Список пользователей")
        print("2 - Работа с пользователем")
        print("0 - Выход")

        match input("Выбор: "):
            case "1":
                list_users()
            case "2":
                login = input("Введите логин пользователя: ")
                try:
                    user = User(login)
                    user_menu(user)
                except Exception as e:
                    print(e)
            case "0":
                break
            case _:
                print("Неверный выбор.")

def list_users():
    with sqlite3.connect(DB_NAME) as conn:
        for row in conn.execute("SELECT id, name, login FROM users"):
            print(f"{row[0]}. {row[1]} ({row[2]})")

def list_all_services():
    with sqlite3.connect(DB_NAME) as conn:
        for row in conn.execute("SELECT id, name FROM services"):
            print(f"{row[0]}. {row[1]}")

def user_menu(user: User):
    while True:
        print(f"\nРабота с: {user.name} ({user.login})")
        print("1 - Информация")
        print("2 - Сменить пароль")
        print("3 - Блокировка")
        print("4 - Добавить услугу")
        print("5 - Удалить услугу")
        print("0 - Назад")

        match input("Выбор: "):
            case "1":
                user.get_info()
            case "2":
                user.change_password()
            case "3":
                block = input("Заблокировать (1) или разблокировать (0)? ")
                user.block_user(bool(int(block)))
            case "4":
                list_all_services()
                sid = int(input("ID услуги: "))
                user.add_service(sid)
            case "5":
                list_all_services()
                sid = int(input("ID услуги: "))
                user.remove_service(sid)
            case "0":
                break
            case _:
                print("Неверный выбор.")



if __name__ == "__main__":
    init_db()
    create_test_data()
    main_menu()


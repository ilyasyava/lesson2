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
import random
import string
from datetime import datetime, timedelta

DB_NAME = "users.db"


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
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type INTEGER,
            cost REAL,
            period_days INTEGER
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_services (
            user_id INTEGER,
            service_id INTEGER,
            start_date TEXT,
            end_date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(service_id) REFERENCES services(id)
        )
        """)


class User:
    def __init__(self, name, login, password=None):
        self.name = self._validate_name(name)
        self.login = self._validate_login(login)
        self.password = self._validate_or_generate(password)
        self.is_blocked = False
        self.subscription_date = datetime.now() + timedelta(days=30)
        self.subscription_mode = "free"
        self.save()

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

    def save(self):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT OR REPLACE INTO users (name, login, password, is_blocked, subscription_date, subscription_mode)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (self.name, self.login, self.password, int(self.is_blocked),
                  self.subscription_date.strftime('%Y-%m-%d'), self.subscription_mode))
            conn.commit()

    def add_service(self, service_id):
        now = datetime.now()
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT period_days FROM services WHERE id=?", (service_id,))
            result = cursor.fetchone()
            if not result:
                print("Услуга не найдена")
                return
            period_days = result[0]
            end_date = now + timedelta(days=period_days)
            cursor.execute("SELECT id FROM users WHERE login=?", (self.login,))
            user_id = cursor.fetchone()[0]
            cursor.execute("""
                INSERT INTO user_services (user_id, service_id, start_date, end_date)
                VALUES (?, ?, ?, ?)
            """, (user_id, service_id, now.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
            conn.commit()

    def extend_service(self, service_id):
        now = datetime.now().date()
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT period_days FROM services WHERE id=?", (service_id,))
            result = cursor.fetchone()
            if not result:
                print("Услуга не найдена")
                return
            period_days = result[0]

            cursor.execute("SELECT id FROM users WHERE login=?", (self.login,))
            user_id = cursor.fetchone()[0]

            cursor.execute("""
                SELECT end_date FROM user_services 
                WHERE user_id=? AND service_id=?
            """, (user_id, service_id))
            res = cursor.fetchone()

            if res and datetime.strptime(res[0], "%Y-%m-%d").date() >= now:
                new_end = datetime.strptime(res[0], "%Y-%m-%d") + timedelta(days=period_days)
                cursor.execute("""
                    UPDATE user_services SET end_date=?
                    WHERE user_id=? AND service_id=?
                """, (new_end.strftime('%Y-%m-%d'), user_id, service_id))
            else:
                self.add_service(service_id)

            conn.commit()

    def remove_service(self, service_id):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE login=?", (self.login,))
            user_id = cursor.fetchone()[0]
            cursor.execute("""
                DELETE FROM user_services WHERE user_id=? AND service_id=?
            """, (user_id, service_id))
            conn.commit()


def main_menu():
    while True:
        print("\nМеню:")
        print("1 - Показать всех пользователей")
        print("2 - Информация о пользователе")
        print("3 - Список услуг")
        print("4 - Пользователи с определённой услугой")
        print("5 - Пользователи с истекшими услугами за месяц")
        print("0 - Выход")

        choice = input("Выберите пункт: ")
        if choice == "0":
            break
        elif choice == "1":
            show_users()
        elif choice == "2":
            user_info()
        elif choice == "3":
            list_services()
        elif choice == "4":
            users_with_service()
        elif choice == "5":
            expired_services()


def show_users():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        for row in cursor.execute("SELECT id, name, login FROM users"):
            print(f"{row[0]}. {row[1]} ({row[2]})")


def user_info():
    login = input("Введите логин пользователя: ")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, is_blocked, subscription_date, subscription_mode FROM users WHERE login=?", (login,))
        user = cursor.fetchone()
        if not user:
            print("Пользователь не найден")
            return
        print(f"Имя: {user[1]}\nЗаблокирован: {bool(user[2])}\nПодписка до: {user[3]}\nРежим: {user[4]}")
        cursor.execute("""
            SELECT s.name, us.end_date FROM user_services us
            JOIN services s ON us.service_id = s.id
            WHERE us.user_id = ?
        """, (user[0],))
        for row in cursor.fetchall():
            print(f"  - {row[0]} до {row[1]}")


def list_services():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        for row in cursor.execute("SELECT id, name, type, cost, period_days FROM services"):
            typ = "Платная" if row[2] else "Бесплатная"
            print(f"{row[0]}. {row[1]} — {typ}, {row[3]} руб., {row[4]} дней")


def users_with_service():
    service_id = input("Введите ID услуги: ")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.name, u.login FROM users u
            JOIN user_services us ON u.id = us.user_id
            WHERE us.service_id = ?
        """, (service_id,))
        for row in cursor.fetchall():
            print(f"{row[0]} ({row[1]})")


def expired_services():
    one_month_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT u.name, u.login FROM users u
            JOIN user_services us ON u.id = us.user_id
            WHERE us.end_date < ?
        """, (one_month_ago,))
        for row in cursor.fetchall():
            print(f"{row[0]} ({row[1]})")


if __name__ == "__main__":
    init_db()
    main_menu()

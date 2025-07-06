# """
# Дан список пользователей след. формата:
# [{"name":"some_name", "login":"some_login", "password":"some_password" },
#  ...
# ]
#
# Отфильтровать используя функцию filter() список на предмет паролей
# которые менее 5 символов.
#
# *Отфильтровать используя функцию filter() список на предмет валидных логинов.
# Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания.
# Каждому пользователю с плохим логином вывести текст
# "Уважаемый user_name, ваш логин user_login не является корректным."
# """
users = [
    {"name": "Иван", "login": "ivan_1", "password": "1234"},
    {"name": "Мария", "login": "maria-77", "password": "pass123"},
    {"name": "Петр", "login": "petr_one", "password": "secure_pass"},
    {"name": "Ольга", "login": "ольга_1", "password": "qwerty"},
    {"name": "Алексей", "login": "alex_2024", "password": "123"}
]

short_pass = list(filter(lambda user: len(user["password"]) < 5, users))
print(short_pass, "\n")

def is_valid_login(login):
    return login.replace('_', 'a').isalnum() and login.isascii()

for user in users:
    login = user["login"]
    if not is_valid_login(login):
        print(f"Уважаемый(ая) {user['name']}, ваш логин {login} не корректный.")

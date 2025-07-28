# """
#
# Переделать прежнее задание на SQLAlchemy
#
# """
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///users.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    login = Column(String, unique=True)
    password = Column(String)
    is_blocked = Column(Boolean, default=False)
    subscription_date = Column(Date)
    subscription_mode = Column(String)

    services = relationship("UserService", back_populates="user")

    def __repr__(self):
        return f"{self.name} ({self.login})"

    def info(self):
        print(f"\nИмя: {self.name}")
        print(f"Логин: {self.login}")
        print(f"Заблокирован: {'Да' if self.is_blocked else 'Нет'}")
        print(f"Подписка до: {self.subscription_date} ({self.subscription_mode})")
        if not self.services:
            print("Услуги: нет")
        else:
            print("Услуги:")
            for us in self.services:
                s = us.service
                print(f"  - {s.name} ({'Платная' if s.type else 'Бесплатная'}, {s.cost}₽) до {us.end_date}")

    def change_password(self, new_password):
        self.password = new_password
        session.commit()

    def block(self, status=True):
        self.is_blocked = status
        session.commit()

    def add_service(self, service_id):
        service = session.query(Service).get(service_id)
        if not service:
            print("Услуга не найдена")
            return

        now = datetime.now().date()
        end = now + timedelta(days=service.period_days)

        # если уже есть такая услуга и активна — продлеваем
        existing = session.query(UserService).filter_by(user_id=self.id, service_id=service_id).first()
        if existing and existing.end_date >= now:
            existing.end_date += timedelta(days=service.period_days)
        else:
            new_us = UserService(user=self, service=service, start_date=now, end_date=end)
            session.add(new_us)
        session.commit()

    def remove_service(self, service_id):
        us = session.query(UserService).filter_by(user_id=self.id, service_id=service_id).first()
        if us:
            session.delete(us)
            session.commit()
        else:
            print("Услуга не подключена.")


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(Boolean)  # 1 - платная, 0 - бесплатная
    cost = Column(Float)
    period_days = Column(Integer)

    users = relationship("UserService", back_populates="service")

    def __repr__(self):
        typ = "Платная" if self.type else "Бесплатная"
        return f"{self.id}. {self.name} ({typ}, {self.cost}₽, {self.period_days} дн.)"


class UserService(Base):
    __tablename__ = "user_services"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    start_date = Column(Date)
    end_date = Column(Date)

    user = relationship("User", back_populates="services")
    service = relationship("Service", back_populates="users")



def init_db():
    Base.metadata.create_all(engine)

def create_test_data():
    if session.query(User).count() == 0:
        users = [
            User(name="Иванов", login="ivan_123", password="A1b2c3D", subscription_date=datetime(2025, 8, 30).date(), subscription_mode="paid"),
            User(name="Петров", login="petr_2025", password="B2c3d4E", subscription_date=datetime(2025, 9, 15).date(), subscription_mode="free"),
            User(name="Сидоров", login="sidor_999", password="C3d4e5F", subscription_date=datetime(2025, 7, 10).date(), subscription_mode="paid", is_blocked=True)
        ]
        session.add_all(users)

    if session.query(Service).count() == 0:
        services = [
            Service(name="Антивирус", type=True, cost=199.0, period_days=30),
            Service(name="Облачное хранилище", type=True, cost=99.0, period_days=30),
            Service(name="Поддержка", type=False, cost=0.0, period_days=60),
        ]
        session.add_all(services)

    session.commit()



def main_menu():
    while True:
        print("\nМеню:")
        print("1 - Список пользователей")
        print("2 - Работа с пользователем")
        print("3 - Список услуг")
        print("4 - Пользователи с определённой услугой")
        print("5 - Истекшие услуги за месяц")
        print("0 - Выход")
        match input("Выбор: "):
            case "1":
                for user in session.query(User).all():
                    print(user)
            case "2":
                login = input("Логин: ")
                user = session.query(User).filter_by(login=login).first()
                if user:
                    user_menu(user)
                else:
                    print("Пользователь не найден.")
            case "3":
                for s in session.query(Service).all():
                    print(s)
            case "4":
                sid = int(input("ID услуги: "))
                users = session.query(User).join(User.services).filter(UserService.service_id == sid).all()
                for u in users:
                    print(u)
            case "5":
                month_ago = datetime.now().date() - timedelta(days=30)
                users = session.query(User).join(User.services).filter(UserService.end_date < month_ago).distinct()
                for u in users:
                    print(u)
            case "0":
                break
            case _:
                print("Неверный выбор.")

def user_menu(user: User):
    while True:
        print(f"\nПользователь: {user}")
        print("1 - Информация")
        print("2 - Сменить пароль")
        print("3 - Блокировать/разблокировать")
        print("4 - Добавить/продлить услугу")
        print("5 - Удалить услугу")
        print("0 - Назад")
        match input("Выбор: "):
            case "1":
                user.info()
            case "2":
                new_pass = input("Новый пароль: ")
                user.change_password(new_pass)
            case "3":
                user.block(not user.is_blocked)
            case "4":
                for s in session.query(Service).all():
                    print(s)
                sid = int(input("ID услуги: "))
                user.add_service(sid)
            case "5":
                for s in session.query(Service).all():
                    print(s)
                sid = int(input("ID услуги: "))
                user.remove_service(sid)
            case "0":
                break
            case _:
                print("Неверный ввод.")



if __name__ == "__main__":
    init_db()
    create_test_data()
    main_menu()



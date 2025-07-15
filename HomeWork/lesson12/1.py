# """
# Описать абстрактный класс Animal у которого:
#
# - атрибут name - кличка (тип str)
# - магический метод __init__, который принимает аргумент name
# - абстрактный метод says, который не принимает аргументов
#
# На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
# says таким образом, чтобы он возвращал строку вида:
#
# - "{кличка} - кошка. Говорит МЯУ!" для класса Cat
# - "{кличка} - собака. Говорит ГАВ!" для класса Dog
# - "{кличка} - корова. Говорит МУ!" для класса Cow
# """
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name


    @abstractmethod
    def says(self):
        pass


class Cat(Animal):
    def says(self):
        return f"{self.name} - кошка. Говорит МЯУ!"


class Dog(Animal):
    def says(self):
        return f"{self.name} - собака. Говорит ГАВ!"


class Cow(Animal):
    def says(self):
        return f"{self.name} - корова. Говорит МУ-МУ!"


murzik = Cat("Мурзик")
mumu = Dog("Муму")
musya = Cow("Муся")


print(murzik.says())
print(mumu.says())
print(musya.says())


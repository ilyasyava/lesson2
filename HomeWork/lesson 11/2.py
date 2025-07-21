# """
# Создать класс Student.
#
#
# Определить атрибуты:
#     - surname - фамилия
#     - name - имя
#     - group - номер группы
#     - grads - список оценок
#
# Определить методы:
#     - инициализатор __init__
#     - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
#     студентов по среднему баллу
#     - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
#     - метод average_grade -считает и возвращает среднюю оценку ученика
#
# Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
# и убыванию.
#
# Вывести студентов, у которых средний балл больше 8
# """
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, surname, name, group, grads=None):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads or []

    def add_grade(self, *grades):
        for grade in grades:
            if 1 <= grade <= 10:
                self.grads.append(grade)
            else:
                print(f"Оценка {grade} некорректна (должна быть от 1 до 10)")

    def average_grade(self):
        return round(sum(self.grads) / len(self.grads), 2) if self.grads else 0

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __str__(self):
        return f"{self.surname} {self.name}, группа: {self.group}, средний балл: {self.average_grade():.2f}"


students = [
    Student("Иванов", "Иван", "9А", [7, 8, 6, 9]),
    Student("Петров", "Пётр", "9Б", [5, 6, 7, 4]),
    Student("Сидорова", "Мария", "9А", [9, 9, 8, 9]),
    Student("Козлов", "Андрей", "9В", [6, 7, 7, 8]),
    Student("Николаева", "Елена", "9Б", [9, 9, 10, 8])
]

students[0].add_grade(8, 9)
students[1].add_grade(10)

print("Все студенты:")
for s in students:
    print(s)

print("\nОтсортировано по возрастанию среднего балла:")
for s in sorted(students):
    print(s)

print("\nОтсортировано по убыванию среднего балла:")
for s in sorted(students, reverse=True):
    print(s)

print("\nСтуденты со средним баллом > 8:")
high_achievers = [s for s in students if s.average_grade() > 8]
for s in high_achievers:
    print(s)
# '''
# 1.Открыть и обработать файл students_grades.txt.
# 2.Собрать все данные в словарь ниже приведенного формата.
# 3.Записать в файл "excellent_students.txt" учеников из каждого класса с наибольшим балом.
# {
#     "9A":[
#         {'fio':'fio',
#          'objects':{
#             'mathematics':[4, 9, 7],
#             'physics':[8, 9, 8, 6],
#             ...:...
#             }
#         },
#         ...
#     ],
#     "9Б":[
#         ...
#     ]
# }
#
# '''
import re

def average_score(objects):
    total = sum(sum(grades) for grades in objects.values())
    count = sum(len(grades) for grades in objects.values())
    return round(total / count, 2) if count else 0

data = {}

with open("students_grades.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = re.split(r",\s*", line, maxsplit=2)
        fio, class_name, subjects_part = parts

        subject_matches = re.findall(r"([а-яА-ЯёЁ]+(?:\s+[а-яА-ЯёЁ]+)?)\s*\(([^)]+)\)", subjects_part)

        objects = {
            subj: list(map(int, re.findall(r'\d+', grades)))
            for subj, grades in subject_matches
        }

        data.setdefault(class_name, []).append({
            'fio': fio,
            'objects': objects
        })

best_students = {
    cls: max(students, key=lambda s: average_score(s['objects']))
    for cls, students in data.items()
}

with open("excellent_students.txt", "w", encoding="utf-8") as f:
    for cls, student in best_students.items():
        avg = average_score(student['objects'])
        f.write(f"{cls}: {student['fio']} — средний балл: {avg}\n")

print("Отличники из каждого класса записаны в excellent_students.txt")
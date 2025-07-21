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

students_data = {}

try:
    with open('students_grades.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Ошибка: файл 'student_grades.txt' не найден!")
    print("Убедитесь, что он лежит в той же папке, что и скрипт.")
    exit()

for line_num, line in enumerate(lines, 1):
    line = line.strip()
    if not line:
        continue

    line = re.sub(r'^[а-яё]+[ \t]+(?=[А-ЯЁ][а-яё])', '', line).strip()

    parts = [part.strip() for part in line.split(',')]

    if len(parts) < 3:
        print(f"Строка {line_num}: слишком мало данных — пропущена")
        continue

    fio = parts[0]
    class_name = parts[1]

    if not re.match(r'\d+[А-Я]', class_name):
        print(f"Строка {line_num}: не распознан класс — '{class_name}'")
        continue

    subjects_data = {}

    for part in parts[2:]:
        match = re.match(r"(.+?)\s*\((.+)\)", part)
        if match:
            subject_name = match.group(1).strip().lower()
            grades_str = match.group(2)

            try:
                grades = [int(x.strip()) for x in grades_str.split(',') if x.strip().isdigit()]
                if grades:
                    subjects_data[subject_name] = grades
            except ValueError:
                print(f"Не удалось прочитать оценки в '{part}' для ученика {fio}")
        else:
            print(f"Не удалось распознать предмет: '{part}'")

    if class_name not in students_data:
        students_data[class_name] = []

    students_data[class_name].append({
        'fio': fio,
        'objects': subjects_data
    })

print("\nДанные загружены:")
for cls, students in students_data.items():
    print(f"Класс {cls}: {len(students)} учеников")

excellent_students = {}

for class_name, students in students_data.items():
    best_student = None
    best_avg = 0

    for student in students:
        all_grades = []
        for grades in student['objects'].values():
            all_grades.extend(grades)

        avg = sum(all_grades) / len(all_grades) if all_grades else 0

        if avg > best_avg:
            best_avg = avg
            best_student = student['fio']

    excellent_students[class_name] = {
        'fio': best_student,
        'average': round(best_avg, 2)
    }

with open('excellent_students.txt', 'w', encoding='utf-8') as file:
    for class_name, info in excellent_students.items():
        line = f"{class_name}: {info['fio']} (средний балл: {info['average']})\n"
        file.write(line)

print("\nГотово! Результат записан в 'excellent_students.txt'")

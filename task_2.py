import os

students = {}

if not os.path.exists("resource/students.txt"):
    with open("resource/students.txt", "w", encoding="utf-8") as f:
        f.write("Иванов Иван:5,4,3,5\n")
        f.write("Петров Петр:4,3,4,4\n")
        f.write("Сидорова Мария:5,5,5,5\n")

with open("resource/students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, grades = line.strip().split(":")
        grades = list(map(int, grades.split(",")))
        avg = sum(grades) / len(grades)
        students[name] = avg

with open("resource/result.txt", "w", encoding="utf-8") as file:
    for name, avg in students.items():
        if avg > 4:
            file.write(f"{name}: {avg:.2f}\n")

best_student = max(students, key=students.get)
print("Лучший студент:", best_student, f"{students[best_student]:.2f}")
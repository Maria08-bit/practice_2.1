students = {}

try:
    with open("resource/students.txt", "r", encoding="utf-8") as file:
        for line in file:
            try:
                name, grades = line.strip().split(":")
                grades = list(map(int, grades.split(",")))
                avg = sum(grades) / len(grades)
                students[name] = avg
            except ValueError:
                print("Ошибка: неправильный формат строки в файле students.txt ->", line.strip())

except FileNotFoundError:
    print("Ошибка: файл students.txt не найден.")

except Exception as e:
    print("Ошибка: не удалось прочитать файл students.txt.", e)


try:
    with open("result.txt", "w", encoding="utf-8") as file:
        for name, avg in students.items():
            if avg > 4:
                file.write(f"{name}: {avg}\n")

except Exception as e:
    print("Ошибка: не удалось записать данные в файл result.txt.", e)


try:
    best_student = max(students, key=students.get)
    print("Лучший студент:", best_student, students[best_student])
except ValueError:
    print("Ошибка: список студентов пуст, невозможно определить лучшего студента.")
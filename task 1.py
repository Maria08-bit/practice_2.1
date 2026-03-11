try:
    with open("text.txt", "w", encoding="utf-8") as file:
        file.write("лол\n")
        file.write("кеек\n")
        file.write("Неупокоев Андрей Евгеньевич\n")
        file.write("питон\n")
        file.write("файл энштейна\n")

except Exception as e:
    print("Ошибка: не удалось записать данные в файл.", e)

try:
    with open("text.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

except FileNotFoundError:
    print("Ошибка: файл text.txt не найден.")
    lines = []

except Exception as e:
    print("Ошибка: не удалось прочитать файл.", e)
    lines = []

line_count = len(lines)

word_count = 0
for line in lines:
    words = line.split()
    word_count += len(words)

try:
    longest_line = max(lines, key=len)
except ValueError:
    longest_line = ""
    print("Ошибка: файл пустой, невозможно определить самую длинную строку.")

print("Количество строк:", line_count)
print("Количество слов:", word_count)

if longest_line:
    print("Самая длинная строка:", longest_line)
else:
    print("Самая длинная строка: отсутствует")
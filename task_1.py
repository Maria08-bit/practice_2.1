import os

filename = "resource/text.txt"


if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("лол\n")
        file.write("кеек\n")
        file.write("Неупокоев Андрей Евгеньевич\n")
        file.write("питон\n")
        file.write("файл энштейна\n")



with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()


line_count = len(lines)


word_count = 0
for line in lines:
    words = line.split()
    word_count += len(words)


longest_line = max(lines, key=len)

print("Количество строк:", line_count)
print("Количество слов:", word_count)
print("Самая длинная строка:", longest_line)
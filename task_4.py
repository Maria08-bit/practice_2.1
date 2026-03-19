from datetime import datetime

try:
    with open("resource/calculator.log", "r") as file:
        lines = file.readlines()
        print("Последние операции:")
        for line in lines[-5:]:
            print(line.strip())
except:
    pass

while True:
    try:
        a = float(input("Введите первое число: "))
        break
    except ValueError:
        print("Ошибка: введите только цифры")

while True:
    try:
        b = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка: введите только цифры")

while True:
    op = input("Введите операцию (+ - * /): ")
    if op in ["+", "-", "*", "/"]:
        break
    else:
        print("Ошибка: введите допустимую операцию (+, -, *, /)")

result = None

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        print("Ошибка: деление на ноль")
        result = "ошибка"
    else:
        result = a / b

print("Результат:", result)

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("resource/calculator.log", "a") as file:
    file.write(f"[{time}] {a} {op} {b} = {result}\n")

while True:
    clear = input("Очистить лог? (да/нет): ").lower()
    if clear in ["да", "нет"]:
        break
    else:
        print("Ошибка: введите да или нет")

if clear == "да":
    open("resource/calculator.log", "w").close()
    print("Лог очищен")
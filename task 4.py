from datetime import datetime

try:
    with open("calculator.log", "r") as f:
        lines = f.readlines()
        print("Последние 5 операций:")
        for line in lines[-5:]:
            print(line.strip())
except Exception:
    print("Ошибка: лог-файл пуст или не существует")

while True:
    try:
        a = float(input("Введите первое число: "))
        break
    except ValueError:
        print("Ошибка: нужно вводить только числа. Попробуйте снова.")

while True:
    try:
        b = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка: нужно вводить только числа. Попробуйте снова.")

while True:
    op = input("Введите операцию (+ - * /): ")

    if op == "+":
        result = a + b
        break
    elif op == "-":
        result = a - b
        break
    elif op == "*":
        result = a * b
        break
    elif op == "/":
        if b == 0:
            print("Ошибка: деление на ноль! Попробуйте другую операцию.")
        else:
            result = a / b
            break
    else:
        print("Ошибка: неверная операция! Попробуйте снова (+, -, *, /).")

if result is not None:

    a_str = f"{a:.1f}"
    b_str = f"{b:.1f}"
    result_str = f"{result:.1f}"

    print(f"Результат: {a_str} {op} {b_str} = {result_str}")

    try:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("calculator.log", "a") as f:
            f.write(f"[{time}] {a_str} {op} {b_str} = {result_str}\n")
    except Exception as e:
        print("Ошибка: не удалось записать операцию в лог.", e)

    clear = input("Очистить ? (да/нет): ")
    if clear.lower() == "да":
        try:
            open("calculator.log", "w").close()
            print("Лог очищен!")
        except Exception as e:
            print("Ошибка: не удалось очистить лог-файл.", e)
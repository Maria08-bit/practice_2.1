import csv

products = []

try:
    with open("resource/products.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and any(row):
                products.append(row)
except Exception as e:
    print("Ошибка: не удалось прочитать файл.", e)
    exit()

print("\nДобавление нового товара ")

while True:
    name = input("Введите название товара: ")
    if any(char.isdigit() for char in name):
        print("Ошибка: название товара не должно содержать цифры. Попробуйте снова.")
    elif name.strip() == "":
        print("Ошибка: название товара не может быть пустым. Попробуйте снова.")
    else:
        break

while True:
    try:
        price = int(input("Введите цену: "))
        if price <= 0:
            print("Ошибка: цена должна быть положительным числом. Попробуйте снова.")
        else:
            break
    except ValueError:
        print("Ошибка: цена должна быть числом. Попробуйте снова.")

while True:
    try:
        qty = int(input("Введите количество: "))
        if qty <= 0:
            print("Ошибка: количество должно быть положительным числом. Попробуйте снова.")
        else:
            break
    except ValueError:
        print("Ошибка: количество должно быть числом. Попробуйте снова.")

products.append([name, price, qty])
print("Товар успешно добавлен!")

print("\nПоиск товара ")
search = input("Введите товар для поиска: ").lower()

found = False
for p in products:
    try:
        if p and p[0].lower() == search:
            print("Найден товар:", p)
            found = True
    except (IndexError, AttributeError):
        print("Ошибка: некорректные данные о товаре.")

if not found:
    print("Товар не найден")

print("\nРасчет стоимости ")
total = 0
error_count = 0
for p in products:
    try:
        if len(p) >= 3:
            total += int(p[1]) * int(p[2])
        else:
            error_count += 1
            print("Ошибка: некорректные данные у товара:", p)
    except (IndexError, ValueError):
        error_count += 1
        print("Ошибка: некорректные числовые данные у товара:", p)

print("Общая стоимость всех товаров:", total)
if error_count > 0:
    print(f"Обнаружено {error_count} товаров с некорректными данными")

print("\nСохранение ")
try:
    with open("resource/products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(products)
    print("Данные успешно сохранены в файл products.csv")
except Exception as e:
    print("Ошибка: не удалось записать данные в файл.", e)
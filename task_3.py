import csv
import os

products = []

if os.path.exists("resource/products.csv"):
    with open("resource/products.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                products.append(row)
else:
    products = [
        ["Яблоки", "100", "50"],
        ["Бананы", "80", "30"],
        ["Молоко", "120", "20"],
        ["Хлеб", "40", "100"]
    ]


while True:
    name = input("Введите название товара (только буквы): ")
    if name.replace(" ", "").isalpha():
        break
    else:
        print("Ошибка: название должно содержать только буквы")

while True:
    price = input("Введите цену (только цифры): ")
    if price.isdigit():
        break
    else:
        print("Ошибка: цена должна содержать только цифры")

while True:
    qty = input("Введите количество (только цифры): ")
    if qty.isdigit():
        break
    else:
        print("Ошибка: количество должно содержать только цифры")

products.append([name, price, qty])


while True:
    search = input("Введите товар для поиска (только буквы): ")
    if search.replace(" ", "").isalpha():
        break
    else:
        print("Ошибка: поиск должен содержать только буквы")

found = False
for p in products:
    if p[0].lower() == search.lower():
        print("Найден товар:", p)
        found = True
if not found:
    print("Товар не найден")


total = 0
for p in products:
    total += int(p[1]) * int(p[2])

print("Общая стоимость:", total)


with open("resource/products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(products)
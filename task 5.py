import json

FILE = "library.json"

initial_books = [
    {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": 1867, "available": True},
    {"id": 2, "title": "Преступление и наказание", "author": "Достоевский", "year": 1866, "available": False}
]

def save_books():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

def load_books():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(initial_books, f, indent=4, ensure_ascii=False)
        return initial_books.copy()

def show_books():
    print("\nСписок книг:")
    for b in books:
        status = "Доступна" if b.get("available", True) else "Выдана"
        print(f"{b['id']}. {b['title']} - {b['author']} ({b['year']}) - {status}")

def add_book():
    title = input("Название: ")
    author = input("Автор: ")
    try:
        year = int(input("Год: "))
    except ValueError:
        print("Ошибка: год должен быть числом")
        return
    new_id = max([b["id"] for b in books], default=0) + 1
    book = {"id": new_id, "title": title, "author": author, "year": year, "available": True}
    books.append(book)
    save_books()
    print("Книга добавлена!")

def search_books():
    text = input("Введите название или автора: ").lower()
    found = [b for b in books if text in b["title"].lower() or text in b["author"].lower()]
    if found:
        for b in found:
            status = "Доступна" if b.get("available", True) else "Выдана"
            print(f"{b['id']}. {b['title']} - {b['author']} ({b['year']}) - {status}")
    else:
        print("Ничего не найдено")

def toggle_status():
    show_books()
    try:
        id_ = int(input("ID книги для изменения статуса: "))
        for b in books:
            if b["id"] == id_:
                b["available"] = not b.get("available", True)
                status = "доступна" if b["available"] else "выдана"
                print(f"Статус изменен: книга теперь {status}")
                save_books()
                return
        print("Книга с таким ID не найдена")
    except ValueError:
        print("Ошибка: введите число")

def delete_book():
    show_books()
    try:
        id_ = int(input("ID книги для удаления: "))
        for i, b in enumerate(books):
            if b["id"] == id_:
                books.pop(i)
                save_books()
                print("Книга удалена")
                return
        print("Книга с таким ID не найдена")
    except ValueError:
        print("Ошибка: введите число")

def export_available():
    count = 0
    with open("available_books.txt", "w", encoding="utf-8") as f:
        for b in books:
            if b.get("available", True):
                f.write(f"{b['title']} - {b['author']} ({b['year']})\n")
                count += 1
    print(f"Экспортировано {count} книг в файл available_books.txt")

books = load_books()

while True:
    print("\n" + "="*30)
    print("БИБЛИОТЕКА")
    print("="*30)
    print("1. Показать все книги\n2. Поиск\n3. Добавить книгу\n4. Изменить статус\n5. Удалить книгу\n6. Экспорт доступных\n0. Выход")
    choice = input("Выбор: ")

    if choice == "1": show_books()
    elif choice == "2": search_books()
    elif choice == "3": add_book()
    elif choice == "4": toggle_status()
    elif choice == "5": delete_book()
    elif choice == "6": export_available()
    elif choice == "0":
        print("До свидания!")
        break
    else:
        print("Неверный выбор")
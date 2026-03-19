import json

FILE = "resource/library.json"

try:
    with open(FILE, "r", encoding="utf-8") as f:
        books = json.load(f)
    if not isinstance(books, list):
        books = []
except:
    books = []


def save():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)


def show_books():
    if not books:
        print("Список книг пуст")
        return
    for b in books:
        if isinstance(b, dict):
            status = "доступна" if b.get("available") else "выдана"
            print(
                f"{b.get('id', '?')}. {b.get('title', '?')} - {b.get('author', '?')} ({b.get('year', '?')}) - {status}")


def add_book():
    title = input("Название: ").strip()
    if not title:
        print("Ошибка: название не может быть пустым")
        return

    while True:
        author = input("Автор: ").strip()
        if not author:
            print("Ошибка: автор не может быть пустым")
            continue
        if author.replace(" ", "").isalpha():
            break
        else:
            print("Ошибка: автор должен содержать только буквы")

    while True:
        year = input("Год издания: ").strip()
        if not year:
            print("Ошибка: год не может быть пустым")
            continue
        if year.isdigit():
            break
        else:
            print("Ошибка: год должен содержать только цифры")

    new_id = 1
    for b in books:
        if isinstance(b, dict) and b.get("id", 0) >= new_id:
            new_id = b["id"] + 1

    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": int(year),
        "available": True
    }
    books.append(book)
    save()
    print("Книга добавлена")


def search():
    text = input("Введите название или автора: ").strip()
    if not text:
        print("Ошибка: введите текст для поиска")
        return

    found = False
    for b in books:
        if isinstance(b, dict) and (
                text.lower() in b.get("title", "").lower() or text.lower() in b.get("author", "").lower()):
            status = "доступна" if b.get("available") else "выдана"
            print(
                f"{b.get('id', '?')}. {b.get('title', '?')} - {b.get('author', '?')} ({b.get('year', '?')}) - {status}")
            found = True
    if not found:
        print("Ничего не найдено")


def change_status():
    try:
        id = int(input("ID книги: "))
    except ValueError:
        print("Ошибка: ID должен быть числом")
        return

    for b in books:
        if isinstance(b, dict) and b.get("id") == id:
            b["available"] = not b.get("available", True)
            save()
            status = "доступна" if b["available"] else "выдана"
            print(f"Статус изменен на: {status}")
            return
    print("Ошибка: книга с таким ID не найдена")


def delete_book():
    try:
        id = int(input("ID книги: "))
    except ValueError:
        print("Ошибка: ID должен быть числом")
        return

    global books
    new_books = [b for b in books if isinstance(b, dict) and b.get("id") != id]
    if len(new_books) == len(books):
        print("Ошибка: книга с таким ID не найдена")
        return

    books = new_books
    save()
    print("Книга удалена")


def export_available():
    try:
        with open("resource/available_books.txt", "w", encoding="utf-8") as f:
            count = 0
            for b in books:
                if isinstance(b, dict) and b.get("available"):
                    f.write(f"{b.get('title', '?')} - {b.get('author', '?')} ({b.get('year', '?')})\n")
                    count += 1
        print(f"Экспортировано книг: {count}")
    except:
        print("Ошибка: не удалось создать файл экспорта")


while True:
    print("\n1. Показать книги")
    print("2. Поиск")
    print("3. Добавить")
    print("4. Изменить статус")
    print("5. Удалить")
    print("6. Экспорт доступных")
    print("0. Выход")

    choice = input("Выбор: ").strip()

    if choice == "1":
        show_books()
    elif choice == "2":
        search()
    elif choice == "3":
        add_book()
    elif choice == "4":
        change_status()
    elif choice == "5":
        delete_book()
    elif choice == "6":
        export_available()
    elif choice == "0":
        break
    else:
        print("Ошибка: введите число от 0 до 6")
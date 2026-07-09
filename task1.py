book_profile = {
    "title": "Основи програмування",
    "author": "Іван Петренко",
    "year": 2023,
    "publisher_info": {
        "name": "Наукова думка",
        "city": "Київ"
    }
}

print(f"Книга «{book_profile["title"]}» автора {book_profile["author"]} була видана у місті {book_profile["publisher_info"]["city"]}.")
if book_profile["year"] is not None:
    print(f"Рік видання {book_profile["year"]}")
else:
    print("Рік видання невідомий")
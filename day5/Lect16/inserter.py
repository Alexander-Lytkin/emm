import sqlite3


conn = sqlite3.connect("data.db")
cur = conn.cursor()

# Одна книга для добавления
one_book = ("HP:2", "J.Rawling")
# Набор книг для добавления
many_books = [
    ("LOTR:1", "J.J.Talkin"),
    ("LOTR:2", "J.J.Talkin"),
    ("LOTR:3", "J.J.Talkin"),
    ] * 50

# '?' - placeholder - место, куда мы подставим данные в ходе выполнения запроса
insert_query = "INSERT INTO books (id, title, author) VALUES(NULL, ?, ?)"
# Способ добавления одной книги
cur.execute(insert_query, one_book)
# Способ добавления нескольких книг
# for book in many_books:
#     cur.execute(insert_query, book)
#     conn.commit()
cur.executemany(insert_query, many_books)
# Сохраняем состояния бд
conn.commit()
# Закрываем содеинение
conn.close()
"""
Третий вариант хранения книг.
1) Создадим заименованный набор полей - структура
"""

class Book:
    title = ""
    author = ""
    year_pub = 0
    pages = 0

b1 = Book() # Это представитель структуры  Book
b1.title = "LOTR:1"
b1.author = "J.J.Tolkin"
b1.year_pub = 1968
b1.pages = 783



b2 = Book()# Это представитель структуры Book
b2.title = "LOTR:2"
b2.author = "J.J.Tolkin"
b2.year_pub = 1975
b2.pages = 890

b3 = Book()# Это представитель структуры Book

books = [b1, b2, b3] # <---- Вот теперь мы храним список КНИГ!!!!!!!

for book in books:
    print(book.title, book.year_pub)

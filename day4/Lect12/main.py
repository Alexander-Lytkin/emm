class Book:
    tablename = "books" # Название таблицы в бд

    def __init__(self, title:str, author:str):
        self.__title = title
        self.__author = author
        

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, new_title:str):
        self.__title = new_title

    @classmethod
    def build_empty_book(cls):
        return cls(title="DEFAULT", author="DEFAULT")

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author:str):
        self.__author = new_author

    def __str__(self):
        return f"Book: T:{self.__title}, A:{self.__author}"

class GiftBook(Book):
    tablename = "gift_books"



b = Book(title="LOTR:1", author="J.J. Tolkin")
gift_book = GiftBook(title="Gifted :LOTR:1", author="J.J.Tolkin")

print(b, "will dumped to database table:", b.tablename)
print("All obj of class Book will dumped to:", Book.tablename)
b.build_empty_book() # Классовый метод можно вызвать у объекта
Book.build_empty_book() # Классовый метод можно вызвать и у класса

print(gift_book, "will dumped to database table:", gift_book.tablename)
print("All obj of class GiftBook will dumped to:", GiftBook.tablename)

b = Book("", "")
b.tablename = "new books"
print(b.tablename)
print(Book.tablename)

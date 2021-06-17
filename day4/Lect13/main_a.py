class Book:

    def __init__(self, title:str= "", author:str=""):
        print(f"__init__ for new book")
        self.title = title
        self.author = author
        

    def __str__(self):
        return f"Book:<{self.title}, {self.author}>"

    def __del__(self):
        print(f"__del__ for {self}")

b = Book("1", "1")
b1 = Book("2", "2")

for i in range(1, 100):
    if i == 50:
        del b1
    b.title = str(i)
1/0


class Book:
    OBJ_COUNTER = 0

    def __new__(cls):
        """
        Возвращает ту самую дефолтную болванку,
        на которую будут нанизываться атрибуты
        в методе __init__
        """
        cls.OBJ_COUNTER += 1
        obj = super().__new__(cls) #object() # Дефолтный объект в галактике
        return obj


    def __init__(self, title:str= "", author:str=""):
        self.title = title
        self.author = author
        

    def __str__(self):
        return f"Book:<{self.title}, {self.author}>"
for i in range(1, 100):
    b = Book()
    if i % 10 == 0:
        print(Book.OBJ_COUNTER)

# for i in range(1, 100):
b = Book() # a = Book.__new__() -> Book.__init__(a, title, author) -> a
print(b)
    # if i % 10 == 0:
    #     print(Book.OBJ_COUNTER)
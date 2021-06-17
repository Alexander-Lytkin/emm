## Лекция 12. Классы. Завершающие слова

### Шаг 0. Проблемы СП
* 1) ***Целостность*** (проблема целостности) - ни что не мешает оторвать структуру от ее обработчиков и разместить их в разных местах.
* 2) ***Усовершенствование*** существующей код-базы очень дорогое.
* 3) ***Создание ПО на основе*** уже существующего кода - практически невозможно.
* 4) ***Полная доступность*** состояния для последующих его модификаций.

### Дополнительный источник
* https://refactoring.guru/ru
* Изучайте **паттерны** - это достаточно строгие и полезные шаблоны при решении типичных задачек.

### Шаг 1. Какие бывают атрибуты и методы?
* ***Атрибуты*** - бывают объектные (instance attributes) и классовые атрибуты (class attributes) и статичные атрибуты (static attribute)
* ***Методы*** - объектные (instance method), классовые (class method) и статичные (static method).

### Шаг 2. Instance method\atributes
* Объектные атрибуты и методы - это состояния и поведения, завязанные конкретно на каком-либо объекте!
```
class Book:
    def __init__(self, title:str, author:str):
        self.__title = title
        self.__author = author
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, new_title:str):
        self.__title = new_title


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author:str):
        self.__author = new_author

    def __str__(self):
        return f"Book: T:{self.__title}, A:{self.__author}"

b = Book(title="LOTR:1", author="J.J. Tolkin")
print(b.author)
b.title = "LOTR:2"
print(b)
```

### Шаг 3. Class method\atributes
* Классовые методы и атрибуты - это такие состояния и поведения, которые завязаны на КЛАССЕ, А не на каких-то конкретных объектах.
* Для того, чтобы пометить метод как классовый - нужно:
```
@classmethod
def build_empty_book(cls):
    return cls(title="DEFAULT", author="DEFAULT")
```
* Теперь полный пример:
```
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
```

* Более менее полезный пример
```
class FileManager:
    READ_MODE = "r"
    WRITE_MODE = "w"
    ENCODING = "utf-8"
    DEFAULT_INPUT = "input.txt"
    DEFAULT_OUTPUT = "output.txt"
    
    def __init__(self, input_path:str = "input.txt", output_path:str= "output.txt"):
        self.input_path = input_path
        self.output_path = output_path
        self.input_handler = None
        self.output_handler = None

    @classmethod
    def creator(cls):
        open(cls.DEFAULT_INPUT, cls.WRITE_MODE)

    def __enter__(self):
        self.input_handler = open(self.input_path, self.READ_MODE, encoding=self.ENCODING)
        self.output_handler = open(self.output_path, self.WRITE_MODE, encoding=self.ENCODING)
        return (self.input_handler, self.output_handler)

    def __exit__(self, *args):
        self.output_handler.close()
        self.input_handler.close()

FileManager.creator() 
with FileManager(input_path="input.txt", output_path="output.txt") as handlers:
    inp, outp = handlers

print("ALLES")
    
    
```

### Шаг 4. Static method
* Статичные методы - это методы которые не зависит ни от объект и ни от класса!
```
class User:
    tablename = "Users"
    def __init__(self, login:str, password_hash:str):
        self.login = login
        self.password_hash = password_hash

    def __str__(self):
        return f"User:<Login:{self.login}, PasswordHash:{self.password_hash}>"

    @staticmethod
    def passw_ecnoder(password:str) -> str:
        """
        Шифрование пароля password
        """
        return password[::-1] * 5 + password[::-2] * 3 + password[3:]

pswd = User.passw_ecnoder(
    password = input()
)

u = User(login="admin", password_hash=pswd)
print(u)
```


### Резюме
* Использование instance method/attributes накладывает одно ограничение - методы (атрибуты) обязаны при себе иметь ```self```!
    * Через объектные (instance) методы можно получить доступ к объектным атрибутам/методам + классовым атрибутам/методам + статичным методам
    * Через классовые методы можно получить доступ к классовым атрибутам/методам + статичным методам
    * Через static методы можно получить доступ НИ К ЧЕМУ (<= 3.8.0). В новых версиях позволяется дергать классовые атрибуты и методы через имя класса
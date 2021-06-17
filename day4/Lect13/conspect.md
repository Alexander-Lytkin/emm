### Лекция 13. Классы. Завершение

### Шаг 0. Простая задача
* Научимся узнавать сколько объектов класса создано в какой-то момент времени.
```
class Book:
    OBJ_COUNTER = 0

    def __init__(self, title:str= "", author:str=""):
        self.title = title
        self.author = author
        self.count()

    @classmethod
    def count(cls):
        cls.OBJ_COUNTER += 1

    def __str__(self):
        return f"Book:<{self.title}, {self.author}>"

for i in range(1, 100):
    b = Book()
    if i % 10 == 0:
        print(Book.OBJ_COUNTER)
```

### Шаг 1. Доделываем конструктор. Или появление __new__
* ```__init__``` - это объектный метод. По сути он насаживает бусины на нитку
* ```__new__``` - это классовый метод, создающий эту самую нитку!

```
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

```

* Конструктор - ```__new__``` + ```__init__```

### Шаг 2. Деструктор?
* ```Python``` - язык со сборщиком мусора.
* В python деструктор используется для каких-то сигнальных целей (или каких-то действий, которые нужно выполнить перед уничтожением объекта)
```
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


```

### Шаг 3. Isinstance
* ```isinstance(obj, class)``` - функция, которая отвечает на вопрос "Связан как нибудь объект ```obj``` с классом ```class```?
```
class A(str):
    def say(self):
        pass

class B(A):
    pass

class C(B):
    pass

a = A()
b = B()
c = C()

print("a is A", isinstance(a, A))
print("a is B",isinstance(a, B))
print("a is C",isinstance(a, C))

print("b is A", isinstance(b, A))
print("b is B", isinstance(b, B))
print("b is C", isinstance(b, C))

print("c is A", isinstance(c, A))
print("c is B", isinstance(c, B))
print("c is C", isinstance(c, C))

print("a is str", isinstance(a, str))
```

* ```issubclass(cls1, cls2)``` -  функция, которая отвечает на вопрос - является ли класс cls2 родительским (или прородительским в нескольких ступенях) по отношению к классу cls1?
## Лекция 11. ООП. Наследование.

### Шаг 0. Наследование - это ...
* ***Наследование*** - это процесс переноса  свойств/материальных вещей от одного представителя к другому.  Чаще всего этих представителей объединяет некое подобие родственной связи. Передающий конец росдтвенной связи - чаще всего именуют ***родительским*** субъектом, а принимающий - ***дочерний*** субъекту. Дочерний субъект сам определеяет как распоряжаться своим наследством.

* ***Наследование (ПО)*** - это процесс создания чего-то нового (какой-то новой кодовой базы) , на основе уже имеющейся.

### Шаг 1. Реализация
* Простейшая реализация
```
"""
Есть персона - это кмакой-то человек
Хотим на основе человека построить школьника
* Проблема 1 - если когда-нибудь нам потребуется внести изменения в Person
    то в школьнике их придется делать руками! (Дублирование кода)
"""

class Person:
    name = "####"
    lastname = "####"
    age = None


class Schoolar(Person):
    letter = "Z"
    wake_up_time = "07:00"

def main():
    """
    """
    sc = Schoolar()
    print(sc.name, sc.lastname, sc.letter)
    
if __name__ == "__main__":
    main()
```

* В данном контексте есть 2 вида классов , которые реализуют механзим наследования.
    * Класс ```Person``` - называют родительским классом (базовым классом) (класс, ***ОТ*** которого наследуют)
    * Класс ```Schoolar``` - называют дочерним классом (класс, ***В*** который наследуют)


### Шаг 2. Реализация переноса методов
```
"""
Взаимное использование родительских методов
"""

class A:
    def say_a(self):
        print("a" * 10)


class B(A):
    def say_b(self):
        self.say_a()
        print("b" * 10)


def main():
    b = B()
    b.say_b()

if __name__ == "__main__":
    main()
```

* Использование ```super()```
```
"""
Взаимное использование родительских методов
"""

class A:
    def say(self):
        print("a" * 10)


class B(A):
    def say(self):
        #self.say() # Хотим вызвать родительский метод!
        #A.say(self) # Вариант официального выхова из любой точки галактики
        super().say() # super() - возвращает родительский объект!!!!
        print("b" * 10)


def main():
    b = B()
    b.say()

if __name__ == "__main__":
    main()
```

* Вызов родительских инициализаторов:
```
class Person:
    def __init__(self, name:str, age:int):
        print("Person __init__")
        self.name = name 
        self.age = age

    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}"

class Schoolar(Person):
    def __init__(self, name:str, age:int, letter:str, wakeup:str):
        print('Schoolar __init__')
        super().__init__(name, age)
        self.letter = letter
        self.wakeup = wakeup

    
    def __str__(self):
        return super().__str__() + f", Letter:{self.letter}, WakeUp: {self.wakeup}"

def main():
    sc = Schoolar("Bob", 14, 'd', '07:00')
    print(sc)
if __name__ == "__main__":
    main()
```

### Шаг 3. Наследование приватных атрибутов/методов
```
class A:
    __a = 10 # _A__a

class B(A):
    __b = 20

    def say_private(self):
        print(self.__b, self.__a)

b = B()
print(dir(b))
```

* Проблема наследования приватных атрибутов и методов, состоит в том, что интерпретатор внутри себя преобразует имена приватизирвоанных блоков по схеме ```__attr -> _ClassName__attr```.
* В обязательном порядке необходимо всегда реализовывать get/set методы, иначе дочерние классы никак не смогут работать с приватными полями/методами!

### Шаг 4. Нелинейное или множественное наследование
* У одного родителського класса может быть сколько угодно дочерних классов
* А у одного дочернего класса может быть несколько родителей!
```
class A:
    a = "a"

class B:
    b = "b"


class C(A,B):
    c = "c"
    
c = C()
print(dir(c))
```

#### Шаг 4.1 Ромбическое наследование
```
class A:
    a = "a"

class B(A):
    b = "b"


class C(A):
    c = "c"

class D(B,C):
    d = "d"
    
d = D()
print(dir(d))
```

* Теперь собственно проблема
```
class A:
    a = "a"
    def say(self):
        print(self.a)

class B(A):
    word = "B"


class C(A):
    word = "C"

class D(B,C):
    pass
    
d = D()
print(d.a)
d.say()
print(d.word)
```
* Наследование в питоне приоритетное - самый высокий приоритет у класса, расположенного ***левее*** в цепочке наследования!
* При проходе по цепочке наследований - интерпретатор "топит" вглубь класса самые первые в цепи. Таким образом, атрибуты/методы самых первых классов оказываются для интерпретатора наиболее актуальными в контесте переопределения

### Шаг 4.2 Обращение к родительским методам, если родителя 2
```
class A:
    word = "from a"
    def say(self):
        print(self.word)


class B(A):
    word = "from b"
    def talk(self):
        print("B class talk method!")

class C(A):
    word = "from c"
    def talk(self):
        self.say()
        print("C class talk method after calling inherit method say()")


class D(B, C):
    def talk(self):
        B.talk(self) # Вызывает метод talk() у самог оприоритетного родителя!
        print("D class method talk!")
        C.talk(self) # Теперь вызову метод talk() класса С


d = D()
d.talk()
```

### Шаг 5. Абстрактный класс. Как его реализовать в питоне?
* Чаще всего, абстрактный класс, это класс от которого наследуются и пытаются переопределить все имеющиеся у него методы
* Объекты абстрактного класса создавать запрещено!

```
class AbstactFigure:
    def __init__(self):
        raise NotImplemented()

    def perimeter(self):
        raise NotImplemented()

    def area(self):
        raise NotImplemented()

    def __str__(self):
        raise NotImplemented()

class Rectangle(AbstactFigure):
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2*(self.a + self.b)
    def area(self):
        return self.a * self.b
        
    def __str__(self):
        return f"Rect <a:{self.a}, b:{self.b}>"

def main():
    r = Rectangle(a=10, b = 20)
    print(r.perimeter(), r.area())
    print(r)
if __name__ == "__main__":
    main()
```

### Шаг 6. @property
* Писать гетеры и сетеры вручную каждый раз дико утомительно!
* К тому же - их вызов может быть не столь уж и очевидным
* Как упростить себе задачу?
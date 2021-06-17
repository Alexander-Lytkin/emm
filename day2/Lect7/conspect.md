### Лекция 7. Классы. Перегрузка и переопределение

***Рассмотрим простую задачу***. У нас есть какой-то пользовательский класс (например ```Backpack```). Мы хотим научиться с этим рюкзаком выполнять базовые математические операции (сравнивать рюкзаки, складывать и т.д. и т.п.)

### Шаг 0. Сам Backpack
```
class Backpack:
    """
    Класс, описывающий рюкзак
    """
    def __init__(self, weight:int=0, volume:int=0):
        self.weight = weight
        self.volume = volume

    def __str__(self):
        return f"Backpack<W:{self.weight} kg, V:{self.volume} l>"
```

### Шаг 1. Функция dir()
* ```dir(<obj>)``` - возвращает список всех атрибутов и методов данного объекта!
* Вызов 
```
bp = Backpack(weight=10, volume=48)
print(dir(bp))
```
* Ответ - все доступные атрибуты и методы
```
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'volume', 'weight']
```

* Вывод - оказывается, когда создаем класс (пользовательский) - в него автоматически уже добавляется ряд методов и атрибутов!

### Шаг 2. Переопределение - это ...
```
"""
Модуль, содержащий игры с классом Рюкзак
"""
class Backpack:
    """
    Класс, описывающий рюкзак
    """
    def __init__(self, weight:int=0, volume:int=0):
        self.weight = weight
        self.volume = volume

    def __str__(self):
        return f"Backpack<W:{self.weight} kg, V:{self.volume} l>"

    def __str__(self):
        return "Backpack"

```

* ***Переопределение*** - это процесс подмены функционала под существующее имя. В примере выше, переопределеяем метод ```__str__```

### Шаг 3. Частые переопределения
* Набор методов, которые вы чаще всего будете переопределять:
    * ```__init__``` - инициализатор объекта (назначает атрибутам значения, по умочланию не делает ничего)
    * ```__str__``` - строковое представление вашего объекта (по умолчанию отдает строку вида```class_name object at object_hash```)
    * ```__repr__``` - объектная репрезентация общего вида

### Шаг 4. Специфические переопределения
* Сравнение на равенство ```__eq__``` - возвращает True, если объекты равны, False - в остальных случаях
```
class Backpack:
    """
    Класс, описывающий рюкзак
    """
    def __init__(self, weight:int=0, volume:int=0):
        self.weight = weight
        self.volume = volume

    def __eq__(self, other):
        return (self.weight == other.weight) and (self.volume == other.volume)

    def __str__(self):
        return f"Backpack<W:{self.weight} kg, V:{self.volume} l>"

```

* Автоматически, при реализации метода ```__eq__``` мы также можем сравнивать на ***!=***.

* Если нужно явное ***!=*** то добавляем метод ```__ne__``` (not equal) 
```
"""
Модуль, содержащий игры с классом Рюкзак
"""
class Backpack:
    """
    Класс, описывающий рюкзак
    """
    def __init__(self, weight:int=0, volume:int=0):
        self.weight = weight
        self.volume = volume

    def __eq__(self, other):
        print("__eq__ works")
        return (self.weight == other.weight) and (self.volume == other.volume)

    def __ne__(self, other):
        print("__ne__ works")
        return not self.__eq__(other)

    def __str__(self):
        return f"Backpack<W:{self.weight} kg, V:{self.volume} l>"

```

* Сравнение (строгое) на больше выполняется при помощи метода ```__gt__``` , сравнение на меньше - через ```__lt__```. В случае, если ```__gt__``` определен, второй метод уже необязателен.

* Сравнение (не строгое) выполняется при помощи метода ```__ge__``` или ```__le__```.
```
"""
Модуль, содержащий игры с классом Рюкзак
"""
from typing import Type


class Backpack:
    """
    Класс, описывающий рюкзак
    """
    def __init__(self, weight:int=0, volume:int=0):
        self.weight = weight
        self.volume = volume

    def __eq__(self, other):
        return (self.weight == other.weight) and (self.volume == other.volume)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.volume > other.volume

    def __lt__(self, other):
        return self.volume < other.volume
    
    def __ge__(self, other):
        return self.volume >= other.volume

    def __le__(self, other):
        return self.volume <= other.volume

    def __str__(self):
        return f"Backpack<W:{self.weight} kg, V:{self.volume} l>"
```

### Шаг 4. Перегрузка - это ...
* ***Перегрузка*** - это доопределение функционала пользовательского класса, на случай использования его объектов с другими операндами,функциями, методами. В нашем случае, попробуем перегрузить операцию ```+```

* ```__add__``` - это метод, который будет вызываться у объектов, в случае их сложения!
```
"""
Модуль, содержащий игры с классом Рюкзак
"""
from typing import Type


class Backpack:
    """
    Класс, описывающий рюкзак
    """
    def __init__(self, weight:int=0, volume:int=0):
        self.weight = weight
        self.volume = volume

    def __eq__(self, other):
        return (self.weight == other.weight) and (self.volume == other.volume)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.volume > other.volume

    def __lt__(self, other):
        return self.volume < other.volume
    
    def __ge__(self, other):
        return self.volume >= other.volume

    def __le__(self, other):
        return self.volume <= other.volume

    def __add__(self, other):
        return Backpack(
            weight=self.weight + other.weight, 
            volume=self.volume + other.volume
            )

    def __str__(self):
        return f"Backpack<W:{self.weight} kg, V:{self.volume} l>"

```

### Шаг 5. Контекстный менеджер
```
"""
Модуль, содержащий игры с классом Рюкзак
"""
from typing import Type


class Backpack:
    """
    Класс, описывающий рюкзак
    """
    def __init__(self, weight:int=0, volume:int=0):
        self.weight = weight
        self.volume = volume

    def __eq__(self, other):
        return (self.weight == other.weight) and (self.volume == other.volume)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.volume > other.volume

    def __lt__(self, other):
        return self.volume < other.volume
    
    def __ge__(self, other):
        return self.volume >= other.volume

    def __le__(self, other):
        return self.volume <= other.volume

    def __add__(self, other):
        return Backpack(
            weight=self.weight + other.weight, 
            volume=self.volume + other.volume
            )

    def __str__(self):
        return f"Backpack<W:{self.weight} kg, V:{self.volume} l>"

    def __enter__(self):
        print("__enter__ works")
        return self.weight * 100

    def __exit__(self, *args):
        print("__exit__ works")


def main():
    """
    Входная точка
    """
    bp_first = Backpack(weight=11, volume=61)
    bp_second = Backpack(weight=12, volume=60)
    with bp_first as value:
        print("Value:", value)



if __name__ == "__main__":
    main()
```

* Методы ```__exit__``` и ```__enter__``` - это методы, необходимые для работы вашего объекта с контекстным менеджером ```with```. Требуется наличие обоих методов!

* Пример копирования из одного файла в другой при помощи единого контекстного менеджера:
```
class FileManager:
    def __init__(self, input_path:str, output_path:str):
        self.input_path = input_path
        self.output_path = output_path
        self.input_handler = None
        self.output_handler = None

    def __enter__(self):
        self.output_handler = open(self.output_path, "w", encoding="utf-8")
        self.input_handler = open(self.input_path, "r", encoding="utf-8")
        return (self.input_handler, self.output_handler)

    def __exit__(self, *args):
        self.output_handler.close()
        self.input_handler.close()

    def __str__(self):
        return f"FM<Input:{self.input_path}, Output:{self.output_path}>"

def main():
    """
    Start
    """
    with FileManager("input.txt", "output.txt") as handlers:
        input_handler, output_handler = handlers
        output_handler.write(input_handler.read())
    

if __name__ == "__main__":
    main()

```

### Шаг 6. Атрибут __dict__
* Каждый объект имеет при себе атрибут ```__dict__``` - возвращает словарь, в котором все ключи - это имена атрибутов объекта, а значения - их прямые значения, назначенные инициализатором:
```
"""
Test module for person serialize
"""
import json


class Person:
    """
    Person description
    """
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        self.jeronimo = None

    def to_json(self):
        return self.__dict__

    def __str__(self):
        return f"Person<N:{self.name}, A:{self.age}>"

def main():
    """
    Start
    """
    person = Person("Bob", 23)
    result = json.dumps(person.to_json(), indent=4, sort_keys=True)
    print(result)
    
if __name__ == "__main__":
    main()
```
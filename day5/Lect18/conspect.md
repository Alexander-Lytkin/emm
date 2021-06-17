## Лекция 18. Модуль collections. Обзор

В языке встроено 5 стандартных коллекций:
    * list
    * dict
    * tuple
    * set
    * str

* Существует модуль ```collections```, внутри которого определены наборы высокоуровневых колелкций (комбинации низкоуровневых) для решениях наиболее част овстречающихся задач.


### Шаг 1. Задача подсчета частот
* Допустим есть какой-то набор элементов - нужно узнать, сколько раз в наборе встречается каждый элемент.
* Решение через базовые коллекции
```
words = ["alice", "bob", "alice", "bob", "bob", "bob", "a", "b", "a"]
counter = {}

for word in words:
    counter[word] = counter.get(word, 0) + 1 

print(counter)
```
* Решение через ```collections.Counter```
```
from collections import Counter

words = ["alice", "bob", "alice", "bob", "bob", "bob", "a", "b", "a"]
counter = Counter(words)

print(counter["bob"]) # можем обращаться по ключам, как у словаря
for k, v in counter.items(): # Поддерживает методы словарей
    print(k, v)

# Получение всех элементов
print(list(counter.elements()))
# Топ-3
counter  = Counter("hello world! hellol world")
print(counter.most_common(3))

```

* ```collections.Counter``` - гибридный объект списка/словаря, созданный для решения задачи частостного подсчета.

### Шаг 2. Отсутствие значения по умочланию у словарей
* В данном коде есть ошибка - обращение к несуществующему ключу! Приведет к выбсроку исключения.
```
words = {}
words["one"] = 1
words["two"] = 2
words["three"]
```
* Я бы хотел, чтобы в такой ситуации, аналогично многим другим ЯП, возвращалось бы значение по умолчанию.
```
from collections import defaultdict
words = defaultdict(int)

words["one"] = 1
words["two"] = 2
print(words["three"])

print(words)

```

* ```defaultdict``` - это гибрид словаря с нвоым конструктором, который способен выдавать значения по уомлчнаию для принятых типов!

### Шаг 3. Неупорядоченность словаря!
* Упорядоченность словаря с точки зрения порядка добавления элементов
```
d = {}
lst = []

pairs = [("a", 1), ('b', 10), ('c', 50), ('d', 150)]

for p in pairs:
    d[p[0]] = p[1]
    lst.append(p[0])

print(d)
print(lst)
```

* То же самое, но при помощи ```collections.OrderDict```
```
from collections import OrderedDict
pairs = [("a", 1), ('b', 10), ('c', 50), ('d', 150)]

od = OrderedDict()
for p in pairs:
    od[p[0]] = p[1]
    

print(od)
# Перетаскивание в конец
od.move_to_end('a', last=True)
print(od)

# Удалим первый добавленный элемент
od.popitem(last=False)
print(od)
```

### Шаг 4. Конкатенация словарей
* У вас есть 2 словаря
    * Первый словарь занимает ~ 1/2RAM (ex. MongoDB)
    * Второй словарь занимает ~ 1/2RAM (json)
* Задача - соединить их в один

* Решение при помощи ```ChainMap```
```
from collections import ChainMap

first = {"a" : 1, "b" : 2, "c" : 3}
second = {"d" : 4, "a" : 5, "f" : 6}

third = ChainMap(first, second)
third = third.new_child({"g" : 10, "h" : 200})
for k, v in third.items():
    print(k, v)

print(third)
print(third["d"])
```

* ```collections.ChainMap``` - обвзяка над основным свойством словарей - а конкретно - над их ссылочностью. По сути, ChainMap хранит под собой набор ссылок, по которым уже ориентируется, и имитирует деятельность словаря.

### Шаг 5. Небольшие структуры
* Иногда приходится описывать классы для объектов выполняющих вспомогательную роль.
    * После иниициализации объекта его никто не будет трогать
    * И от объекта требуется, чтобы у него был метод ```__str__```

* ```class Point```
```
class Point:
    """
    Point description
    """
    def __init__(self, x:int, y:int):
        self.x = x 
        self.y = y
    def __str__(self):
        return f"<Point X:{self.x} Y:{self.y}>"

p = Point(x =1, y=2)
print(p)
print(p.x, p.y)

```

* Все то же самое, но только через ```namedtuple```
```
NewPoint = namedtuple('NewPoint', ['x', 'y'])
np = NewPoint(1, 2)
print(np)
print(np.x, np.y)
print(np[0], np[1])
```

* ```namedtuple``` - это обвязка над кортежем, который имитирует поведение класса (кажется, что там ест ьметоды ```__init``` и ```__str__``` , а также набор нужных нам атрибутов!)
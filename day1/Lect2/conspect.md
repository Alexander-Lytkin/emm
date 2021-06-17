## Лекция 2. Начало

***Python*** - один из достаточно глубоких языков.

### Шаг 0. Параллельно нужно
* Теория Баз данных
* Алгоритмы и структуры данных
* Язык программирования 
* ОС (nix-like)

### Шаг 1. Как бороться с плохим кодом?
* Создадим модуль ```app.py```
```
def add(x, y):
    return x + y
def sub(x,y):
    return x - y
def mult(x,y):
    return x * y
def sq_add(x,y):
    return x**2 + y**2

a_num = int(input())
b_num = int(input())

result = add(a_num, b_num)*sub(a_num, b_num)/mult(a_num, b_num)
result += 1/sq_add(a_num, b_num)
print(result)
```

#### Шаг 1.1. Выделение  main() части
```
def add(x, y):
    return x + y
def sub(x,y):
    return x - y
def mult(x,y):
    return x * y
def sq_add(x,y):
    return x**2 + y**2

def main():
    a_num = int(input())
    b_num = int(input())

    result = add(a_num, b_num)*sub(a_num, b_num)/mult(a_num, b_num)
    result += 1/sq_add(a_num, b_num)
    print(result)

if __name__ == "__main__":
    main()
```

* ```__name__``` - это переменная, которая присутствует в каждом модуле. Она равна ```__main__``` если модуль вызывается напрямую ОС. В другом случае (если модуль импортируется), эта переменная равна значению пути импорта.

#### Шаг 1.2 Автоформатирование
* ```black```. Установка ```pip install black```
* Использование  ```python -m black app.py```
* В результате у нас получится:
```
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def sq_add(x, y):
    return x ** 2 + y ** 2


def main():
    a_num = int(input())
    b_num = int(input())
    result = add(a_num, b_num) * sub(a_num, b_num) / mult(a_num, b_num)
    result += 1 / sq_add(a_num, b_num)
    print(result)


if __name__ == "__main__":
    main()
```

#### Шаг 1.2 Документирование
```
"""
Этот модуль содержит набор учебных функций
"""

def add(x, y):
    """
    Функция возвращает результат арифметического сложения 
    параметров x и y
    """
    return x + y


def sub(x, y):
    """
    Функция возвращает результат арифметического вычитания 
    параметров x и y
    """
    return x - y


def mult(x, y):
    """
    Функция возвращает результат арифметического умножения
    параметров x и y
    """
    return x * y


def sq_add(x, y):
    """
    Функция возвращает результат суммы квадратов
    параметров x и y
    """
    return x ** 2 + y ** 2


def main():
    """
    Входная точка в приложение
    """
    a_num = int(input())
    b_num = int(input())
    result = add(a_num, b_num) * sub(a_num, b_num) / mult(a_num, b_num)
    result += 1 / sq_add(a_num, b_num)
    print(result)


if __name__ == "__main__":
    main()

```

* ```docformatter``` -  это инстурмент для форматирования строк документации.
```pip install docformatter```.  Запуск  ```python -m docformatter -i app.py```
```
"""Этот модуль содержит набор учебных функций."""


def add(x, y):
    """Функция возвращает результат арифметического сложения параметров x и
    y."""
    return x + y


def sub(x, y):
    """Функция возвращает результат арифметического вычитания параметров x и
    y."""
    return x - y


def mult(x, y):
    """Функция возвращает результат арифметического умножения параметров x и
    y."""
    return x * y


def sq_add(x, y):
    """Функция возвращает результат суммы квадратов параметров x и y."""
    return x ** 2 + y ** 2


def main():
    """Входная точка в приложение."""
    a_num = int(input())
    b_num = int(input())
    result = add(a_num, b_num) * sub(a_num, b_num) / mult(a_num, b_num)
    result += 1 / sq_add(a_num, b_num)
    print(result)


if __name__ == "__main__":
    main()

```

#### Шаг 1.3 Семантика
* ```pylint```. ```pip install pylint```.  Запуск ```python -m pylint app.py```
```
"""Этот модуль содержит набор учебных функций."""


def add(x_arg, y_arg):
    """Функция возвращает результат арифметического сложения параметров x_arg и
    y_arg."""
    return x_arg + y_arg


def sub(x_arg, y_arg):
    """Функция возвращает результат арифметического вычитания параметров x_arg и
    y_arg."""
    return x_arg - y_arg


def mult(x_arg, y_arg):
    """Функция возвращает результат арифметического умножения параметров x_arg и
    y_arg."""
    return x_arg * y_arg


def sq_add(x_arg, y_arg):
    """Функция возвращает результат суммы квадратов параметров x_arg и y_arg."""
    return x_arg ** 2 + y_arg ** 2


def main():
    """Входная точка в приложение."""
    a_num = int(input())
    b_num = int(input())
    result = add(a_num, b_num) * sub(a_num, b_num) / mult(a_num, b_num)
    result += 1 / sq_add(a_num, b_num)
    print(result)


if __name__ == "__main__":
    main()

```

#### Шаг 1.4 Аннотации
```
"""Этот модуль содержит набор учебных функций."""


def add(x_arg: int, y_arg: int) -> int:
    """Функция возвращает результат арифметического сложения параметров x_arg и
    y_arg."""
    return x_arg + y_arg


def sub(x_arg: int, y_arg: int) -> int:
    """Функция возвращает результат арифметического вычитания параметров x_arg
    и y_arg."""
    return x_arg - y_arg


def mult(x_arg: int, y_arg: int) -> int:
    """Функция возвращает результат арифметического умножения параметров x_arg
    и y_arg."""
    return x_arg * y_arg


def sq_add(x_arg: int, y_arg: int) -> int:
    """Функция возвращает результат суммы квадратов параметров x_arg и
    y_arg."""
    return x_arg ** 2 + y_arg ** 2


def main() -> None:
    """Входная точка в приложение."""
    a_num = int(input())
    b_num = int(input())
    result = add(a_num, b_num) * sub(a_num, b_num) / mult(a_num, b_num)
    result += 1 / sq_add(a_num, b_num)
    print(result)


if __name__ == "__main__":
    main()

```

* ***Аннотации*** - это тоже споосб документирования, только позволяет обозначить "желаемые параметры".
* ```pip install mypy```

### Шаг 2 . Резюме:
* Общая команда : ```python -m black app.py && python -m docformatter -i app.py && python -m pylint app.py && python -m mypy app.py```
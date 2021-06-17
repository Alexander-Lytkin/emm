### Лекция 9. ООП. Инкапсуляция.

***ООП (Объектно-Ориентированное программирование)*** - абстракция, инкапсуляция, полиморфизм и наследование.

### Шаг 0. Инкапсуляция - это ...

* ***Инкапсуляция*** - это явление замкнутости оболчки.
* ***Инкапсулировать*** - это процесс помещения чего-либо в оболчку.

* ***Инкапсуляция (ПО)*** - это явление сокрытия внутренней реализации и обеспечение целостности состояний.
* ***Инкапсулировать (ПО)*** - это процесс реалзиации объединения всех состояний и их сокрытие от внешней среды.

### Шаг 1. Пример из жизни - монитор
* Монитор
* Нам нужно увеличить контрастность
* Как мы это можем сделать?
    * Потыкаем кнопки, что-то да произойдет
    * Снимаем корпус, берем отвертку и ищем резистор (этот вариант недопустим, т.к. может привести к поломке монитора или нанести травму пользователю монитора)

### Шаг 2. Класс Ракета
* Преставтье у вас есть класс ```Rocket```
* Самая важная часть - это описание состояний двигателя
    * Допустим, касаемо описания состояний двигателя у нас есть 3 атрибута:
        * Максимальная температура сопла (Т)
        * Предельный расход топлива (л/с)
        * Скорость впрыска (л/с)

### Шаг 3. Критически важные атрибуты
* Критически важные атрибуты - это атрибуты класса, сильно влияющие на поведение объекта в целом. Изменение и доступ к таким атрибутам должен быть жескто ограничен.

### Шаг 4. Выделение интерфейсов
* ***Интерфейс взаимодейтсвия*** - способ взаимодействия с чем-либо.
* ***Публичный интерфейс*** - это способ взаимодействия с объектом, который доступ всему внешнему окружения.
* ***Приватный интерфейс*** - это внутренний способ взаимодействия с объектом, недоступный извне.


### Шаг 5. Реализация 
```
class Point:
    """
    Это точка.
    Допусти, координаты точки можно варьировать в пределах
    x,y := [-100, 100]
    Если выйдем за пределы - мир рухнет
    """

    def __init__(self, x: float = 0.0, y: float = 0.0):
        if x <= -100 or x >= 100:
            raise ValueError("attr X should be in [-100, 100]. got", x)
        if y <= -100 or y >= 100:
            raise ValueError("attr Y should be in [-100, 100]. got", y)
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Point<x:{self.__x}, y:{self.__y}>"

```

* Для реализации приватизации атрибутов (методов) , их стоит начинать называть с ```__```.
* После этого данные атрибуты становятся недоступными за пределами класса!
* В питоне реализован механизм ***полу-приватизации*** (приватизация по договоренности)

### Шаг 6. Сеттеры
* Сеттер - это метод, который позволяет безопасно устанавливать нвоые значения приватным атрибутам!
* В ```python``` принятно все сетеры начинать со слова ```set_```
```
class Point:
    """
    Это точка.
    Допусти, координаты точки можно варьировать в пределах
    x,y := [-100, 100]
    Если выйдем за пределы - мир рухнет
    """

    def __init__(self, x: float = 0.0, y: float = 0.0):
        if x <= -100 or x >= 100:
            raise ValueError("attr X should be in [-100, 100]. got", x)
        if y <= -100 or y >= 100:
            raise ValueError("attr Y should be in [-100, 100]. got", y)
        self.__x = x
        self.__y = y

    def set_x(self, new_x:float):
        if new_x <= -100 or new_x >= 100:
            raise ValueError("attr X should be in [-100, 100]. got", new_x)
        self.__x =  new_x

    def set_y(self, new_y:float):
        if new_y <= -100 or new_y >= 100:
            raise ValueError("attr Y should be in [-100, 100]. got", new_y)
        self.__y =  new_y

    def __str__(self):
        return f"Point<x:{self.__x}, y:{self.__y}>"

```

### Шаг 7. Геттеры
* Геттеры - это публичные методы, позволяющие безопасно получать доступ к приватным полям на чтение!
```class Point:
    """
    Это точка.
    Допусти, координаты точки можно варьировать в пределах
    x,y := [-100, 100]
    Если выйдем за пределы - мир рухнет
    """

    def __init__(self, x: float = 0.0, y: float = 0.0):
        if x <= -100 or x >= 100:
            raise ValueError("attr X should be in [-100, 100]. got", x)
        if y <= -100 or y >= 100:
            raise ValueError("attr Y should be in [-100, 100]. got", y)
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x:float):
        if new_x <= -100 or new_x >= 100:
            raise ValueError("attr X should be in [-100, 100]. got", new_x)
        self.__x =  new_x

    def set_y(self, new_y:float):
        if new_y <= -100 or new_y >= 100:
            raise ValueError("attr Y should be in [-100, 100]. got", new_y)
        self.__y =  new_y

    def __str__(self):
        return f"Point<x:{self.__x}, y:{self.__y}>"
```

### Шаг 8. Инкапсуляция - это ...
* ***Инкапсуляция (ООП)*** - процесс выделения публичных и приватных интерфейсов взаимодействия с объектами класса.

### Шаг 9. Приватные методы
* Приватные методы создаются точно по такому же правилу как и атрибуты - начинаем имя с ```__```.
```
class Point:
    def __init__(self, x:float=0.0, y:float = 0.0):
        if x <= -100 or x >= 100:
            raise ValueError("attr X should be in [-100, 100]. got", x)
        if y <= -100 or y >= 100:
            raise ValueError("attr Y should be in [-100, 100]. got", y)
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __shift(self, value:float):
        """
        Приватный метод для сдвига координат
        """
        self.__x += value
        self.__y += value

    def set_x(self, new_x:float):
        if new_x <= -100 or new_x >= 100:
            raise ValueError("attr X should be in [-100, 100]. got", new_x)
        self.__x =  new_x

    def set_y(self, new_y:float):
        if new_y <= -100 or new_y >= 100:
            raise ValueError("attr Y should be in [-100, 100]. got", new_y)
        self.__y =  new_y

    def __str__(self):
        self.__shift(10)
        return f"Point<x:{self.__x}, y:{self.__y}>"
```

### Шаг 10. Блиц!
```
class ____:
    def __init__(self):
        self._ = "_"
        self.__ = "____"
        self.___ = "____"
        self.____ = "_____"
```

* Сколько публичных, приватных и магических атрибутов в классе?
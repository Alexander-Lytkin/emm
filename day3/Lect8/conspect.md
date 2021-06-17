### Лекция 8. ООП. Абрстракция

***ООП (Объектно-Ориентированное Программирование)*** - это подход к созданию ПО, с использованием объектов.
* Альтернативное определение ***ООП*** - абстракция, инкапсуляция, полиморфизм и наследование.

### Шаг 0. Абстракция - это ...
* ***Абстракция*** - это общее описание происходящего явления или сопровождающего его предметов.
* ***Абстрагироваться*** - это процесс, в результате которого выделяются необходимые для решения поставленной задачи способы.

* ***Абстракция (ПО)*** - это общее описание состояний или поведений.
* ***Абстрагироваться (ПО)*** - это процесс, в результате которого выделяется минимально возможное число состояний (атрибутов) для реализации желаемого поведения.

### Шаг 1. Пример абстракций
* Основная проблема - абстракция не имеет какой-то команды или четкой реализации в коде.
* Допустим у нас есть класс Film
```
import time

class Film:
    """
    Класс описывающий фильм
    """
    def __init__(self, title, author, rating, duration, actors):
        self.title = title
        self.author = author
        self.rating = rating
        self.duration = duration
        self.actors = actors
        self.current_time = 0

    def play(self):
        """
        Запуск фильма
        """
        for _ in range(self.duration):
            time.sleep(1)
            print(f"Next scene in {self.title}")
            self.current_time += 1
        

    def has_action(self):
        """
        Фильм содержит экшн-сцены?
        """
        if "Vin Diesel" in self.actors:
            return True
        return False

    def replay(self):
        """
        Перемотка на какой-то момент
        """
        self.current_time = 0

def main():
    """
    Входная точка
    """
    f = Film("LOTR:2", "Mikle Bay", "5.0", 3, ["Legolas", "Bilbo", "Aragorn", "Vin Diesel"])
    f.play()
    print("Current time:", f.current_time)
    print("Has action?:", f.has_action())
    f.replay()

    
    print("Current time:", f.current_time)
if __name__ == "__main__":
    main()
```

* Применение абстракции
```
import time

class Film:
    """
    Класс описывающий фильм.
    Класс содержит минимум состояний для реализации
    своего поведения (абстрагирован)
    """
    def __init__(self, title, duration, actors):
        self.title = title 
        self.duration = duration
        self.actors = actors
        self.current_time = 0

    def play(self):
        """
        Запуск фильма
        """
        for _ in range(self.duration):
            time.sleep(1)
            print(f"Next scene in {self.title}")
            self.current_time += 1
        

    def has_action(self):
        """
        Фильм содержит экшн-сцены?
        """
        if "Vin Diesel" in self.actors:
            return True
        return False

    def replay(self):
        """
        Перемотка на какой-то момент
        """
        self.current_time = 0

def main():
    """
    Входная точка
    """
    f = Film("LOTR:2", 3, ["Legolas", "Bilbo", "Aragorn", "Vin Diesel"])
    f.play()
    print("Current time:", f.current_time)
    print("Has action?:", f.has_action())
    f.replay()


    print("Current time:", f.current_time)
if __name__ == "__main__":
    main()
```

* В результате применения абстракции над классом Film мы оставили минимально-возможное количество состояний для решений поставленной задачи!
    * Чем меньше состояний - тем проще понять, как оно устроено (пример - монитор)
    * Абстрагированные классы - гораздо проще поддерживать и на основе их очень удобно создавать новые (задел на наследование).

### Шаг 2. Абстракция - это ...
* ***Абстракция (абстрагирование) в ООП*** - это  процесс выделения мнимально возможного количество атрибутов класса для удовлетворения поведенческого паттерна, описанного методами этого класса.
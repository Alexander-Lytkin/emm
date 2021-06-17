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
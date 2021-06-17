"""
Создать модель очереди,
которая будет поддерживать следующий функционал:
    * Если приходит человек с фразой "Кто последний? Я - <фамилия>." - то этого человека 
        надо добавить в конец очереди
    * Если врач говорит "Следующий!" - то будет заходить первый стоящий в очереди. Если очередь
        уже пустая , то будем выводить "В очереди никого нет!"
"""

class Queue:
    """
    Класс, описывающий модель очереди
    """
    def __init__(self, queue:list = []):
        self.queue = queue # Инициализируем атрибут объекта queue значением queue,который явл.параметром

    def add_to_tail(self, name:str):
        """
        Метод добавляет новую персону name 
        в конец очереди queue
        """
        self.queue.append(name)

    def remove_from_head(self) -> str:
        """
        Возвращает имя первой
        персоны в очереди и удаляет ее из очереди
        """
        if len(self.queue) > 0:
            return self.queue.pop(0)

        return "В очереди никого нет!"
    def __str__(self):
        return "Queue<" + ", ".join(self.queue) + ">"

def main():
    """
    Входная точка
    """
    q = Queue()
    first_person_command = "Кто последний? Я - Вася."
    second_person_command = "Кто последний? Я - Петя."
    q.add_to_tail(
        name=first_person_command.split(" - ")[1].split('.')[0]
        )
    q.add_to_tail(
        name=second_person_command.split(" - ")[1].split('.')[0]
    )
    print(q.remove_from_head()) # Вася
    print(q) # Queue<Петя>

if __name__ == "__main__":
    main()
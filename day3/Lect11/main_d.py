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
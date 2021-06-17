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
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
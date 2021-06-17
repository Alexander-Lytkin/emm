class A:
    __a = 10 # _A__a
    def get_a(self):
        return self.__a

class B(A):
    __b = 20

    def say_private(self):
        print(self.__b, self.get_a())

b = B()
b.say_private()
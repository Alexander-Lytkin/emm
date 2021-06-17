class A(str):
    def say(self):
        pass

class B(A):
    pass

class C(B):
    pass

a = A()
b = B()
c = C()

print("a is A", isinstance(a, A))
print("a is B",isinstance(a, B))
print("a is C",isinstance(a, C))

print("b is A", isinstance(b, A))
print("b is B", isinstance(b, B))
print("b is C", isinstance(b, C))

print("c is A", isinstance(c, A))
print("c is B", isinstance(c, B))
print("c is C", isinstance(c, C))

print("a is str", isinstance(a, str))

print("C is str", issubclass(C,str))
print("A is C", issubclass(A, C))
"""
Простейшее линейное наследование
"""
class A:
    a = "a"

class B(A):
    #a = "a"
    b = "b"

class C(B):
    #a = "a"
    #b = "b"
    c = "c"

def main():
    """
    Start
    """
    c = C()
    print(c.a, c.b, c.c)

    

if __name__ == "__main__":
    main()
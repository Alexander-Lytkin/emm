class AbstactFigure:
    def __init__(self):
        raise NotImplemented()

    def perimeter(self):
        raise NotImplemented()

    def area(self):
        raise NotImplemented()

    def __str__(self):
        raise NotImplemented()

class Rectangle(AbstactFigure):
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2*(self.a + self.b)
    def area(self):
        return self.a * self.b
        
    def __str__(self):
        return f"Rect <a:{self.a}, b:{self.b}>"

def main():
    r = Rectangle(a=10, b = 20)
    print(r.perimeter(), r.area())
    print(r)
if __name__ == "__main__":
    main()
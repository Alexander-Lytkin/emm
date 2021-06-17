
import math
class Rectangle:
    def __init__(self, width:float, length:float ):
        self.width = width
        self.length = length

    def perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def area(self) -> float:
        return self.width * self.length

    def __str__(self):
        return f"Rectangle<W:{self.width}, L:{self.length}>"


class Circle:
    def __init__(self, radius:float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle<R:{self.radius}>"

class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        semi_p = self.perimeter() / 2
        return (semi_p*(semi_p - self.a)*(semi_p - self.b) * (semi_p - self.c))**0.5

def metrics(figures:list) -> tuple:
    """
    Возвращает общую площадь и периметр всех фигур
    """
    total_area = 0
    total_perimeter = 0
    for fig in figures:
        total_area += fig.area()
        total_perimeter += fig.perimeter()

    return (total_area, total_perimeter)


def main():
    """
    Start
    """
    r1 = Rectangle(width=5, length=200)
    r2 = Rectangle(width=80, length = 50)
    r3 = Rectangle(width=2, length =200)
    c1 = Circle(radius=52)
    c2 = Circle(radius=31)
    c3 = Circle(radius=85)
    tr1 = Triangle(a=3, b=4, c= 5)
    tr2 = Triangle(a=4, b=3, c=5)

    figures = [r1, r2, r3, c1, c2, c3, tr1, tr2]
    
    total_area, total_perimeter = metrics(figures)

    print("Total area:",total_area)
    print("Total perimeter:", total_perimeter)

if __name__ == "__main__":
    main()
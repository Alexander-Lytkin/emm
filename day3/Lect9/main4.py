"""
Решение задачи
нахождения длины отрезка по двум точкам
"""

class Point:
    """
    Класс точки
    Точки могут быть только с координатами
    в пределах от [-1000, 1000]
    """
    def __init__(self, x:float=0, y:float=0):
        if x <= -1000 or x >= 1000:
            raise ValueError("attr X should be in [-1000, 1000]. got", x)
        if y <= -1000 or y >= 1000:
            raise ValueError("attr Y should be in [-1000, 1000]. got", y)
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x:float):
        if new_x <= -1000 or new_x >= 1000:
            raise ValueError("attr X should be in [-1000, 1000]. got", new_x)
        self.__x = new_x

    def set_y(self, new_y:float):
        if new_y <= -1000 or new_y >= 1000:
            raise ValueError("attr Y should be in [-1000, 1000]. got", new_y)
        self.__y = new_y

    def __str__(self):
        return f"Point<{self.__x}, {self.__y}>"
    

class Line:
    """
    Класс описывающий линию
    """
    def __init__(self, p1:Point, p2:Point):
        self.__p1 = p1
        self.__p2 = p2

    def get_p1(self):
        return self.__p1

    def get_p2(self):
        return self.__p2

    def set_p1(self, new_p1:Point):
        self.__p1 = new_p1

    def set_p2(self, new_p2:Point):
        self.__p2 = new_p2

    def length(self) -> float:
        """
        Считает длину отрезка и возвращает ее
        """
        delta_x = self.__p1.get_x() - self.__p2.get_x()
        delta_y = self.__p1.get_y() - self.__p2.get_y()
        return (delta_x**2 + delta_y**2) ** 0.5

    def __str__(self):
        return f"Line on p1{self.__p1}, p2{self.__p2}"
    

def main():
    """
    Start
    """
    line = Line(
        Point(0,0),
        Point(10,10)
    )
    print(line.length())

if __name__ == "__main__":
    main()
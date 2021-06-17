class Point:
    """
    Это точка.
    Допусти, координаты точки можно варьировать в пределах
    x,y := [-100, 100]
    Если выйдем за пределы - мир рухнет
    """

    def __init__(self, x: float = 0.0, y: float = 0.0):
        if x <= -100 or x >= 100:
            raise ValueError("attr X should be in [-100, 100]. got", x)
        if y <= -100 or y >= 100:
            raise ValueError("attr Y should be in [-100, 100]. got", y)
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x:float):
        if new_x <= -100 or new_x >= 100:
            raise ValueError("attr X should be in [-100, 100]. got", new_x)
        self.__x =  new_x

    def set_y(self, new_y:float):
        if new_y <= -100 or new_y >= 100:
            raise ValueError("attr Y should be in [-100, 100]. got", new_y)
        self.__y =  new_y

    def __str__(self):
        return f"Point<x:{self.__x}, y:{self.__y}>"


def main():
    """
    Start
    """
    p = Point(-92, 82)
    print(p)
    p.set_x(11)
    p.set_y(99)
    print(p.get_y())
    print(dir(p))
    


if __name__ == "__main__":
    main()

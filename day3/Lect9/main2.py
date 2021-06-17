class Point:
    def __init__(self, x:float=0.0, y:float = 0.0):
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

    def __shift(self, value:float):
        """
        Приватный метод для сдвига координат
        """
        self.__x += value
        self.__y += value

    def set_x(self, new_x:float):
        if new_x <= -100 or new_x >= 100:
            raise ValueError("attr X should be in [-100, 100]. got", new_x)
        self.__x =  new_x

    def set_y(self, new_y:float):
        if new_y <= -100 or new_y >= 100:
            raise ValueError("attr Y should be in [-100, 100]. got", new_y)
        self.__y =  new_y

    def __str__(self):
        self.__shift(10)
        return f"Point<x:{self.__x}, y:{self.__y}>"

def main():
    """
    Start
    """
    p = Point()
    print(p)
    print(p)
    print(p)

if __name__ == "__main__":
    main()
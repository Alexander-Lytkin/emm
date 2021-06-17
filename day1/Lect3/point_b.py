"""
Считывание данные в задаче A
"""

class Point:
    """Это структура Точки.

    * содержит поле x - это координата x
    * содержит поле y - это координата y
    """

    x = 0
    y = 0


def point_creator(x_arg: int, y_arg: int) -> Point:
    """Создает и возвращает точку с координатами x_arg и y-arg."""
    p = Point()
    p.x = x_arg
    p.y = y_arg
    return p

def is_on_line(ref_point_1:Point, ref_point_2:Point, quest_point:Point) -> bool:
    """
    Функция возвращает  True  если quest_point 
    * принадлежит отрезку [ref_point1, ref_point2]
    Иначе - возвращает False
    """
    pass

def main():
    """
    Входная точка
    """

    first_line = [int(x) for x in input().split()] # [0,  0,  10, 10]
    second_line = [int(x) for x in input().split()]


    p1 = point_creator(first_line[0], first_line[1])
    p2 = point_creator(first_line[2], first_line[3])
    p3 = point_creator(second_line[0], second_line[1])
    if is_on_line(ref_point_1=p1, ref_point_2= p2, quest_point=p3):
        print('YES')
    else:
        print("NO")

if __name__ == "__main__":
    main()
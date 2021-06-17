from point import Point

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

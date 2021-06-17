"""Модуль содержащий описание структуры Точка."""


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



def length(p1: Point, p2: Point) -> float:
    """Подсчет длины отрезка на точках p1 p2."""
    delta_x = p1.x - p2.x
    delta_y = p1.y - p2.y
    result = (delta_x ** 2 + delta_y ** 2) ** 0.5
    return result


def main() -> None:
    """Входная точка в приложение."""
    p_first = point_creator(0, 0)
    p_second = point_creator(10, 10)
    print(length(p_first, p_second))


if __name__ == "__main__":
    main()

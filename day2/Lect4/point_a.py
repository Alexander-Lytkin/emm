"""
Модуль с точкой
"""

class Point:
    """
    Класс как класс
    """
    x = 0
    y = 0

    def stringer(p):
        """
        Преобразует точку в строкове представление
        """
        return f"Point[x:{p.x}, y:{p.y}]"

    def shifter(p, shift):
        """
        Данная процедура сдвигает точку на shift единиц
        """
        p.x = p.x + shift
        p.y = p.y + shift
        return p


        

def point_creator(x_arg, y_arg) :
    """Создает и возвращает точку с координатами x_arg и y-arg."""
    p = Point()
    p.x = x_arg
    p.y = y_arg
    return p



points = [
    point_creator(10, 10), # объект класса Point/экземпляр класса
    point_creator(20, 30),
    point_creator(30, 40),
    point_creator(1, 2),
]

for p in points:
    print("Before shift:", p.stringer())
    p = p.shifter( 10)
    print("After shift:", p.stringer(p))

"""
p.stringer() равносильно Point.stringer(p)
Будем пользоваться синтаксисом p.stringer()
"""


"""
Модуль с точкой
"""

class Point:
    """
    Класс как класс
    """
    x = 0
    y = 0

    def stringer(self):
        """
        Преобразует точку в строкове представление
        """
        return f"Point[x:{self.x}, y:{self.y}]"

    def shifter(self, shift):
        """
        Данная процедура сдвигает точку на shift единиц
        """
        self.x = self.x + shift
        self.y = self.y + shift

p = Point()
print(p.stringer())
p.shifter(10)
print(p.stringer())




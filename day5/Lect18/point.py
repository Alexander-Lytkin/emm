"""
Module with points
"""
from collections import namedtuple

class Point:
    """
    Point description
    """
    def __init__(self, x:int, y:int):
        self.x = x 
        self.y = y
    def __str__(self):
        return f"<Point X:{self.x} Y:{self.y}>"

p = Point(x =1, y=2)
print(p)
print(p.x, p.y)

NewPoint = namedtuple('NewPoint', ['x', 'y'])
np = NewPoint(1, 2)
print(np)
print(np.x, np.y)
print(np[0], np[1])
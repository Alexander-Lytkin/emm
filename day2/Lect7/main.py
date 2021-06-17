"""
Модуль, содержащий игры с классом Рюкзак
"""
from typing import Type


class Backpack:
    """
    Класс, описывающий рюкзак
    """
    def __init__(self, weight:int=0, volume:int=0):
        self.weight = weight
        self.volume = volume

    def __eq__(self, other):
        return (self.weight == other.weight) and (self.volume == other.volume)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.volume > other.volume

    def __lt__(self, other):
        return self.volume < other.volume
    
    def __ge__(self, other):
        return self.volume >= other.volume

    def __le__(self, other):
        return self.volume <= other.volume

    def __add__(self, other):
        return Backpack(
            weight=self.weight + other.weight, 
            volume=self.volume + other.volume
            )

    def __str__(self):
        return f"Backpack<W:{self.weight} kg, V:{self.volume} l>"

    def __enter__(self):
        print("__enter__ works")
        return self.weight * 100

    def __exit__(self, *args):
        print("__exit__ works")


def main():
    """
    Входная точка
    """
    bp_first = Backpack(weight=11, volume=61)
    bp_second = Backpack(weight=12, volume=60)
    with bp_first as value:
        print("Value:", value)



if __name__ == "__main__":
    main()
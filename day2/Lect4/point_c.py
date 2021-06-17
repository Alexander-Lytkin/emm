
class Point:
    """
    Класс как класс
    """
    def __init__(self, x_arg=0.0, y_arg=0.0) :
        """Назначает значения атрибутам класса"""
        self.x = x_arg # Создаете атрибут x
        self.y = y_arg # Создаете атрибут y


    def __str__(self):
        """
        Преобразует точку в строкове представление
        """
        
        return f"Point[x:{self.x}, y:{self.y}]"

    def __repr__(self):
        """
        Делает представление объекта
        """
        return f"Point repr [x:{self.x}, y:{self.y}]"

        
    def shifter(self, shift):
        """
        Данная процедура сдвигает точку на shift единиц
        """
        self.x = self.x + shift
        self.y = self.y + shift


    
def main():
    p = Point(10, 20) # Point.__new__() -> object -> Point__init__(object, ....) -> object
    print(p.x, p.y)
    q = str(p) # print(str(p)) #str(p) -> p.__str__()
    q += "NqanananananananananBataman"
    print(q)
    print(p.x, p.y)
    
    

if __name__ == "__main__":
    main()


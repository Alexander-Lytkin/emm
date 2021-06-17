class Person:
    def __init__(self, name:str):
        self.__name = name
    
    @property # теперь есть такой property как name и к неу можно добюавлять то то 
    def name(self):
        """
        Имитатор геттера для name
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        print("name setter works!")
        if len(new_name) < 2:
            raise TypeError("invalud new_name type length")

        self.__name = new_name

    def __str__(self):
        return f"Person:{self.__name}"

def main():
    p = Person("Bob")
    p.name = "A" # Здесь вызывается setter
    print(p.name) # Здесь вызывается getter


if __name__ == "__main__":
    main()
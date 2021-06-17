class Person:
    def __init__(self, name:str, age:int):
        print("Person __init__")
        self.name = name 
        self.age = age

    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}"

class Schoolar(Person):
    def __init__(self, name:str, age:int, letter:str, wakeup:str):
        print('Schoolar __init__')
        super().__init__(name, age)
        self.letter = letter
        self.wakeup = wakeup

    
    def __str__(self):
        return super().__str__() + f", Letter:{self.letter}, WakeUp: {self.wakeup}"

def main():
    sc = Schoolar("Bob", 14, 'd', '07:00')
    print(sc)
if __name__ == "__main__":
    main()
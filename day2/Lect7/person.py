"""
Test module for person serialize
"""
import json


class Person:
    """
    Person description
    """
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        self.jeronimo = None

    def to_json(self):
        return self.__dict__

    def __str__(self):
        return f"Person<N:{self.name}, A:{self.age}>"

def main():
    """
    Start
    """
    person = Person("Bob", 23)
    result = json.dumps(person.to_json(), indent=4, sort_keys=True)
    print(result)
    
if __name__ == "__main__":
    main()
"""
Есть персона - это кмакой-то человек
Хотим на основе человека построить школьника
* Проблема 1 - если когда-нибудь нам потребуется внести изменения в Person
    то в школьнике их придется делать руками! (Дублирование кода)
"""

class Person:
    name = "####"
    lastname = "####"
    age = None


class Schoolar(Person):
    letter = "Z"
    wake_up_time = "07:00"

def main():
    """
    """
    sc = Schoolar()
    print(sc.name, sc.lastname, sc.letter)
    
if __name__ == "__main__":
    main()
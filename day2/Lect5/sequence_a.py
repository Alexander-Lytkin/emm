class AFinder:
    """
    Класс, отвечающий на вопрос -
    сколько раз буква 'A' и 'a' 
    встречается в строке
    """
    def __init__(self, input_msg:str):
        self.message = input_msg

    def find(self) -> int:
        """
        Возвращает количество букв А и а в 
        строке
        """
        return self.message.count("A") + self.message.count("a")

    def __str__(self):
        return f"AFinder[msg:{self.message}]"

# 1) Первым делом вам необходимо определить желаемое поведение!!!!!
# 2) Разрабсываем скелет
def main():
    """
    Входная точка
    """
    afinder = AFinder(
        input_msg = input()
        )
    print(afinder.find()) # 2

if __name__ =="__main__":
    main()
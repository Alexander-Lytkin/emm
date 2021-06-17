class SmartList:
    """
    Класс, реализующий функционал
    списка, который автоматически
    поддерживает в отсортированном состоянии (список слов - ТОЛЬКО по !алфавиту!)
    """
    def __init__(self, input_words:list):
        self.word = input_words
        self.sort_me() # Образаюсь к методу sort_me

    def add(self, new_word:str):
        self.word.append(new_word)
        self.sort_me()

    def sort_me(self):
        self.word.sort()

    def __str__(self):
        return "[" + ", ".join(self.word) + "]"

def main():
    sm = SmartList(
        input_words=["bob", "alice", "george"]
        )
    print(sm) # ['alice', 'bob', 'george'] 
    sm.add("bobby")
    print(sm) # ['alice', 'bob', 'bobby', 'george']
    print(10) # str(p=10) -> p.__str__() -> "10"

if __name__ == "__main__":
    main()


def sub(a,b):
    return a**2 - b**2



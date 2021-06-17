import json

class JSONSerializable:
    def __init__(self):
        raise NotImplementedError

    @classmethod
    def from_json(cls, obj):
        return cls(**obj)

    def to_json(self):
        return self.__dict__ # Вернет словарь из пар имя_атрибута:значение

    def __str__(self):
        raise NotImplementedError

class Triangle(JSONSerializable):
    def __init__(self, a:int, b:int, c:int):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Triangle:{self.a} {self.b} {self.c}"


def main():
    """
    Start
    """
    tr1 = Triangle(10, 20, 30)
    with open("figure.json", "w") as fh:
        json.dump(tr1.to_json(), fh, indent=4)

    with open("figure.json", "r") as fh:
        print(Triangle.from_json(json.load(fh)))

if __name__ == "__main__":
    main()
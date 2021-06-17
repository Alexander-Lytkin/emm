"""
json example
"""
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

class User(JSONSerializable):
    def __init__(self, id:int, username:str, password:str):
        self.username = username
        self.password = password
        self.id  = id

    def say(self):
        print("Hello! I'm", self.username)

    def __str__(self):
        return f"User({self.id}, {self.username}, {self.password})"
    def __repr__(self):
        return self.__str__()

def serialize(obj):
    return json.dumps(obj, indent=4)

def deserialize(bytes):
    return json.loads(bytes)

def main():
    """
    Start
    """
    person = User(id=2, username="alice", password="password")
    serialized_value = serialize(person.to_json())
    print(serialized_value)

    recovered_value = User.from_json(json.loads(serialized_value))
    print(recovered_value)

    with open("data.json", "w") as fh:
        json.dump(person.to_json(), fh, indent=4)

    with open("data.json", "r") as fh:
        from_file = User.from_json(json.load(fh))
        print(from_file)

if __name__ == "__main__":
    main()
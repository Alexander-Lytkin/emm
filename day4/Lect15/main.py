"""
pickle example
"""
import pickle

class User:
    def __init__(self, _id:int, username:str, password:str):
        self.username = username
        self.password = password
        self.id  = _id

    def say(self):
        print("Hello! I'm", self.username)

    def __str__(self):
        return f"User({self.id}, {self.username}, {self.password})"
    def __repr__(self):
        return self.__str__()

def serialize(obj):
    return pickle.dumps(obj)

def deserialize(bytes):
    return pickle.loads(bytes)

def main():
    """
    Start
    """
    # Вложенные коллекции
    result_value = [
        User(_id=1, username="admin", password="admin"),
        User(_id=2, username="vasya", password="vasya"),
        User(_id=3, username="alice", password="alice"),
    ]

    serialized_value = serialize(result_value) #loads()
    print(serialized_value)
    # recovered_value = deserialize(serialized_value)
    # print("\n\n", recovered_value)

    with open("data.pickle", "wb") as fh:
        pickle.dump(result_value, fh)

    with open("data.pickle", "rb") as fh:
        from_file = pickle.load(fh)
        print("\n\n\n\nFrom file:", from_file)
        for user in from_file:
            user.say()

if __name__ == "__main__":
    main()
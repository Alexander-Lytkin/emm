### Лекция 15. Способы хранения объектов?

***Допустим*** существует объект А. Нужно его сохранить. Как?

### Шаг 0. Объектно-Реляционные соответствия и сериализация
* ***Объектно-Реляционное соответствие*** - это способ сохранения информации об объекте с привязкой к его структуре.

* ***Сериализация*** - конвертация в низкоуровневое представление объекта, и поселдующее его сохранение.

### Шаг 1. Про сериализацию
* ***Сериализация*** - это процесс, в результате которого объект конвертируется в последовательность байт.
* ***Десериализация*** - это процесс, в резульатте которого объект восстанавливается из последовательности байт.

* В ```python``` модуль ```pickle```
* Функция ```dumps(obj)``` (dump-to-String) - преобразует объект в последовательность байт и сохраняет это в run-time в виде байтовой строки. 
* Функция ```loads(bytes)``` (load-from-String) - функция, которая восстанавливает объект (десериализует) из байтовой строки ```bytes```.

* Функция ```dump(obj, fh)``` - преобразует объект в последовательность байт и сохраняет в файл ```fh```
* Функция ```from_file = pickle.load(fh)``` - пытается восстановить серилазиованный объект в файле ```fh```.
```
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
```

### Шаг 2. Сериализация и JSON
* ```JSON``` - файловое расширение, которое позволяет хранить в себе наборы байт, при этом, отображая эти наборы в человеко-читаемом виде.
* ```JSON``` - ```JavaScriptObjectNotation```  (js object == python dict)
* ```JSON``` способен хранить только состояния!
* В питоне есть модуль ```json```
    * ```dump() dumps()```
    * ```load() loads()```
```
"""
json example
"""
import json

def serialize(obj):
    return json.dumps(obj, indent=4)

def deserialize(bytes):
    return json.loads(bytes)

def main():
    """
    Start
    """
    person = {"name" : "admin", "address" : "Hamburg", "vaild" : None}
    serialized_value = serialize(person)
    print(serialized_value)

    recovered_value = deserialize(serialized_value)
    print(recovered_value)

    with open("data.json", "w") as fh:
        json.dump(person, fh, indent=4)

    with open("data.json", "r") as fh:
        from_file = json.load(fh)
        print(from_file)

if __name__ == "__main__":
    main()
```

### Шаг 3. JSON и пользовательские классы
* Беда ```TypeError: Object of type User is not JSON serializable```
* Сериализация в ```json``` пользовательскими классами по умолчанию не поддерживается.
* Для сериализации состояния пользователя в ```json``` необходимо добавить механизм отделения состояния объекта (```to_json```)
```
"""
json example
"""
import json

class User:
    def __init__(self, _id:int, username:str, password:str):
        self.username = username
        self.password = password
        self.id  = _id

    def to_json(self):
        return self.__dict__ # Вернет словарь из пар имя_атрибута:значение

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
    person = User(_id=1, username="admin", password="password")
    serialized_value = serialize(person.to_json())
    print(serialized_value)
```

***ВАЖНО*** - прочтите ```*args, **kwargs```
            - прочтите про типы реляций в  бд (one-to-one, many-to-one, many-to-many)

```
"""
json example
"""
import json

class User:
    def __init__(self, id:int, username:str, password:str):
        self.username = username
        self.password = password
        self.id  = id

    @classmethod
    def from_json(cls, obj):
        return cls(**obj)

    def to_json(self):
        return self.__dict__ # Вернет словарь из пар имя_атрибута:значение


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
```

* Абстрактный сериализатор!
```
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

```

* Теперь, наследуясь от ```JSONSerializable``` можно без труда сериализовать/десериализовать вообще любой пользовательский класс!
from collections import Counter

words = ["alice", "bob", "alice", "bob", "bob", "bob", "a", "b", "a"]
counter = Counter(words)

print(counter["bob"])  # можем обращаться по ключам, как у словаря
for k, v in counter.items():  # Поддерживает методы словарей
    print(k, v)

# Получение всех элементов
print(list(counter.elements()))
# Топ-3
counter = Counter("hello world! hellol world")
print(counter.most_common(3))

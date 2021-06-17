from collections import ChainMap

first = {"a" : 1, "b" : 2, "c" : 3}
second = {"d" : 4, "a" : 5, "f" : 6}

third = ChainMap(first, second)
third = third.new_child({"g" : 10, "h" : 200})
for k, v in third.items():
    print(k, v)

print(third)
print(third["d"])
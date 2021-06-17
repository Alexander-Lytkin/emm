from collections import OrderedDict
pairs = [("a", 1), ('b', 10), ('c', 50), ('d', 150)]

od = OrderedDict()
for p in pairs:
    od[p[0]] = p[1]
    

print(od)
# Перетаскивание в конец
od.move_to_end('a', last=True)
print(od)

# Удалим первый добавленный элемент
od.popitem(last=False)
print(od)
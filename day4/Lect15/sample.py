def add(*args):
    s = 0
    for a in args:
        s += a
    return s 

print(add(1,2)) # args = (1,2)
print(add(1,2,3,4)) # args = (1,2,3,4)
print(add(1)) # args = (1,)

def sub(a,b,c):
    return a ** 2 + b ** 3 + c ** 4

tup = (10, 20, 30)
print(sub(*tup)) # sub(10, 20, 30)
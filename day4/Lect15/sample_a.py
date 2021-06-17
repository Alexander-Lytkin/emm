def add(**kwargs):
    print(kwargs)

add(vova=10, vitya=20, a=3, b=4)

def sub(a, b, c):
    return a ** 2 + b ** 3 + c ** 4
params = {
    "a" : 10,
    "b" : 20,
    "c" : 30,
}

print(sub(**params)) # sub(a=10, b=20, c=30)
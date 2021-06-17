class A:
    name = "name_a"
    a = "a"

class B(A):
    name = "name_b"
    b = "b"

def main():
    """
    """
    b = B()
    print(b.name)

if __name__ == "__main__":
    main()
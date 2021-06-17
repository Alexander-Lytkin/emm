"""module with erros."""


def add(a_arg: int, b_arg: int):
    """return sum of a_arg and b_arg."""
    return a_arg + b_arg


def sub(a_arg: int, b_arg: int):
    """
    return a_arg - b_arg
    """
    return a_arg - b_arg


def mult(a_arg: int, b_arg: int):
    """
    return a_arg * b_arg
    """
    return a_arg * b_arg


def main():
    """Start."""
    result = add(2, 3) + sub(3, 4) + mult(1, 5)
    print(result)


if __name__ == "__main__":
    main()

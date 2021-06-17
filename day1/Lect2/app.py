"""Этот модуль содержит набор учебных функций."""


def add(x_arg: int, y_arg: int) -> int:
    """Функция возвращает результат арифметического сложения параметров x_arg и
    y_arg."""
    return x_arg + y_arg


def sub(x_arg: int, y_arg: int) -> int:
    """Функция возвращает результат арифметического вычитания параметров x_arg
    и y_arg."""
    return x_arg - y_arg


def mult(x_arg: int, y_arg: int) -> int:
    """Функция возвращает результат арифметического умножения параметров x_arg
    и y_arg."""
    return x_arg * y_arg


def sq_add(x_arg: int, y_arg: int) -> int:
    """Функция возвращает результат суммы квадратов параметров x_arg и
    y_arg."""
    return x_arg ** 2 + y_arg ** 2


def main() -> None:
    """Входная точка в приложение."""
    a_num = int(input())
    b_num = int(input())
    result = add(a_num, b_num) * sub(a_num, b_num) / mult(a_num, b_num)
    result += 1 / sq_add(a_num, b_num)
    print(result)
    


if __name__ == "__main__":
    main()

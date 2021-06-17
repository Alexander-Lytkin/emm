"""
Легкий способ выделить нужные блоки
в задаче А
"""

TOTAL_MESSAGE = "ooooppoopopopoooopopoooooooooopopo"

def main():
    """
    Входная точка
    """
    print(len(max(TOTAL_MESSAGE.split('p'))))

if __name__ == "__main__":
    main()
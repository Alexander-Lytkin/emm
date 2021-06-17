from point_a import Point

def main():
    """
    Входная точка
    """

    first_line = [int(x) for x in input().split()] # [0,  0,  10, 10]
    second_line = [int(x) for x in input().split()]


    p1 = Point.point_creator(first_line[0], first_line[1])
    p2 = Point.point_creator(first_line[2], first_line[3])
    p3 = Point.point_creator(second_line[0], second_line[1])

   

if __name__ == "__main__":
    main()

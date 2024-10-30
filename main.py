class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add_points(self, point):
        x = self.__x + point.x
        y = self.__y + point.y
        return Point(x, y)


def main():

    p1 = Point(3, 4)
    p2 = Point(2, 2)
    p1.__add_points(p2)
main()
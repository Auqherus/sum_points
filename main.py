class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, point):
        x = self.__x + point.__x
        y = self.__y + point.__y
        return Point(x, y)
    
    def __str__(self):
        return f"Point({self.__x}, {self.__y})"

def main():

    p1 = Point(3, 4)
    p2 = Point(2, 2)
    p3 = p1 + p2
    print(p3)
main()
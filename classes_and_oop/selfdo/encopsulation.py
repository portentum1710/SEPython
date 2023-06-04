class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y


pt = Point(1, 2)
print(pt.__dict__)

print(pt.__x)
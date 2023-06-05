#              __setattr__(self, key, value)__
# – автоматически вызывается при изменении свойства key класса;
#              __getattribute__(self, item)
# – автоматически вызывается при получении свойства класса с именем item;
#              __getattr__(self, item)
# – автоматически вызывается при получении несуществующего свойства item класса;
#              __delattr__(self, item)
# – автоматически вызывается при удалении свойства item (не важно: существует оно или нет)

class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MAX_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MAX_COORD = left


pt1 = Point(1, 2)
pt2 = Point(10, 20)

print(pt1.MAX_COORD)
# getattr(object, name, [,default]) - возвращает значение атрибута объекта.
# hasattr(obj, name) - проверяет на наличие атрибута name в obj.
# setattr(obj, name, value) - задает значение атрибута(если атрибут не существует, то он создаётся).
# delatrr(obj, name) - удаляет атрибут с именем name

# __doc__ - содержит строку с описанием класса.
# __dict__ - содержит набор атрибутов экземпляра класса.

class Point:
    color = "red"
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point()
pt.set_coords(1, 2)
pt2 = Point()
pt2.set_coords(10, 20)
print(pt2.get_coords())

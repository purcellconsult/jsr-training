################################
# OOP basics in python
# --------------------
# Learn the basics of OOP by
# modeling a simple point
# in python.
#
#
#
################################


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x_value):
        self.x = x_value

    def set_y(self, y_value):
        self.y = y_value

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

# create an instance of the class

point1 = Point(5, 10)
print(point1.get_x())
print(point1.get_y())

point1.set_x(100)
point1.set_y(50)

print(point1.get_x())
print(point1.get_y())

point2 = Point(299, 300)

point3 = (75, 20)


# Simple inheritance example in python
# ------------------------------------
# class B extends class A
# Or class B subclasses class A


class B(Point):
    pass

class C(B):
    pass

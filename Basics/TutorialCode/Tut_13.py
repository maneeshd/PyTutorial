import math


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance_from_point(self, point):
        dx = point.get_x() - self.x
        dy = point.get_y() - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        return dist

    def reflect(self):
        return '(' + str(self.x) + ', ' + str(0 - self.y) + ')'

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def slope_from_origin(self):
        if self.x == 0:
            return None
        else:
            return self.y / self.x


point1 = Point(7, 7)
point2 = Point(6, 9)
print("Point1 = ", point1)
print("Point2 = ", point2)
print("Distance between Point1 & Point2 is %.2f" % point1.distance_from_point(point2))
print("Reflection of Point1 along x-axis is", point1.reflect())
print("Reflection of Point2 along x-axis is", point2.reflect())
print("Slope from Origin for Point1 is %.2f" % point1.slope_from_origin())
print("Slope from Origin for Point2 is %.2f" % point2.slope_from_origin())

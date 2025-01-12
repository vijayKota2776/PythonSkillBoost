import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, other_point):
        if isinstance(other_point, Point):
            return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        else:
            raise ValueError("The argument must be a Point object.")

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
point1 = Point(2, 3)
point2 = Point(5, 7)
print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
point1.set_coordinates(4, 1)
print(f"Updated Point 1: {point1}")
distance = point1.distance_from(point2)
print(f"Distance between Point 1 and Point 2: {distance:.2f}")
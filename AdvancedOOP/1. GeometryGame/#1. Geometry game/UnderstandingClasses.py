class Point: # BluePrint
    def __init__(self, x, y): # initialize, executed when class is instanced
        self.x = x
        self.y = y
        self.point = (x, y)

    # methods, executed only when called explicitly
    def falls_in_rectangle(self, lower_left, upper_right):
        if lower_left[0] < self.x < upper_right[0] and lower_left[1] < self.y < upper_right[1]:
            return True
        else:
            return False
                    # Remember we can't give class typing Point inside same class i.e a: Point
    def distance_from_point(self, point): # We can solve this by pythagorean theorem
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5 # 0.5 is sqrt

point1 = Point(3, 7)
point2 = Point(4, 2)
point3 = Point(1, 5)
    #   self.x
print(point1.x)

print(point1.falls_in_rectangle(
    lower_left= (1, 6),
    upper_right= (4, 8)
))

print(point1.distance_from_point(
    point= point3
))

# Creating another class
class Rectangle:
    def __init__(self, lower_left: Point, upper_right: Point): # accepts tuple
        self.lower_left = lower_left
        self.upper_right = upper_right

    # Creating method
    def inside_rectangle(self, point: Point):
        return self.lower_left.x < point.x < self.upper_right.x and \
        self.lower_left.y < point.y < self.upper_right

    def area(self): # Length * breadth
                    # As upper_right will be higher value
        return (self.upper_right.x - self.lower_left.x) * \
               (self.upper_right.y - self.lower_left.y)

import random

rectangle1 = Rectangle(lower_left= Point(random.randint(1, 9), random.randint(1, 9)),
                       upper_right= Point(random.randint(10, 19), random.randint(10, 19)))

# user_point: float = Point(float(input("Enter Guess x")),
#                           float(input("Enter Guess y")))
#
# print(rectangle1.inside_rectangle(point= user_point))
print(rectangle1.lower_left.point, rectangle1.upper_right.point)
print(rectangle1.area())
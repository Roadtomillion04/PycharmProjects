from random import randint
import turtle

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(object):
    def __init__(self, lower_left: Point, upper_right: Point):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def falls_in_rectangle(self, point: Point):
        if self.lower_left.x < point.x < self.upper_right.x and \
        self.lower_left.y < point.y < self.upper_right.y:
            return True
        return False

    def area(self): # l x b
        # in maths we consider origin as (0, 0), to shorten formula we use upper_right() x * y
        return (self.upper_right.x - self.lower_left.x) * \
               (self.upper_right.y - self.lower_left.x)

class RectangleGui(Rectangle): # inheritance

    def draw_gui(self, canvas):
        canvas.penup() # hide()
        canvas.goto(x= self.lower_left.x, y= self.lower_left.y)

        # show()
        canvas.pendown()
        ''' drawing rectangle '''
        height = self.upper_right.y - self.lower_left.y
        width = self.upper_right.x - self.lower_left.x

        canvas.forward(distance= width)
        canvas.left(90)

        canvas.forward(distance= height)
        canvas.left(90)

        canvas.forward(distance= width)
        canvas.left(90)

        canvas.forward(distance= height) # comes back to origin

class GuiPoint(Point):

    def draw_point(self, canvas, size= 5, color= 'pink'):
        canvas.penup() # hide()
        canvas.goto(x= self.x, y= self.y)

        canvas.pendown() # show()
        canvas.dot(size, color) # draws a point

rectangle = RectangleGui(
    lower_left= Point(x= randint(0, 100), y= randint(0, 100)),
    upper_right= Point(x= randint(100, 200), y= randint(100, 200))
)

user_point = GuiPoint(x= float(input("Enter x: ")),
                      y= float(input("Enter y: ")))

# Print the result
print(f"""
Rectangle coordinates:
lower_left = {(rectangle.lower_left.x, rectangle.lower_left.y)}
upper_right = {(rectangle.upper_right.x, rectangle.upper_right.y)}
""")

print(f"The given point is in rectangle : {rectangle.falls_in_rectangle(user_point)}")

# Display the result
my_turtle = turtle.Turtle()
rectangle.draw_gui(canvas= my_turtle)
user_point.draw_point(canvas= my_turtle)
turtle.done()

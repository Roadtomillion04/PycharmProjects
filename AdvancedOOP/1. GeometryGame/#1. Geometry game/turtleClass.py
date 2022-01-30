import turtle # for visualising

my_turtle = turtle.Turtle() # Turtle() is a class generates canvas

''' By default the origin starts at centre of window '''
# To change the origin of a rectangle
my_turtle.penup() # like hide() in godot
my_turtle.goto(x= 50, y= 70) # The goto() itself draws it's own line from origin

my_turtle.pendown() # to show() the rectangle
my_turtle.forward(distance= 100) # moves horizontally right given distance

# changes the angle of pointer by given degree
my_turtle.left(angle= 90)
my_turtle.forward(distance= 200)

# drawing top width
my_turtle.left(angle= 90)
my_turtle.forward(distance= 100)

# drawing left height, complete rectangle
my_turtle.left(angle= 90)
my_turtle.forward(distance= 200)

turtle.done() # Like root.mainloop() in tkinter
# or turtle.mainloop() both works the same
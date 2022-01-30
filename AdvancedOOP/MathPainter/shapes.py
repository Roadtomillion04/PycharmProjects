from canvas import Canvas

class Square(object):
    """
    draws a square with given shape, size and color
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas: Canvas):
                                # row (length)              # col (breadth)
        canvas.data[self.x : self.x + self.side, self.y : self.y + self.side] = self.color

class Rectangle(object):
    """
    draws a rectangle with given shape, size and color
    """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas: Canvas):
                            # row (length)                   # col (breadth)
        canvas.data[self.x : self.x + self.width, self.y : self.y + self.height] = self.color

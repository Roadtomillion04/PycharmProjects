from canvas import Canvas
from  shapes import Square, Rectangle
from file_sharer import FileSharer

canvas_width = int(input("Hey user, Enter the canvas width: "))
canvas_height = int(input("Hey user, Enter the canvas height: "))

colors: dict = {'white': [255, 255, 255], 'black': [0, 0, 0]}

canvas_color = input("Please Enter (white or black) color: ").lower()
assert canvas_color == 'black' or canvas_color == 'white', 'Please Enter black or white!'

canvas = Canvas(width= canvas_width,
                height= canvas_height,
                color= colors[canvas_color])

# Letting user to draw shapes as many they wanted
while True:
    decision = input('Enter shape(Rectangle or Square), press Q to quit: ')
    assert decision.lower() == 'rectangle' or decision.lower() == 'square' or decision.lower() == 'q', 'Please Enter correct command!'

    if decision.lower() == 'q':
        break

    if decision.lower() == 'rectangle':
        # As godot coordinates (0, 0) at top left
        rect_x = int(input('Enter starting x-coordinate: '))
        rect_y = int(input('Enter starting y-coordinate: '))
        assert rect_x < canvas.width and rect_y < canvas.height, f'You can\'t draw {decision.lower()} outside the canvas layer'

        rect_width = int(input('Enter length: '))
        rect_height = int(input('Enter breadth: '))
        assert rect_x + rect_width <= canvas.width and rect_y + rect_height <= canvas.height, f'{decision.lower()} goes outside the canvas layer'

        # colors
        red = int(input('Enter Red amount: '))
        green = int(input('Enter Green amount: '))
        blue = int(input('Enter Blue amount: '))
        assert red <= 255 and green <= 255 and blue <= 255, 'Please Enter RGB values'

        rectangle = Rectangle(x= rect_x,
                              y= rect_y,
                              width= rect_width,
                              height= rect_height,
                              color= [red, green, blue])
        rectangle.draw(canvas)

    if decision.lower() == 'square':
        sqr_x = int(input('Enter starting x coordinate: '))
        sqr_y = int(input('Enter starting y coordinate: '))
        assert sqr_x < canvas.width and sqr_y < canvas.height, 'Square canno\'t be drawn outside canvas layer'

        sqr_side = int(input('Enter side of a square: '))
        assert sqr_x + sqr_side <= canvas.width and sqr_y + sqr_side <= canvas.height, "Sqaure goes outside the rectangle"

        # colors
        red = int(input('Enter Red amount: '))
        green = int(input('Enter Green amount: '))
        blue = int(input('Enter Blue amount: '))
        assert red <= 255 and green <= 255 and blue <= 255, 'Please Enter RGB values'

        square = Square(x= sqr_x,
                        y= sqr_y,
                        side= sqr_side,
                        color= [red, green, blue])
        square.draw(canvas)

canvas.create('canvas.png')

# uploading image to cloud
file_sharer = FileSharer(image_path= 'canvas.png')
print(file_sharer.upload())

print('REPL link : https://replit.com/@NIRMAL-KUMARKU1/MathPainter?embed=1%20--Replt.it%20MathPainter')

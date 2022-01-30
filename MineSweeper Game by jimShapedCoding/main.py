import tkinter as tk
from Cell import Cell
import settings
import utilities

# root is a common convention
root = tk.Tk() # Creating a new window

# -------------------------------------------------------------------------
root.configure(bg= "black") # tkinter also supports hexadecimal value

root.geometry(newGeometry= f'{settings.WIDTH}x{settings.HEIGHT}') # setting screen resolution

root.title(string= "MineSweeper Game")

root.resizable(width= False, height= False) # blocks maximize window

top_frame = tk.Frame( # Frame is a container
    master= root, # inside root
    bg= 'red',
    width= settings.WIDTH, # size
    height= utilities.height_prct(25)
)
# placing container
top_frame.place(x= 0, y= 0) # As godot the top left axis is (0, 0)


# Setup game title
game_title = tk.Label(
    master= top_frame,
    bg= 'yellow',
    fg= 'black',
    text= 'MineSweeper',
    font= ("", settings.LABEL_SIZE * 2) # font-style, font-size
)

game_title.place(
    x= utilities.width_prct(33), # just random values to get text to center
    y= utilities.height_prct(5)
)

# ?? container
left_frame = tk.Frame(
    master= root,
    bg= 'salmon',
    width= utilities.width_prct(25),
    height= utilities.height_prct(100 - 25) # we used 25% space for top frame
)

left_frame.place(x= 0, y= utilities.height_prct(25)) # to place under top frame

# Game window container
center_frame = tk.Frame(
    master= root,
    bg= 'grey',
    width= utilities.width_prct(100 - 25), # we used 25% space for left frame
    height= utilities.height_prct(100 - 25) # we used 25% space for top frame
)
                        # 25%                              # 25%
center_frame.place(x= utilities.width_prct(100 - 75), y= utilities.height_prct(100 - 75))

'''
Let's create a Simple button 
btn1 = Cell()
btn1.create_btn_object(location= center_frame) # inside center frame
btn1.cell_btn_object.place(x= 0, y=0)

As we used place() it's not a best option to arrange multiple cell
we need some sort of grid, So let's use grid() method to place cells
'''

# Let's arrange a buttons
for row in range(settings.GRID_SIZE):
    for col in range(settings.GRID_SIZE):
        btn = Cell(x= row, y= col)
        btn.create_btn_object(location= center_frame)
        btn.cell_btn_object.grid(
            row= row,
            column= col
        )

Cell.create_label_object(location= left_frame)
Cell.cell_count_label_object.place(
    x= 0,
    y= 0
)
# print(Cell.all)
Cell.randomize_mines()

# -------------------------------------------------------------------------

root.mainloop() # Window Runs until exit button is pressed

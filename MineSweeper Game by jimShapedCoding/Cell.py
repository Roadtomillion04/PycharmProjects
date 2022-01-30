# Here we are going to create a cell class
from tkinter import Button, Label
import settings
import ctypes  # To pop GameOver & GameWon Message box


class Cell:
    all = [] # class attribute, to select all class instance
    cell_count_label_object = None # We gonna use it only one time
    cell_count = settings.CLICKABLE_CELLS
    def __init__(self, x, y, is_mine= False): # constructor method
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.cell_btn_object = None # later we can create different button objects

        self.is_cell_opened = False # to avoid decreasing if already opened
        self.is_mine_candidate = False # To markdown a cell when right clicked

        Cell.all.append(self) # appends itself when instanced

    def create_btn_object(self, location):
        btn = Button(
            master= location,
            # text= f"cell({self.x}, {self.y})",
            width= settings.BUTTON_SIZE * 4, # to occupy more width
            height= settings.BUTTON_SIZE,
        )
        # Let's assign action for left & right click
                                        # just assign func reference & bind pass event argument
        btn.bind(sequence= '<Button-1>', func= self.left_click_action) # Left click
        btn.bind(sequence= '<Button-3>', func= self.right_click_action) # Right click

        self.cell_btn_object = btn

    @staticmethod
    def create_label_object(location):
        label = Label(
            master= location,
            bg= "pink",
            fg= "black", # foreground
            text= f"Safe cells: {Cell.cell_count}",
            font= ("", settings.LABEL_SIZE) # font_type, font_size
        )

        Cell.cell_count_label_object = label

    def left_click_action(self, event): # bind pass event argument by default
        if not self.is_mine_candidate: # if marked by right clicked we can't left click
            if self.is_mine:
                self.show_mine()
            else:
                # to speed up progress
                if self.count_surrounded_mines == 0: # when count is 0 in all 8 dir
                    for cell_obj in self.surrounded_cells: # Display everything
                        cell_obj.display_mines_around()

                        cell_obj.cell_btn_object.unbind('<Button-1>')
                        cell_obj.cell_btn_object.unbind('<Button-3>')

                self.display_mines_around()

        # Cancel left and right click events if cell is opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

        # win condition
        if self.cell_count == 0:
            ctypes.windll.user32.MessageBoxW(0, "Congratulations!!", 'You won', 0)

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell # cell object

    @property
    def surrounded_cells(self):
        cells = []
        for i in range(-1, 2):
            for j in range(-1, 2):      # for edge cases like corners
                if self.get_cell_by_axis(self.x + i, self.y + j) is not None:
                    cells.append(self.get_cell_by_axis(self.x + i, self.y + j))

        return cells

    @property
    def count_surrounded_mines(self):
        mine_count = 0
        print(self.surrounded_cells)
        for cell in self.surrounded_cells:
            if cell.is_mine == True:
                mine_count += 1

        return mine_count

    def display_mines_around(self):
        if Cell.cell_count_label_object and not self.is_cell_opened:
            Cell.cell_count -= 1
            Cell.cell_count_label_object.configure(text= f"Safe cells: {Cell.cell_count}")
            self.is_cell_opened = True # to avoid decreasing if already opened

        self.cell_btn_object.configure(text= self.count_surrounded_mines)

    def show_mine(self):
        # A logic to interrupt the game and display a message that player lost!
        self.cell_btn_object.configure(bg= 'red')
        # configure is a universal method for all class to access it's attributes in tkinter

        ctypes.windll.user32.MessageBoxW(0, "You clicked on mine!", "Game Over", 0)

        # to exit
        import sys
        sys.exit()

    def right_click_action(self, event): # bind pass event argument by default
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg= 'light blue')
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg= "SystemButtonFace") # default tkinter bg
            self.is_mine_candidate = False

    @staticmethod # Static method can be accessed with Class.method() not instance.method()
    def randomize_mines(): # So no self
        import random
        # Let's use random.sample() same as df
        picked_cells = random.sample(
            population= Cell.all, # collection
            k= settings.MINE_COUNT # amount to select
        )
        print(picked_cells)
        for picked_cell in picked_cells:
            # Remember picked cell is a randomly chosen class
            picked_cell.is_mine = True


    def __repr__(self): # Represent object memory location to our format
        return f"Cell({self.x}, {self.y})"
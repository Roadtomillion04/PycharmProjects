WIDTH = 1280
HEIGHT = 720
GRID_SIZE = 6 # for 6 grids in row, col
BUTTON_SIZE= 5
CELL_COUNT = GRID_SIZE * GRID_SIZE
                        # odd returns float
MINE_COUNT = CELL_COUNT // 4 # 1/4 part contains mines
LABEL_SIZE = 32

CLICKABLE_CELLS = CELL_COUNT - MINE_COUNT
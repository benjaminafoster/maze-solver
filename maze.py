import time
from cell import Cell
from point import Point

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = [] # list of lists. each top-level list is a column of cells
        self._create_cells()
        self._break_entrace_and_exit()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells_list = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                col_cells_list.append(cell)
            self._cells.append(col_cells_list)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
                

    def _draw_cell(self, i, j):
        #print(f"cell size x: {self.cell_size_x}")
        tl_x_pos = (i * self.cell_size_x) + self.x1
        tl_y_pos = (j * self.cell_size_y) + self.y1
        lr_x_pos = tl_x_pos + self.cell_size_x
        lr_y_pos = tl_y_pos + self.cell_size_y
        self._cells[i][j].draw(tl_x_pos, tl_y_pos, lr_x_pos, lr_y_pos)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrace_and_exit(self): 
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols -1, self.num_rows - 1)
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
        self._create_cells()

    def _create_cells(self):
        self._cells = [] # list of lists. each top-level list is a column of cells
        for i in range(self.num_cols):
            col_cells_list = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                col_cells_list.append(cell)
                tl_point, lr_point = self._draw_cell(i, j)
                cell.draw(tl_point,lr_point)
                self._animate()
            self._cells.append(col_cells_list)

    def _draw_cell(self, i, j):
        #print(f"cell size x: {self.cell_size_x}")
        tl_x_pos = (i * self.cell_size_x) + self.x1
        tl_y_pos = (j * self.cell_size_y) + self.y1
        lr_x_pos = tl_x_pos + self.cell_size_x
        lr_y_pos = tl_y_pos + self.cell_size_y
        return [Point(tl_x_pos, tl_y_pos), Point(lr_x_pos, lr_y_pos)]
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
        